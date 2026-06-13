"""Game orchestration for the Tic-tac-toe game."""

from board import Board
from player import Player


class Game:
    """Orchestrates a single round of Tic-tac-toe between two players."""

    def __init__(self, players=None):
        self.board = Board()
        self.players = players or (Player("X"), Player("O"))
        self._turn = 0

    @property
    def current_player(self):
        return self.players[self._turn % len(self.players)]

    def _advance_turn(self):
        self._turn += 1

    def play(self):
        print("Welcome to Tic-tac-toe!")
        Board.print_position_guide()

        while True:
            self.board.display()
            player = self.current_player
            index = player.choose_move(self.board)
            self.board.place(index, player.marker)

            if self.board.has_winner(player.marker):
                self.board.display()
                print(f"Player {player.marker} wins!")
                return

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                return

            self._advance_turn()
