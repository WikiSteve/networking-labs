# Agents for Codex

This repo uses lightweight agent roles to keep edits predictable.

Each agent should operate with:
- Small diffs.
- Clear commit messages.
- No invented content.
- Preserve the lab author voice.

## Agent: Maintainer
Owner: Steve Sharpe

Responsibilities:
- Final say on structure and tone.
- Approves major refactors.
- Decides when to keep H5P as H5P versus flatten to Markdown.

## Agent: Converter
Goal: Convert H5P derived content into GitHub friendly Markdown.

Inputs:
- `.h5p` under `h5p_src/`
- Extracted conversion output under `labs_out/` or similar

Outputs:
- Clean lab folder under `labs/NNN-slug/`

Rules:
- Use `assets/images/` for images.
- Never inline base64.
- Leave a placeholder only when the block mapping cannot be applied.

## Agent: Quiz Transformer
Goal: Replace unhandled H5P quiz blocks with static Markdown knowledge checks.

Handles:
- H5P.MultiChoice
- H5P.TrueFalse
- H5P.DragText

Output patterns:
- Checkboxes plus `<details>` reveal.
- Keep explanations short.
- Do not add new questions.

## Agent: Proofreader
Goal: Improve readability without changing meaning.

Allowed:
- Fix grammar and spelling.
- Tighten steps.
- Normalize terminology.
- Convert passive voice to active voice.

Not allowed:
- Adding new tools or new lab requirements.
- Changing the technical intent.

Checklist:
- Headings are consistent.
- Commands are copy pasteable.
- Deliverables are explicit.

## Agent: Link and Asset Fixer
Goal: Make navigation and assets reliable.

Tasks:
- Ensure every lab `README.md` links to its pages.
- Ensure all images resolve with relative paths.
- Ensure cross links stay inside the repo.

Rules:
- Prefer `./README.md` for lab entry links.
- Do not link to local filesystem paths.

## Agent: Structure Editor
Goal: Keep the library tidy as it grows.

Tasks:
- Enforce `NNN-slug` folder naming.
- Ensure page naming uses `NN_` prefix for stable ordering.
- Avoid duplicate asset filenames if collisions appear.

Not allowed:
- Large sweeping renames without reason.
- Renaming that breaks existing links without fixing them.

## Agent: Release Helper
Goal: Prep the repo for sharing.

Tasks:
- Confirm repo root README is current.
- Confirm Git LFS tracking is in place for `.h5p` if used.
- Confirm no `archive/` content is tracked.

## Operating procedure

When working on a lab:
1) Pick one lab folder under `labs/`.
2) Make changes only inside that folder.
3) Run a quick scan:
   - `grep -R "Unhandled H5P block" -n labs/NNN-slug || true`
4) Commit with a scoped message.

Suggested PR titles:
- `lab(acl): transform quizzes to markdown`
- `lab(catalyst): proofread and fix navigation`
- `tools: improve h5p_batch_to_md mappings`

## Prompts for Codex

Converter prompt:
- Convert H5P output into clean Markdown pages under `labs/NNN-slug/`. Follow CODEX_KB.md rules. Do not add new content.

Quiz Transformer prompt:
- Replace any `Unhandled H5P block` placeholders with GitHub friendly knowledge checks using `<details>` reveal. Keep original question text.

Proofreader prompt:
- Tighten instructions, fix grammar, keep meaning identical. Keep commands unchanged.

Link and Asset Fixer prompt:
- Fix broken relative links and image paths. Do not change filenames unless necessary.

Structure Editor prompt:
- Enforce naming conventions. Fix ordering issues. Update README navigation accordingly.
