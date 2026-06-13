"""Entry point for the two-player command-line Tic-tac-toe game.

Run this module directly to play:

    python main.py
"""

from game import Game


def main():
    """Run games until the players choose to stop."""
    while True:
        Game().play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
