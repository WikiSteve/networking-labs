# Networking Labs Codex Knowledge Base

This repo is a library of vendor neutral networking labs.

Primary goals:
- Keep labs easy to edit in Obsidian (Markdown first).
- Keep labs readable on GitHub (GitHub Flavored Markdown).
- Convert H5P content to Markdown at scale.
- Keep interactivity where it matters, but do not turn this into a JavaScript hobby.

Non goals:
- Perfect grading in GitHub Markdown.
- Hiding exam content. This repo is for labs, not secure assessments.

## Repo layout

- `labs/`
  - Each lab has its own folder.
  - Naming convention: `NNN-slug`
  - Example: `labs/010-access-control-lists/`
  - Each lab folder contains:
    - `README.md` as the entry point
    - chapter pages like `01_introduction.md`
    - `assets/images/` for extracted H5P screenshots

- `h5p_src/`
  - Raw `.h5p` originals.
  - These are source assets, not what learners read.

- `tools/`
  - Conversion scripts.
  - Current main script: `tools/h5p_batch_to_md.py`

- `archive/`
  - Ignored on purpose. Do not commit.

## Authoring rules

### Markdown compatibility
Write for:
1) Obsidian preview
2) GitHub rendering

Avoid Obsidian only features unless they degrade gracefully on GitHub.

### Headings
- One `#` per page.
- Use `##` for major sections, `###` for steps inside a section.

### Code blocks
- Always fenced code blocks.
- Tag language when obvious: `bash`, `text`, `diff`.

### Images
- Store in `assets/images/`.
- Reference with relative links.
  - Example: `![Alt text](assets/images/file-xxxx.png)`
- Never inline base64 blobs.

### Links
- Use relative links inside a lab.
- Use repo relative links in the top level README.

### Callouts
GitHub supports alert blocks. Use these instead of custom HTML when possible:

```text
> [!NOTE]
> Something important.
```

Supported types worth using:
- NOTE
- TIP
- IMPORTANT
- WARNING
- CAUTION

### Tone
- Direct.
- Step based.
- Commands first, explanation after.
- Assume the reader is capable but busy.

## Conversion workflow at scale

### Batch convert H5P to Markdown
Inputs:
- Directory of .h5p files: `h5p_src/`

Outputs:
- One folder per lab inside an output dir.

Example:
```bash
python3 tools/h5p_batch_to_md.py h5p_src labs_out
```
Then promote outputs into `labs/NNN-slug/`.

### Find unhandled H5P blocks
After conversion, scan for placeholders:
```bash
grep -R "Unhandled H5P block" -n labs/ | sort
```
These are the current pain points that need post processing rules.

## H5P block mapping rules
The converter emits Markdown and sometimes HTML comments for unhandled blocks.
Codex should help by transforming unhandled blocks into GitHub friendly Markdown patterns.

### H5P.AdvancedText
- Keep as HTML if conversion is risky.
- Prefer to convert to Markdown when it is clean:
  - `<h2>` to `##`
  - `<ul>` to `-`
  - `<code>` to backticks or fenced blocks

### H5P.Image
- Copy file into `assets/images/`
- Use Markdown image syntax with relative path.

### H5P.Link
- Convert to `[text](url)`.

### H5P.MultiChoice
Convert into a static knowledge check with reveal.

Pattern:
```markdown
### 🧠 Knowledge Check: <title>

<Question text>

- [ ] Option A
- [ ] Option B
- [ ] Option C

<details>
<summary>Answer</summary>

**Correct:** Option B

Short explanation.
</details>
```
If H5P provides feedback per option, include it inside the details block as short bullets.

### H5P.TrueFalse
Convert into a binary check.

Pattern:
```markdown
### 🧠 Quick Check

Statement:

- [ ] True
- [ ] False

<details>
<summary>Answer</summary>

**Correct:** True

Why.
</details>
```

### H5P.DragText
Convert into a fill in the blanks check, still static.

Pattern:
```markdown
### 🧠 Knowledge Check: Drag Text

Fill the blanks, then reveal.

To have your virtual machine obtain an IP address from your home router, **[ BLANK ]** networking will be used.

<details>
<summary>Answer</summary>

Bridged

Optional explanation.
</details>
```
If there are multiple blanks, list them as Blank 1, Blank 2, etc.

### H5P.Video
If the video is external:
- Link it.
- Optionally add a screenshot thumbnail if present.

Pattern:
```markdown
### 🎥 Video

[Title](https://example)

Key takeaways:
- Bullet
- Bullet
```
If the video is bundled media:
- Place under `assets/video/` and link to it.
- Do not assume GitHub will inline play it.

### H5P.CoursePresentation or Interactive Book
This repo does not try to replicate slide logic.
We flatten into:
- One Markdown file per page.
- A `README.md` that lists pages in order.

## Lab folder conventions
Each lab folder should include:
- `README.md` with:
  - What you will do
  - Prereqs
  - Submission requirements
  - Table of contents
- Ordered pages:
  - `01_*.md`, `02_*.md`, etc
- `assets/images/` for screenshots

### README template
Use this skeleton:
```markdown
# <Lab Name>

## Goal
One paragraph.

## Prereqs
- Bullet list

## Deliverables
- Bullet list of required screenshots, files, or outputs

## Pages
- [01 Something](./01_something.md)
- [02 Something](./02_something.md)
```

## Quality checks
Before committing changes to a lab:
- All image links resolve.
- All intra lab links resolve.
- No Unhandled H5P block remains unless explicitly accepted.
- Pages render in GitHub without giant HTML mess.

Helpful commands:
```bash
# find broken relative links by eyeballing output quickly
grep -R "](assets/images/" -n labs/ | head

# find leftover placeholders
grep -R "Unhandled H5P block" -n labs/ || true
```

## Suggested Codex tasks
Codex should be used to:
- Proofread lab steps for clarity and consistency.
- Convert unhandled H5P blocks using the mapping rules above.
- Normalize headings and page structure.
- Fix image alt text and add missing captions.
- Keep changes localized to one lab per PR or commit.

Codex should NOT:
- Invent technical steps that are not in the source.
- Add external dependencies unless asked.
- Rewrite the lab voice into corporate training sludge.

## Commit habits
Keep commits small and scoped:
- One lab per commit when possible.
- Message format:
  - `lab(acl): convert multichoice blocks`
  - `lab(catalyst): fix image captions`
  - `tools: improve h5p_batch_to_md mappings`
