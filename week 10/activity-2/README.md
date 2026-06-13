# Activity 2 — Tic-tac-toe (Console)

A simple two-player command-line Tic-tac-toe game written in Python.
Players take turns marking positions on a 3×3 grid; the first to line up
three in a row (horizontally, vertically, or diagonally) wins.

## Features

- Two-player local play (`X` vs `O`)
- Numbered position guide (1–9) for easy input
- Input validation — rejects non-numeric, out-of-range, or occupied cells
- Win and draw detection
- Play-again prompt after each round

## Project layout

| File             | Responsibility                                          |
| ---------------- | ------------------------------------------------------- |
| `board.py`       | `Board` class — cells, placement, win/draw checks, view |
| `player.py`      | `Player` class — marker and console move input          |
| `game.py`        | `Game` class — turn loop wiring board and players       |
| `main.py`        | Entry point — play-again loop and `main()`              |

## Run

```bash
python3 main.py
```

## How to play

The board cells are numbered 1–9, left-to-right and top-to-bottom:

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

On each turn, enter the number of the cell you want to claim. `X` plays
first. The game ends when a player gets three in a row or the board fills
up (draw).
