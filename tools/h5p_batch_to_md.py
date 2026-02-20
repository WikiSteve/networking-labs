#!/usr/bin/env python3
"""
Batch convert .h5p InteractiveBook packages to GitHub-friendly Markdown.

- One folder per H5P file under the output directory
- One Markdown file per chapter (or index.md per chapter folder if you want)
- Copies image assets out of the .h5p zip into assets/images/
- Converts common content types:
  - H5P.AdvancedText: keeps HTML as-is (fast, faithful)
  - H5P.Image: links extracted files
  - H5P.Link: normal markdown links
  - H5P.DragText: converts to a fill-in-the-blanks prompt + <details> answer
Other widgets get a placeholder comment.

This stays standard-library only.
"""

import argparse
import json
import os
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from html import unescape

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "item"

def unzip_h5p(h5p_path: Path, out_dir: Path) -> None:
    with zipfile.ZipFile(h5p_path, "r") as z:
        z.extractall(out_dir)

def md_escape(s: str) -> str:
    return s.replace("\n", " ").strip()

def dragtext_to_md(params: dict) -> str:
    """
    H5P DragText stores a single text field with * markers around draggable words.
    """
    text = params.get("textField", params.get("text", "")) or ""
    text = unescape(text)

    # Extract answers between asterisks
    answers = re.findall(r"\*([^*]+)\*", text)
    
    # Create word bank (shuffled for extra challenge if desired, but here just listed)
    word_bank = sorted(list(set(answers)))
    word_bank_str = " | ".join(f"`{a}`" for a in word_bank)

    # Replace each *...* with a numbered placeholder ( 1 ), ( 2 ), etc.
    prompt = text
    for i in range(len(answers)):
        prompt = prompt.replace(f"*{answers[i]}*", f"**( {i+1} )**", 1)

    lines = [
        "---",
        "### 🧠 Knowledge Check: Fill in the Blanks",
        "",
        f"**Word Bank:** {word_bank_str}",
        "",
        "> [!IMPORTANT]",
        "> *Match the correct terms from the word bank to the numbered placeholders below.*",
        "> ",
        f"> {prompt.strip()}",
        "",
        "<details>",
        "<summary>👉 <b>Reveal answers</b></summary>",
        "",
        "\n".join(f"{i+1}. **{a}**" for i, a in enumerate(answers)),
        "</details>",
        "",
        "---"
    ]
    return "\n".join(lines)

def clean_html(html: str) -> str:
    """Basic HTML to Markdown conversion for common tags."""
    if not html:
        return ""
    # Unescape first
    s = unescape(html)
    # Remove some common wrappers if they are the only thing
    s = s.strip()
    
    # Replace headers
    s = re.sub(r"<(?:h1|h2)[^>]*>(.*?)</(?:h1|h2)>", r"## \1", s, flags=re.IGNORECASE)
    s = re.sub(r"<(?:h3|h4)[^>]*>(.*?)</(?:h3|h4)>", r"### \1", s, flags=re.IGNORECASE)
    
    # Replace bold/italic
    s = re.sub(r"<(?:strong|b)[^>]*>(.*?)</(?:strong|b)>", r"**\1**", s, flags=re.IGNORECASE)
    s = re.sub(r"<(?:em|i)[^>]*>(.*?)</(?:em|i)>", r"*\1*", s, flags=re.IGNORECASE)
    
    # Replace paragraphs with newlines
    s = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", s, flags=re.IGNORECASE | re.DOTALL)
    
    # Replace line breaks
    s = re.sub(r"<br\s*/?>", r"\n", s, flags=re.IGNORECASE)
    
    # Replace lists (simplified)
    # First, handle list items
    s = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", s, flags=re.IGNORECASE | re.DOTALL)
    # Then strip ul/ol tags
    s = re.sub(r"<(?:ul|ol)[^>]*>(.*?)</(?:ul|ol)>", r"\1\n", s, flags=re.IGNORECASE | re.DOTALL)
    
    # Replace code tags
    s = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", s, flags=re.IGNORECASE | re.DOTALL)
    s = re.sub(r"<pre[^>]*>(.*?)</pre>", r"```\n\1\n```\n", s, flags=re.IGNORECASE | re.DOTALL)
    
    # Strip any remaining tags (carefully)
    s = re.sub(r"<[^>]+>", "", s)
    
    # Cleanup extra newlines
    s = re.sub(r"\n{3,}", "\n\n", s)
    
    return s.strip()

