## Goal

This is a command-line Tic-Tac-Toe game played on a 3x3 board where the two players take turns marking "O" and "X" on the board. The game supports two modes: human-versus-human and human-versus-computer, with two levels of difficulty for the computer opponent.

## Requirements

| ID | Requirement | How to verify it |
|---|---|---|
| R1 | The board is 3x3. X always goes first. | Test the board dimensions and verify that the first move is always X. |
| R2 | Players enter a move as a row and a column, numbered from 1, such as `2 3`. | Test valid coordinates such as `(1, 1)` and `(2, 3)`, and verify that invalid coordinates such as `(0, 1)` and `(2, 4)` are rejected. |
| R3 | Players must alternate their turns. | Make a valid X move and verify that O plays next, then verify that X plays after O. |
| R4 | A move to a taken cell, a cell off the board, or non-numeric input shows a message and lets the player try again. It does not use up the turn. | Test each invalid input and verify that the board and current player remain unchanged. |
| R5 | The game detects a win (across, down, or diagonal). | Test a winning board configuration for each direction and verify that a non-winning board is not detected as a win. |
| R6 | The game detects a draw when all cells are filled and no player has won. | Test a board without a winning configuration and verify that the game reports a draw. |
| R7 | Easy picks a random empty cell. | Seed the random number generator, verify that the choices are repeatable, and check that Easy always selects an empty cell. |
| R8 | Hard AI never loses against a human on a 3x3 board when playing as O. | Test Hard AI against every possible legal human move sequence and verify that the human never wins. |
| R9 | The game stops accepting moves after a win or draw. | Complete a game with a win and another with a draw, and verify that no additional moves are accepted. |

## Components

| Class / File Name | Function |
|---|---|
| `board.py` - `Board` | The Board class manages the 3x3 grid, keeps the board state private, validates moves, and checks for wins or draws. |
| `ai.py` - `AIPlayer`, `EasyAI`, `HardAI` | `AIPlayer` is the abstract base class that defines how an AI chooses a move. `EasyAI` picks a random empty cell, and `HardAI` uses minimax. Both use the same interface. |
| `game.py` | Manages turns, player modes, and win or draw checks. |
| `main.py` | Manages menus, prompts, printing, and displaying the game results. All terminal input and output will be handled here. |
| `tests/` | Contains pytest tests for the board, game, and AI. |
| `PLAN.md` | My written plan for the game. |
| `README.md` | Explains how to run the game and the tests. |
| `.github/workflows/ci.yml` | Runs the tests automatically through GitHub Actions. |

## Decisions

### 1. How to handle invalid moves

**Options considered**
- Reject invalid moves inside `main.py`.
- Let the Board class validate moves and report whether a move is valid.

**Chosen:** Let the Board class handle move validation.

**Why:** The board owns the state of the cells, so it is the appropriate place to determine whether a cell is available and within bounds. This also makes validation easier to test without terminal input.

### 2. How to detect a win

**Options considered**
- Write separate checks for every possible winning combination.
- Maintain a collection of all eight winning combinations and check them systematically.

**Chosen:** Maintain a collection of the eight winning combinations.

**Why:** This reduces duplicated logic and makes the win-detection code easier to read, test, and maintain.

## What changed

No changes have been made to the original plan yet. This section will be updated if the planned requirements, components, or design decisions change during implementation.