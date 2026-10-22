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
        '''Returns True if player is able to place a mark on the board, False otherwise.'''
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
        '''Returns the player whose turn it is.'''
        return self.current_player

    def get_game_state(self) -> GameState:
        '''Returns the state - In_progress / Win / Draw of the current game'''
        return self.state

    def get_winner(self) -> Optional[Player]:
        '''Returns the winner player (if any) of the current game'''
        return self.winner

    def get_board(self) -> Board:
        '''Returns the current board object of class Board'''
        return self.board