def multichoice_to_md(params: dict, meta: dict) -> str:
    question = clean_html(params.get("question", ""))
    answers = params.get("answers", [])
    title = meta.get("title") or "Knowledge Check"
    
    lines = [
        "---",
        f"### 🧠 {title}",
        "",
        "> [!NOTE]",
        f"> **Question:** {question}",
        "> "
    ]
    
    correct_answers = []
    for i, ans in enumerate(answers):
        letter = chr(65 + i) # A, B, C...
        text = clean_html(ans.get("text", ""))
        is_correct = ans.get("correct", False)
        lines.append(f"> - [ ] **{letter}.** {text}")
        if is_correct:
            feedback = clean_html(ans.get("tipsAndFeedback", {}).get("chosenFeedback", ""))
            correct_answers.append((letter, text, feedback))
            
    lines.append("")
    lines.append("<details>")
    lines.append("<summary>👉 <b>Check your answer</b></summary>")
    lines.append("")
    for letter, text, feedback in correct_answers:
        lines.append(f"**Correct Option: {letter}**")
        if feedback:
            lines.append("")
            lines.append(f"**Feedback:** {feedback}")
    lines.append("</details>")
    lines.append("")
    lines.append("---")
    return "\n".join(lines)

def truefalse_to_md(params: dict, meta: dict) -> str:
    question = clean_html(params.get("question", ""))
    correct = params.get("correct") == "true"
    title = meta.get("title") or "Quick Check"
    feedback_correct = params.get("behaviour", {}).get("feedbackOnCorrect", "")
    feedback_wrong = params.get("behaviour", {}).get("feedbackOnWrong", "")
    
    lines = [
        "---",
        f"### 🧠 {title}",
        "",
        "> [!NOTE]",
        f"> **Statement:** {question}",
        "> ",
        "> - [ ] True",
        "> - [ ] False",
        "",
        "<details>",
        "<summary>👉 <b>Reveal answer</b></summary>",
        "",
        f"**Correct:** {'True' if correct else 'False'}"
    ]
    feedback = feedback_correct if correct else feedback_wrong
    if feedback:
        lines.append("")
        lines.append(f"**Feedback:** {clean_html(feedback)}")
    lines.append("</details>")
    lines.append("")
    lines.append("---")
    return "\n".join(lines)

def video_to_md(params: dict, meta: dict) -> str:
    title = meta.get("title") or "Video"
    sources = params.get("sources", [])
    url = sources[0].get("path") if sources else ""
    
    lines = [f"### 🎥 {title}", ""]
    if url:
        lines.append(f"[Watch Video]({url})")
    else:
        lines.append("*Video source missing*")
    return "\n".join(lines)

