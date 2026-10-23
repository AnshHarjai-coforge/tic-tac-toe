from abc import ABC, abstractmethod


class AIPlayer(ABC):
    def __init__(self, rng):
        self.rng = rng


    @abstractmethod
    def choose_move(self, board, mark):
        """Returns the (row, col) where this player wants to play."""
        pass


class EasyAI(AIPlayer):
    def choose_move(self, board, mark):
        """Picks a random empty cell."""
        empty_cells = board.empty_cells()
        return self.rng.choice(empty_cells)


class HardAI(AIPlayer):
    def choose_move(self, board, mark):
        """Picks the move that gives the best result."""
        best_score = None
        best_moves = []
        opponent = "O" if mark == "X" else "X"

        for row, col in board.empty_cells():
            clone = board.copy()
            clone.place_mark(row, col, mark)
            score = self._minimax(clone, opponent, mark)

            if best_score is None or score > best_score:
                best_score = score
                best_moves = [(row, col)]
            elif score == best_score:
                best_moves.append((row, col))

        return self.rng.choice(best_moves)


    def _minimax(self, board, current_mark, ai_mark):
            """Returns 1 for a forced win, -1 for a loss, and 0 for a draw."""
            opponent = "O" if ai_mark == "X" else "X"
            if board.has_won(ai_mark):
                return 1
            if board.has_won(opponent):
                return -1
            if board.is_full():
                return 0

            next_mark = "O" if current_mark == "X" else "X"
            best_score = None

            for row, col in board.empty_cells():
                clone = board.copy()
                clone.place_mark(row, col, current_mark)
                score = self._minimax(clone, next_mark, ai_mark)

                if best_score is None:
                    best_score = score
                elif current_mark == ai_mark and score > best_score:
                    best_score = score
                elif current_mark != ai_mark and score < best_score:
                    best_score = score

            return best_score