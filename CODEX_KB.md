# Networking Labs Codex Knowledge Base

This repo is a library of vendor-neutral networking labs.

## Primary goals
- **Markdown First:** Keep labs easy to edit in Obsidian and readable on GitHub.
- **High Visual Contrast ("Pop"):** Technical commands must be visually distinct from descriptive text.
- **De-cluttered Structure:** Avoid unnecessary numbering. Use bullet points or flat headers for non-sequential information.
- **Robust Interactivity:** Use "Framed" knowledge checks that work reliably across platforms.

## Repository Layout
- `labs/`: One folder per lab (e.g., `010-access-control-lists`).
- `h5p_src/`: Raw `.h5p` originals (source only).
- `tools/`: Conversion scripts.
  - **Main Script:** `tools/h5p_batch_to_md.py` (Handles H5P -> MD conversion, image extraction, and formatting).

## Authoring & Formatting Standards

### 1. Command Syntax ("The Pop")
Technical commands must stand out.
- **Inline Commands:** Bold and backticked.
  - *Bad:* Run the `ip address` command.
  - *Good:* Run the **`ip address`** command.
- **Configuration Blocks:** Use fenced code blocks with language tags (`bash`, `plaintext`).
  - *Good:*
    ```bash
    interface vlan 1
    ip address 192.168.1.1 255.255.255.0
    ```

### 2. Lists vs. Headers
**Do not use numbered lists for document structure.**
- *Bad:*
  1. ### Introduction
  2. **Step 1**
- *Good:*
  ### Introduction
  **Step 1**

Use bullet points for lists of items. Use numbers ONLY for strictly sequential steps where order is critical.

### 3. "Framed" Knowledge Checks
To ensure `<details>` toggles work correctly on GitHub, use the "Framed" style where the interactive part sits **outside** the alert block.

**Pattern:**
```markdown
---
### 🧠 Activity Title

> [!NOTE]
> **Question:** What is the answer?
>
> - [ ] Option A
> - [ ] Option B

<details>
<summary>👉 <b>Check your answer</b></summary>

**Correct Option: A**

**Feedback:** Detailed explanation here.
</details>

---
```

## Conversion Workflow for New H5P Content

1. **Run the Converter:**
   The `tools/h5p_batch_to_md.py` script has been upgraded to handle:
   - Deep HTML cleaning.
   - Automatic "Framed" style generation for MultiChoice, TrueFalse, and DragText.
   - Image extraction and linking.
   - Navigation link generation (`[Prev] | [Home] | [Next]`).

   ```bash
   python3 tools/h5p_batch_to_md.py h5p_src labs_new
   ```

2. **Manual Polish (The "De-clutter" Pass):**
   After conversion, a human (or agent) must:
   - **Flatten Lists:** Remove artifact `1.` numbers from headers and non-sequential lists.
   - **Check Command Formatting:** Ensure the script caught all commands; manually bold inline commands if missed.
   - **Verify Images:** Ensure images are placed correctly and referenced.

## Agent Roles (Ref. AGENTS.md)
- **Converter:** Runs the script.
- **Polisher:** Applies the "Pop" and removes numbering artifacts.
- **Quiz Master:** Verifies correct answers against the H5P source (using `tools/extract_answers.py` logic if needed).
