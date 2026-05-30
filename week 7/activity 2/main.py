"""Auckland Aquarium Manager - entry point.

Demonstrates the Factory and Singleton design patterns:
  - FishFactory  : Factory pattern for creating Fish objects.
  - Aquarium     : Singleton pattern for the single Auckland aquarium.
"""

from aquarium import Aquarium
from fish_factory import FishFactory


def show_menu() -> None:
    print("\n--- Auckland Aquarium Manager ---")
    print("Available fish types: " + ", ".join(FishFactory.available_types()))
    print("1. Add fish to aquarium")
    print("2. View aquarium inventory")
    print("3. Check count of a specific fish")
    print("4. Exit")


def add_fish_flow(aquarium: Aquarium) -> None:
    fish_type = input("Enter fish type: ").strip()
    qty_input = input("Enter quantity: ").strip()
    try:
        quantity = int(qty_input)
        fish = FishFactory.create_fish(fish_type)
        aquarium.add_fish(fish, quantity)
        print(f"Added {quantity} x {fish.describe()} to the aquarium.")
    except ValueError as e:
        print(f"Error: {e}")


def check_count_flow(aquarium: Aquarium) -> None:
    fish_type = input("Enter fish type to check: ").strip().capitalize()
    count = aquarium.get_count(fish_type)
    print(f"{fish_type}: {count} fish currently in the aquarium.")


def main() -> None:
    aquarium = Aquarium("Auckland")
    print(f"Welcome to the {aquarium.location} Aquarium!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_fish_flow(aquarium)
        elif choice == "2":
            aquarium.display()
        elif choice == "3":
            check_count_flow(aquarium)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
