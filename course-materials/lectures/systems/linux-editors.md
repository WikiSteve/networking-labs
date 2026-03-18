# Linux Editors

- Filename: `Linux Editors.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Linux%20Editors.pptx)

## Summary

This reusable introductory lecture deck covers Linux text editors with an emphasis on practical survival skills rather than deep editor theory. It surveys the difference between graphical editors like `gedit` and terminal-based editors such as `nano`, `emacs`, `vi`, and `joe`, then spends most of its instructional weight on `nano` and especially `vi` or `vim`. The deck explains why `nano` became popular as a GNU-licensed Pico-style editor and highlights features like syntax highlighting, line numbers, regular expressions, multiple buffers, indentation, and undo or redo. It then frames `vi` as historically important and still essential because some systems may only provide `vi`, making it a required competency even if other tools are preferred.

## Key Details

- Introduces both graphical and text-based editors, naming `gedit`, `nano`, `emacs`, `vi`, and `joe`.
- Explains the origin of `nano` as a GNU-licensed editor meant to feel like Pico.
- Lists useful `nano` features including syntax highlighting, line numbers, regular expressions, multiple buffers, indenting groups of lines, and undo or redo.
- Mentions Emacs only briefly and explicitly notes that it is not covered in the course.
- Treats `vi` or `vim` as essential because some systems may only have `vi` available.
- States the minimum required `vi` knowledge: command mode, insert mode, `hjkl` movement, typing in insert mode, and using Escape to return to command mode.
- Includes a historical note about arrow keys generating escape sequences and suggests reproducing this by launching `sh` instead of `bash`.
- Teaches basic `vi` editing commands such as `i`, `A`, `dd`, and `x`.
- Explicitly requires completion of `vimtutor`.
- Covers `vi` search commands such as `/string`, `?string`, `n`, and `N`.
- Introduces substitution syntax `:s/pattern/string/flag` with `g` and `c` flags.
- Encourages building a cheat sheet for search and replace commands.

## Tags

- `linux`
- `text-editors`
- `nano`
- `vim`
- `vi`
- `vimtutor`
- `command-line`
- `lecture`
