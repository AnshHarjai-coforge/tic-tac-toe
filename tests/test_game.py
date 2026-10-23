from game import Game, Player, GameState


def make_game():
    player_1 = Player('player 1', 'X')
    player_2 = Player('player 2', 'O')
    return Game(player_1, player_2)


def test_x_goes_first():
    new_game = make_game()
    assert new_game.get_current_player() is new_game.player1
    assert new_game.get_current_player().mark == "X"
    assert new_game.get_game_state() is GameState.IN_PROGRESS
    assert new_game.get_winner() is None
    assert len(new_game.get_board().empty_cells()) == 9


def test_players_alternate_turns():
    new_game = make_game()
    assert new_game.make_move(new_game.player1, 0, 0) is True
    assert new_game.get_current_player() is new_game.player2

    assert new_game.make_move(new_game.player2, 1, 1) is True
    assert new_game.get_current_player() is new_game.player1
    assert new_game.get_board().cell(0, 0) == "X"
    assert new_game.get_board().cell(1, 1) == "O"


def test_wrong_player_cannot_move():
    new_game = make_game()
    assert new_game.make_move(new_game.player2, 0, 0) is False
    assert new_game.get_current_player() is new_game.player1
    assert len(new_game.get_board().empty_cells()) == 9


def test_taken_cell_does_not_use_the_turn():
    new_game = make_game()
    new_game.make_move(new_game.player1, 0, 0)

    assert new_game.make_move(new_game.player2, 0, 0) is False
    assert new_game.get_current_player() is new_game.player2


def test_move_off_the_board_does_not_use_the_turn():
    new_game = make_game()
    assert new_game.make_move(new_game.player1, 3, 0) is False
    assert new_game.make_move(new_game.player1, -1, 0) is False
    assert new_game.get_current_player() is new_game.player1
    assert new_game.get_game_state() is GameState.IN_PROGRESS
    assert len(new_game.get_board().empty_cells()) == 9


def test_game_detects_a_row_win():
    new_game = make_game()
    moves = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
    for row, col in moves:
        player = new_game.get_current_player()
        assert new_game.make_move(player, row, col) is True

    assert new_game.get_game_state() is GameState.WON
    assert new_game.get_winner() is new_game.player1
    assert new_game.get_winner().mark == "X"


def test_game_detects_a_column_win():
    new_game = make_game()
    moves = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
    for row, col in moves:
        player = new_game.get_current_player()
        assert new_game.make_move(player, row, col) is True

    assert new_game.get_game_state() is GameState.WON
    assert new_game.get_winner() is new_game.player1


def test_game_detects_a_diagonal_win():
    new_game = make_game()
    moves = [(0, 0), (0, 1), (1, 1), (0, 2), (2, 2)]
    for row, col in moves:
        player = new_game.get_current_player()
        assert new_game.make_move(player, row, col) is True

    assert new_game.get_game_state() is GameState.WON
    assert new_game.get_winner().mark == "X"


def test_game_detects_the_other_diagonal_win():
    new_game = make_game()
    moves = [(0, 2), (0, 0), (1, 1), (1, 0), (2, 0)]
    for row, col in moves:
        player = new_game.get_current_player()
        assert new_game.make_move(player, row, col) is True

    assert new_game.get_game_state() is GameState.WON
    assert new_game.get_winner() is new_game.player1


def test_o_can_win():
    new_game = make_game()
    moves = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (1, 2)]
    for row, col in moves:
        player = new_game.get_current_player()
        assert new_game.make_move(player, row, col) is True

    assert new_game.get_game_state() is GameState.WON
    assert new_game.get_winner() is new_game.player2
    assert new_game.get_winner().mark == "O"


def test_game_detects_a_draw():
    new_game = make_game()
    moves = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (1, 1), (2, 2), (2, 1)]
    for row, col in moves:
        player = new_game.get_current_player()
        assert new_game.make_move(player, row, col) is True

    assert new_game.get_game_state() is GameState.DRAW
    assert new_game.get_winner() is None
    assert new_game.get_board().is_full() is True


def test_no_moves_are_accepted_after_a_win():
    new_game = make_game()
    moves = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
    for row, col in moves:
        player = new_game.get_current_player()
        new_game.make_move(player, row, col)

    empty_before = len(new_game.get_board().empty_cells())
    assert new_game.make_move(new_game.player2, 2, 2) is False
    assert new_game.get_game_state() is GameState.WON
    assert new_game.get_winner() is new_game.player1
    assert len(new_game.get_board().empty_cells()) == empty_before


def test_no_moves_are_accepted_after_a_draw():
    new_game = make_game()
    moves = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (1, 1), (2, 2), (2, 1)]
    for row, col in moves:
        player = new_game.get_current_player()
        new_game.make_move(player, row, col)

    assert new_game.make_move(new_game.player1, 0, 0) is False
    assert new_game.make_move(new_game.player2, 1, 1) is False
    assert new_game.get_game_state() is GameState.DRAW
    assert new_game.get_winner() is None