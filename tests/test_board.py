import pytest
from board import Board


def test_new_board_is_empty():
    board = Board()
    assert board.size == 3
    assert len(board.empty_cells()) == 9
    assert board.is_full() is False
    assert board.cell(0, 0) == " "
    assert board.cell(2, 2) == " "


def test_size_cannot_be_less_than_three():
    with pytest.raises(ValueError):
        Board(2)


def test_custom_size_has_that_many_cells():
    board = Board(4)
    assert board.size == 4
    assert len(board.empty_cells()) == 16


def test_cell_outside_the_board_is_none():
    board = Board()
    assert board.cell(-1, 0) is None
    assert board.cell(0, -1) is None
    assert board.cell(3, 0) is None
    assert board.cell(0, 3) is None


def test_in_range_accepts_every_corner():
    board = Board()
    assert board._in_range(0, 0) is True
    assert board._in_range(0, 2) is True
    assert board._in_range(2, 0) is True
    assert board._in_range(2, 2) is True


def test_in_range_rejects_cells_outside_the_board():
    board = Board()
    assert board._in_range(-1, 0) is False
    assert board._in_range(0, -1) is False
    assert board._in_range(3, 0) is False
    assert board._in_range(0, 3) is False


def test_place_mark_on_an_empty_cell():
    board = Board()
    assert board.place_mark(0, 0, "X") is True
    assert board.cell(0, 0) == "X"
    assert board.place_mark(2, 2, "O") is True
    assert board.cell(2, 2) == "O"


def test_place_mark_on_a_taken_cell():
    board = Board()
    board.place_mark(0, 0, "X")
    assert board.place_mark(0, 0, "O") is False
    assert board.cell(0, 0) == "X"


def test_place_mark_off_the_board():
    board = Board()
    assert board.place_mark(-1, 0, "X") is False
    assert board.place_mark(0, -1, "X") is False
    assert board.place_mark(3, 0, "X") is False
    assert board.place_mark(0, 3, "X") is False
    assert len(board.empty_cells()) == 9


def test_empty_cells_lists_every_open_cell():
    board = Board()
    assert board.empty_cells() == [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
    ]

    board.place_mark(1, 1, "X")
    assert (1, 1) not in board.empty_cells()
    assert len(board.empty_cells()) == 8


def test_is_full_is_false_while_a_cell_is_open():
    board = Board()
    board.place_mark(0, 0, "X")
    assert board.is_full() is False


def test_is_full_is_true_when_every_cell_is_taken():
    board = Board()
    for row in range(3):
        for col in range(3):
            board.place_mark(row, col, "X")

    assert board.empty_cells() == []
    assert board.is_full() is True


def test_has_won_across_every_row():
    for row in range(3):
        board = Board()
        for col in range(3):
            board.place_mark(row, col, "X")

        assert board.has_won("X") is True
        assert board.has_won("O") is False


def test_has_won_down_every_column():
    for col in range(3):
        board = Board()
        for row in range(3):
            board.place_mark(row, col, "O")

        assert board.has_won("O") is True
        assert board.has_won("X") is False


def test_has_won_on_the_main_diagonal():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "X")
    board.place_mark(2, 2, "X")
    assert board.has_won("X") is True
    assert board.has_won("O") is False


def test_has_won_on_the_other_diagonal():
    board = Board()
    board.place_mark(0, 2, "O")
    board.place_mark(1, 1, "O")
    board.place_mark(2, 0, "O")
    assert board.has_won("O") is True
    assert board.has_won("X") is False


def test_has_won_is_false_when_a_line_is_broken():
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "O")
    board.place_mark(0, 2, "X")
    assert board.has_won("X") is False
    assert board.has_won("O") is False


def test_remove_mark_clears_a_filled_cell():
    board = Board()
    board.place_mark(1, 1, "O")
    board.remove_mark(1, 1)
    assert board.cell(1, 1) == " "
    assert (1, 1) in board.empty_cells()


def test_remove_mark_outside_the_board_does_nothing():
    board = Board()
    board.place_mark(0, 0, "X")
    board.remove_mark(3, 0)
    board.remove_mark(-1, 0)
    assert board.cell(0, 0) == "X"
    assert len(board.empty_cells()) == 8


def test_copy_has_the_same_marks_and_is_separate():
    board = Board()
    board.place_mark(0, 0, "X")
    clone = board.copy()

    assert clone.size == board.size
    assert clone.cell(0, 0) == "X"

    clone.place_mark(0, 1, "O")
    assert board.cell(0, 1) == " "

    board.place_mark(1, 0, "O")
    assert clone.cell(1, 0) == " "