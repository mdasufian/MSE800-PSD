"""Board class for the Tic-tac-toe game."""


class Board:
    """A 3x3 Tic-tac-toe board."""

    EMPTY = " "
    SIZE = 9
    WINNING_LINES = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )

    def __init__(self):
        self._cells = [Board.EMPTY] * Board.SIZE

    def is_empty(self, index):
        return self._cells[index] == Board.EMPTY

    def place(self, index, marker):
        if not self.is_empty(index):
            raise ValueError("Cell is already taken.")
        self._cells[index] = marker

    def is_full(self):
        return all(cell != Board.EMPTY for cell in self._cells)

    def has_winner(self, marker):
        for a, b, c in Board.WINNING_LINES:
            if self._cells[a] == self._cells[b] == self._cells[c] == marker:
                return True
        return False

    def display(self):
        print()
        for row in range(3):
            start = row * 3
            print(f" {self._cells[start]} | {self._cells[start + 1]} | {self._cells[start + 2]} ")
            if row < 2:
                print("-----------")
        print()

    @staticmethod
    def print_position_guide():
        print("Positions:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print()
