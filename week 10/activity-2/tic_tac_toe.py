"""Simple two-player command-line Tic-tac-toe game.

Run this module directly to play:

    python tic_tac_toe.py
"""


def create_board():
    """Return an empty 3x3 board represented as a list of nine spaces."""
    return [" "] * 9


def print_board(board):
    """Print the current board to the console."""
    print()
    for row in range(3):
        start = row * 3
        print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
        if row < 2:
            print("-----------")
    print()


def print_position_guide():
    """Print a numbered guide showing how positions map to the board."""
    print("Positions:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()


def get_player_move(board, player):
    """Prompt the player for a valid move and return the chosen index."""
    while True:
        choice = input(f"Player {player}, choose a position (1-9): ").strip()
        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice)
        if position < 1 or position > 9:
            print("Please enter a number from 1 to 9.")
            continue

        index = position - 1
        if board[index] != " ":
            print("That position is already taken. Try another one.")
            continue

        return index


def check_winner(board, player):
    """Return True if the given player has a winning line on the board."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    for first, second, third in winning_lines:
        if board[first] == board[second] == board[third] == player:
            return True
    return False


def is_board_full(board):
    """Return True when there are no empty cells left on the board."""
    return all(cell != " " for cell in board)


def play_game():
    """Play a single round of Tic-tac-toe between two human players."""
    board = create_board()
    current_player = "X"

    print("Welcome to Tic-tac-toe!")
    print_position_guide()

    while True:
        print_board(board)
        index = get_player_move(board, current_player)
        board[index] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        current_player = "O" if current_player == "X" else "X"


def main():
    """Run games until the players choose to stop."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
