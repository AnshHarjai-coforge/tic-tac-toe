import random
from board import Board
from ai import EasyAI, HardAI


def test_easy_ai_picks_the_same_empty_cell_when_seeded():
    board = Board()
    board.place_mark(0, 0, "X")

    easy_1 = EasyAI(random.Random(1))
    easy_2 = EasyAI(random.Random(1))
    move_1 = easy_1.choose_move(board, "O")
    move_2 = easy_2.choose_move(board, "O")

    assert move_1 == move_2
    assert move_1 in board.empty_cells()


def test_easy_ai_picks_an_empty_cell_on_a_used_board():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")

    easy = EasyAI(random.Random(5))
    row, col = easy.choose_move(board, "X")

    assert board.cell(row, col) == " "
    assert (row, col) in board.empty_cells()


def hard_ai_holds_as_o(board, humans_turn, cpu):
    if board.has_won("X"):
        return False
    if board.has_won("O") or board.is_full():
        return True

    if humans_turn:
        for row, col in board.empty_cells():
            clone = board.copy()
            clone.place_mark(row, col, "X")
            if hard_ai_holds_as_o(clone, False, cpu) is False:
                return False
        return True

    row, col = cpu.choose_move(board, "O")
    clone = board.copy()
    clone.place_mark(row, col, "O")
    return hard_ai_holds_as_o(clone, True, cpu)


def test_hard_ai_never_loses_as_o():
    cpu = HardAI(random.Random(0))
    assert hard_ai_holds_as_o(Board(), True, cpu) is True
