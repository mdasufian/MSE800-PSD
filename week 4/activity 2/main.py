from land import RectangularLand


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Rectangular Land Calculator")
    print("--------------------------")

    length = get_positive_number("Enter the length of the land: ")
    width = get_positive_number("Enter the width of the land: ")

    land = RectangularLand(length, width)

    print("\nResults")
    print(f"Area: {land.area()} square units")
    print(f"Perimeter: {land.perimeter()} units")


if __name__ == "__main__":
    main()
