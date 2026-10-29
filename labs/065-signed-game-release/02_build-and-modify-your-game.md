# Build and Modify Your Game

The **publisher** completes this page. Start in **`~/game-release`** and choose one game.

## Choose your game

| Game | Source | Build | Run |
| --- | --- | --- | --- |
| **Snake Duel — default** | [nbsdgames](https://github.com/abakh/nbsdgames) | **`make snakeduel`** inside `nbsdgames/src` | **`./snakeduel`** |
| Battleship | [nbsdgames](https://github.com/abakh/nbsdgames) | **`make battleship`** inside `nbsdgames/src` | **`./battleship`** |
| Tetris | [jserv/tetris](https://github.com/jserv/tetris) | **`make`** inside `tetris` | **`./tetris`** |

Make reads the project's `Makefile` and compiles the game. A name after **`make`** selects one game. The `./` runs a program in your current directory.

### Snake Duel or Battleship

Download the source and build Snake Duel:

```bash
cd ~/game-release
git clone https://github.com/abakh/nbsdgames.git
cd nbsdgames/src
make snakeduel
./snakeduel
```

Use the arrow keys to steer and **Q** to quit. Press **F1** for controls or **F2** for gameplay help. Avoid the walls, yourself, and the other snake.

For Battleship, replace the last two commands with:

```bash
make battleship
./battleship
```

Choose single player for your first test. Use the arrow keys, **Enter**, and **R** to place and rotate ships. Follow the prompts, then use the arrow keys and **Enter** to fire. **Q** quits.

### Tetris

Use this route instead if you choose Tetris:

```bash
cd ~/game-release
git clone https://github.com/jserv/tetris.git
cd tetris
make
./tetris
```

Use the arrow keys to move, rotate, and drop blocks. **Q** opens the pause/quit dialog. Select Quit with the arrow keys and confirm with **Enter**. Use a terminal at least 80 columns wide and 24 rows tall. If the game reports that your terminal is too small, enlarge it and run the game again.

## Make it your edition

First confirm the original game runs. Quit before editing. Make **two source changes**:

- Add a short release label containing your name or group name to the game screen.
- Change one other visible feature or gameplay setting.

Keep the original copyright and licence notices. These games allow modification: nbsdgames uses [CC0](https://github.com/abakh/nbsdgames/blob/master/LICENSE), and Tetris uses the [MIT licence](https://github.com/jserv/tetris/blob/master/LICENSE).

### Snake Duel starting points

Open the source:

```bash
nano snakeduel.c
```

Search with **Ctrl+W** for `void logo(void)`. Change the text in its first `mvaddstr` call from `" _       _"` to a short label such as `"Alex Duel v1"`. Keep your label under 16 characters so it fits beside the score display. Change only the quoted text.

For a gameplay change, find `#define WIN_LIMIT 5`. Change `5` to `3` for a shorter match. This sets the initial round-win target; the game extends the target when both players reach the deciding round together.

Save with **Ctrl+O**, press **Enter**, then exit Nano with **Ctrl+X**. Rebuild and run:

```bash
make snakeduel
./snakeduel
```

### Alternative starting points

| Game | Release label | Second change |
| --- | --- | --- |
| Battleship | In `battleship.c`, replace the displayed `\|_)ATTLESHIP` strings with a short group label such as `Alex Fleet`; the title appears on several screens | Change the quoted ship-hit or victory messages, keeping them short enough to fit |
| Tetris | In `ui.c`, replace `"Next Block"` with a group label of at most 10 characters | In `game.c`, change `BASE_SCORE_PER_ROW` or `MAX_ROWS_PER_LEVEL` |

Use **`nano battleship.c`**, or **`nano ui.c`** followed by **`nano game.c`**, to edit the appropriate files. Re-run your game's build and run commands after saving. Change values or displayed text; preserve the surrounding C punctuation.

If compilation fails, read the first error and inspect the line you changed. If you still see the old game label, check that you saved the correct source file and rebuilt successfully.

## **Screenshot 1: Modified Game Running**

**Requirement:** Show your compiled game running in the terminal with your own release label visible.

Add a short caption beneath this screenshot in the submission template naming the source files you edited and explaining your two changes.

## Record your changes and build command

Quit the game. Create a note in your workspace:

```bash
cd ~/game-release
nano CHANGES.txt
```

Include your release label, the upstream repository URL, the files and changes you made, and the commands needed to compile and run your chosen game. Your trusted developer will use these notes after decrypting the source.

---
[Prev](01_setup-and-keys.md) | [Home](README.md) | [Next](03_package-protect-and-publish.md)
