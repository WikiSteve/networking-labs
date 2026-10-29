# Build Your Game

Choose **one** game. Go Tetris has the fewest build dependencies; Snake Duel and Battleship are C/ncurses alternatives. All run entirely in the terminal.

| Game | Source URL | File to edit | Simple change |
| --- | --- | --- | --- |
| Go Tetris | https://github.com/cespare/go-tetris.git | `tetris/drawing.go` | Change `"SCORE"` to `"Alex SCORE"`, using your name |
| Snake Duel | https://github.com/abakh/nbsdgames.git | `src/snakeduel.c` | Change `"Your wins: %d"` to `"Alex wins: %d"`, keeping `%d` |
| Battleship | https://github.com/abakh/nbsdgames.git | `src/battleship.c` | Change the displayed `ATTLESHIP` text to your name on its title screens |

Keep labels short enough to fit. Keep the original licence: Go Tetris uses MIT and nbsdgames uses CC0. You may choose another free terminal game with an equally simple build and a licence that permits your release.

## Download and edit

```bash
mkdir ~/game-release
cd ~/game-release
mkdir incoming
```

Download [build-installer.sh](assets/build-installer.sh) using **Download raw file** on GitHub. If your browser saves it in `Downloads`, move it into your game folder:

```bash
mv ~/Downloads/build-installer.sh ~/game-release/
```

`incoming` will hold your partner's files separately from yours.

Replace `SOURCE_URL` with your chosen URL:

```bash
git clone SOURCE_URL source
cd source
```

The last word gives the downloaded project the folder name `source`.

Open the file from the table with **`nano`**, for example:

```bash
nano tetris/drawing.go
```

Use **Ctrl+W** to find the text. Make the name change, save with **Ctrl+O**, press **Enter**, then exit with **Ctrl+X**. One visible change is enough.

## Compile and play

For Go Tetris, from `source`:

```bash
go build
./go-tetris
```

Use the arrow keys, **Space** to drop, and **Q** to quit. Enlarge your terminal to about 100 columns by 40 rows so the board and controls fit.

For Snake Duel:

```bash
cd src
make snakeduel
./snakeduel
```

For Battleship, use **`make battleship`** and **`./battleship`** instead. Snake Duel uses arrow keys to steer. Battleship uses arrow keys, **Enter** and **R** to place/rotate ships, then arrow keys and **Enter** to fire. Both use **Q** to quit.

**`go build`** and **`make`** compile the source. `./` runs the executable in the current folder. Check that your name appears in the game.

## **Screenshot 1: Modified Game Running**

**Requirement:** Show your compiled game running with your name visible in its interface.

---
[Home](README.md) | [Next](02_sign-and-share.md)
