"""Player class for the Tic-tac-toe game."""


class Player:
    """A human player who picks moves via console input."""

    def __init__(self, marker):
        self.marker = marker

    def choose_move(self, board):
        while True:
            choice = input(f"Player {self.marker}, choose a position (1-9): ").strip()
            if not choice.isdigit():
                print("Please enter a number from 1 to 9.")
                continue

            position = int(choice)
            if position < 1 or position > 9:
                print("Please enter a number from 1 to 9.")
                continue

            index = position - 1
            if not board.is_empty(index):
                print("That position is already taken. Try another one.")
                continue

            return index
