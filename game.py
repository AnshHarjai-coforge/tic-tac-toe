from board import Board
from enum import Enum
from typing import Optional

class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark



class GameState(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    WON = "WON"
    DRAW = "DRAW"


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.state = GameState.IN_PROGRESS
        self.winner: Optional["Player"] = None

    def make_move(self, player, row:int, col: int) -> bool:
        if self.state is not GameState.IN_PROGRESS:
            return False
        if player is not self.current_player:
            return False

        if not self.board.place_mark(row, col, player.mark):
            return False


        if self.board.has_won(player.mark):
            self.state = GameState.WON
            self.winner = player
        elif self.board.is_full():
            self.state = GameState.DRAW
        else:
            self.current_player = self.player2 if self.current_player is self.player1 else self.player1

        return True

    def get_current_player(self) -> Player:
        return self.current_player

    def get_game_state(self) -> GameState:
        return self.state

    def get_winner(self) -> Optional[Player]:
        return self.winner

    def get_board(self) -> Board:
        return self.board
