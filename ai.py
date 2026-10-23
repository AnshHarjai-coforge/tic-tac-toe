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
