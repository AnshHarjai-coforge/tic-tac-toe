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
    print(f"You have chosed {valid_game_mode[game_mode]} mode\n")
    return int(game_mode)


def choose_CPU_difficulty():
    """Returns a valid CPU difficulty"""
    valid_cpu_difficulty = {"1": "Easy", "2": "Hard"}
    CPU_difficulty = check_valid_option("Please choose a valid CPU difficulty: 1 - Easy; 2 - Hard ", valid_cpu_difficulty)
    print("-"*100)
    print(f"You have chosed {valid_cpu_difficulty[CPU_difficulty]} mode\n")
    return int(CPU_difficulty)


if __name__ == "__main__":

    game_mode = choose_game_mode()

    if game_mode == 2:
        CPU_difficulty = choose_CPU_difficulty()

    