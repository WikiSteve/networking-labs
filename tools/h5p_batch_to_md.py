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
    Example: "To get an IP from home router *bridged*..."
    """
    text = params.get("text", "") or ""
    # Some exports contain HTML entities.
    text = unescape(text)

    # Extract answers between asterisks
    answers = re.findall(r"\*([^*]+)\*", text)
    prompt = re.sub(r"\*([^*]+)\*", "[ ... ]", text)

    lines = []
    lines.append("🧠 **Knowledge Check**")
    lines.append("")
    lines.append("Drag the words into the correct boxes, then check your work.")
    lines.append("")
    lines.append(prompt.strip())
    lines.append("")
    if answers:
        lines.append("<details>")
        lines.append("<summary><b>Reveal answers</b></summary>")
        lines.append("")
        lines.append("**Answers (in order):** " + ", ".join(f"`{md_escape(a)}`" for a in answers))
        lines.append("</details>")
        lines.append("")
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
        index_lines = [f"# {title}", "", "## Table of contents", ""]

        for i, ch in enumerate(chapters, start=1):
            ch_title = (ch.get("metadata", {}) or {}).get("title") or f"Chapter {i}"
            ch_slug = f"{i:02d}_{slugify(ch_title)}"
            md_file = out_dir / f"{ch_slug}.md"

            index_lines.append(f"- [{ch_title}]({md_file.name})")

            lines = [f"# {ch_title}", ""]

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
                        lines.append(html)
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

                else:
                    lines.append(f"<!-- Unhandled H5P block: {lib} -->")
                    lines.append("")

            md_file.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

        # Write a per-book README that GitHub renders nicely
        (out_dir / "README.md").write_text("\n".join(index_lines).strip() + "\n", encoding="utf-8")
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