def convert_one(h5p_path: Path, out_root: Path) -> Path:
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        unzip_h5p(h5p_path, td_path)

        content_json = td_path / "content" / "content.json"
        if not content_json.exists():
            raise RuntimeError(f"Missing content.json in {h5p_path.name}")

        book = json.loads(content_json.read_text(encoding="utf-8"))
        title = (book.get("metadata", {}) or {}).get("title") or h5p_path.stem
        book_slug = slugify(title)

        out_dir = out_root / book_slug
        out_dir.mkdir(parents=True, exist_ok=True)

        img_dir = out_dir / "assets" / "images"
        img_dir.mkdir(parents=True, exist_ok=True)

        chapters = book.get("chapters", [])
        
        # Prepare chapter metadata
        chapter_files = []
        for i, ch in enumerate(chapters, start=1):
            ch_title = (ch.get("metadata", {}) or {}).get("title") or f"Chapter {i}"
            ch_slug = f"{i:02d}_{slugify(ch_title)}"
            chapter_files.append({
                "title": ch_title,
                "filename": f"{ch_slug}.md"
            })

        for i, ch in enumerate(chapters):
            ch_meta = chapter_files[i]
            md_file = out_dir / ch_meta["filename"]

            lines = [f"# {ch_meta['title']}", ""]

            col_params = (ch.get("params", {}) or {})
            blocks = col_params.get("content", [])

            for b in blocks:
                content = (b.get("content", {}) or {})
                lib = (content.get("library") or "").split()[0]
                params = content.get("params", {}) or {}
                meta = content.get("metadata", {}) or {}

                if lib == "H5P.AdvancedText":
                    html = (params.get("text", "") or "").strip()
                    if html:
                        lines.append(clean_html(html))
                        lines.append("")

                elif lib == "H5P.Image":
                    f = params.get("file", {}) or {}
                    rel_path = f.get("path")
                    if rel_path:
                        src = td_path / "content" / rel_path
                        if src.exists():
                            dest_name = os.path.basename(rel_path)
                            dest = img_dir / dest_name
                            shutil.copy2(src, dest)
                            alt = params.get("contentName") or meta.get("title") or "image"
                            lines.append(f"![{md_escape(alt)}](assets/images/{dest_name})")
                            lines.append("")

                elif lib == "H5P.Link":
                    lw = params.get("linkWidget", {}) or {}
                    url = (lw.get("protocol") or "") + (lw.get("url") or "")
                    text = params.get("title") or url
                    if url:
                        lines.append(f"[{md_escape(text)}]({url})")
                        lines.append("")

                elif lib == "H5P.DragText":
                    lines.append(dragtext_to_md(params))
                    lines.append("")

                elif lib == "H5P.MultiChoice":
                    lines.append(multichoice_to_md(params, meta))
                    lines.append("")

                elif lib == "H5P.TrueFalse":
                    lines.append(truefalse_to_md(params, meta))
                    lines.append("")

                elif lib == "H5P.Video":
                    lines.append(video_to_md(params, meta))
                    lines.append("")

                else:
                    lines.append(f"<!-- Unhandled H5P block: {lib} -->")
                    lines.append("")

            # Add navigation
            nav = []
            if i > 0:
                nav.append(f"[Prev]({chapter_files[i-1]['filename']})")
            nav.append("[Home](README.md)")
            if i < len(chapter_files) - 1:
                nav.append(f"[Next]({chapter_files[i+1]['filename']})")
            
            lines.append("---")
            lines.append(" | ".join(nav))

            md_file.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

        # Write a per-book README using the template from CODEX_KB.md
        readme_lines = [
            f"# {title}",
            "",
            "## Goal",
            "*(Add lab goal here)*",
            "",
            "## Prereqs",
            "- *(Add prerequisites here)*",
            "",
            "## Deliverables",
            "- *(Add deliverables here)*",
            "",
            "## Pages"
        ]
        for cf in chapter_files:
            readme_lines.append(f"- [{cf['title']}]({cf['filename']})")
            
        (out_dir / "README.md").write_text("\n".join(readme_lines).strip() + "\n", encoding="utf-8")
        return out_dir

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_dir", type=Path, help="Folder containing .h5p files")
    ap.add_argument("output_dir", type=Path, help="Folder to write Markdown books into")
    args = ap.parse_args()

    inp = args.input_dir
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)

    h5ps = sorted(inp.glob("*.h5p"))
    if not h5ps:
        raise SystemExit(f"No .h5p files found in {inp}")

    converted = []
    for h5p in h5ps:
        try:
            converted_dir = convert_one(h5p, out)
            converted.append(converted_dir)
            print(f"OK: {h5p.name} -> {converted_dir}")
        except Exception as e:
            print(f"FAIL: {h5p.name}: {e}")

    # Write a top-level README
    toc = ["# Course content", "", "## Books", ""]
    for d in converted:
        toc.append(f"- [{d.name}](./{d.name}/)")
    (out / "README.md").write_text("\n".join(toc).strip() + "\n", encoding="utf-8")

    print(f"Done. Converted {len(converted)}/{len(h5ps)} files into {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

