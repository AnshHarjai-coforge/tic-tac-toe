from game import Game, Player, GameState

def check_valid_option(prompt, valid_options):
    """Keep prompting the user to enter a valid option."""
    while True:
        selected_option = input(prompt)
        if selected_option in valid_options:
            return selected_option

        print(f"{selected_option} is not a valid option.")


def choose_game_mode():
    """Returns a valid game mode"""
    valid_game_mode = {"1": "human-vs-human", "2": "human-vs-computer"}
    game_mode = check_valid_option("Please choose a game mode: 1 - human-vs-human; 2 - human-vs-computer ", valid_game_mode)
    print("-"*100)
    print(f"You have chosen {valid_game_mode[game_mode]} mode\n")
    return int(game_mode)


def choose_CPU_difficulty():
    """Returns a valid CPU difficulty"""
    valid_cpu_difficulty = {"1": "Easy", "2": "Hard"}
    CPU_difficulty = check_valid_option("Please choose a valid CPU difficulty: 1 - Easy; 2 - Hard ", valid_cpu_difficulty)
    print("-"*100)
    print(f"You have chosen {valid_cpu_difficulty[CPU_difficulty]} difficulty\n")
    return int(CPU_difficulty)


def get_coordinates():
    """Keeps prompting the user until they enter a row and a column."""
    while True:
        coordinates = input("Enter a row and column from 1 to 3 where you want to place your mark: ")
        coordinates_list = coordinates.split()
        if len(coordinates_list) != 2:
            print(f"{coordinates} is not a valid input")
            continue
        try:
            row, col = int(coordinates_list[0])-1, int(coordinates_list[1])-1
        except ValueError:
            print(f"{coordinates} is not a valid input")
            continue
        return coordinates, row, col


def play_turn(new_game):
    """Asks the current player for a move and places it on the board."""
    player = new_game.current_player
    print(f"Hello {player.name} ({player.mark})")
    print(new_game.board.__str__())

    while True:
        coordinates, row, col = get_coordinates()
        if new_game.make_move(player, row, col):
            break
        print(f"{coordinates} is taken or off the board. Try again.")


def display_result(new_game):
    """Prints the final board and the winner or a draw."""
    print(new_game.board.__str__())
    winner = new_game.get_winner()
    if winner is not None:
        print(f"{winner.name} ({winner.mark}) wins")
    else:
        print("The game is a draw")


def play_human_vs_human():
    """Runs a human-vs-human game."""
    player_1 = Player('player 1', 'X')
    player_2 = Player('player 2', 'O')
    new_game = Game(player_1, player_2)

    while new_game.state == GameState.IN_PROGRESS:
        play_turn(new_game)

    display_result(new_game)


def main():
    game_mode = choose_game_mode()
    
    if game_mode == 2:
        CPU_difficulty = choose_CPU_difficulty()

    else:
        play_human_vs_human()


if __name__ == "__main__":
    main()
