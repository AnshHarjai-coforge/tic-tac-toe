# tic-tac-toe

A command-line tic-tac-toe game on a 3x3 board. You can play another person, or play the computer on Easy or Hard. X always goes first. Type a move as a row and a column from 1 to 3, like `2 3`.

## Run the game

You need Python 3.12 or newer. From this folder:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

The first prompt is the mode: `1` for two people, `2` to play the computer. Against the computer, `1` is Easy (random empty cell) and `2` is Hard.

## Run the tests

With the same virtual environment active:

```bash
python -m pytest
```

That runs the board, game, and AI tests in `tests/`. All 36 passed.

## Tests

| What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|
| A new board | Created a `Board()` | Size 3, 9 empty cells, not full, corners blank | Size was 3, all 9 cells were empty | Yes |
| Board size | Tried `Board(2)` and `Board(4)` | Size 2 is rejected; size 4 has 16 cells | `Board(2)` raised `ValueError`; `Board(4)` had 16 empty cells | Yes |
| Cells off the board | Checked corners, then cells and ranges outside 0–2 | Corners are in range; outside cells are not, and `cell()` is `None` | Corners were in range; off-board cells came back as `None` | Yes |
| Placing a mark | Put X and O on empty cells, then O on a cell X already had | Empty cells take the mark; a taken cell keeps the old mark | Both marks landed; the second write on X's cell was rejected | Yes |
| A move off the board | Tried to place a mark at negative and size-3 coordinates | The move fails and the board stays empty | `place_mark` returned false and all 9 cells were still empty | Yes |
| Empty cells | Listed the open cells, then filled the center | All 9 cells at the start; the center drops out after it is filled | The list matched the grid, then had 8 cells | Yes |
| A full board | Filled one cell, then every cell | `is_full` is false while a cell is open, true when none are | False with one mark, true after all 9 were filled | Yes |
| A win on the board | Filled each row, each column, and both diagonals, plus one broken row | A full line wins for that mark; a broken line does not | Each full line won; the broken row did not | Yes |
| Removing a mark | Cleared the center, then tried cells off the board | The center is empty again; off-board calls do nothing | Center was blank; the corner mark stayed | Yes |
| Copying a board | Copied a board with X in the corner and marked each copy differently | The copy starts the same, then the two boards stay separate | Later marks showed up on only one board | Yes |
| Starting a game | Started a game with player 1 as X and player 2 as O | X goes first, the game is in progress, there is no winner, the board is empty | X was current, state was in progress, no winner, 9 empty cells | Yes |
| Taking turns | X played, then O, and I also had O try to move first | Players alternate; the other player cannot move on your turn | The turn switched after each legal move; O's early move was rejected | Yes |
| A bad move in a game | Played a taken cell and cells off the board | The move is rejected and the same player still has the turn | Both moves returned false and the current player did not change | Yes |
| X winning | Played out a row, a column, and both diagonals | The game is won by X | Each one ended as a win for X | Yes |
| O winning | Played a game where O finishes a line | The game is won by O | State was won and the winner was O | Yes |
| A draw | Filled the board with no three in a row | The game is a draw and there is no winner | State was draw, winner was none, board was full | Yes |
| A finished game | Tried another move after a win and after a draw | No further moves are accepted | Both extra moves were rejected and the result stayed the same | Yes |
| Easy AI | Used the same random seed twice, and picked on a board that already had marks | The same seed picks the same empty cell; the pick is always an empty cell | Both seeded runs matched, and the pick was an open cell | Yes |
| Hard AI as O | Let Hard answer every legal line of human moves | The human never wins | Hard held a draw or a win on every line | Yes |
