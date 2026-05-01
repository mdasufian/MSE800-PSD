# Rectangular Land OOP Project

This is a simple object-oriented Python project for calculating the **area** and **perimeter** of a rectangular piece of land.

## What the project includes

- `land.py`
  - Contains the `RectangularLand` class.
  - The class stores the `length` and `width` of the land.
  - It has two methods:
    - `area()` to calculate the area
    - `perimeter()` to calculate the perimeter

- `main.py`
  - Runs the program.
  - Takes user input for length and width.
  - Creates an object of the `RectangularLand` class.
  - Displays the area and perimeter.

## OOP concepts used

- **Class**: `RectangularLand`
- **Object**: Created in `main.py`
- **Methods**: `area()` and `perimeter()`

## How the code works

1. The user enters the length.
2. The user enters the width.
3. The program creates a `RectangularLand` object.
4. The program calculates:
   - Area = length × width
   - Perimeter = 2 × (length + width)
5. The results are printed on the screen.

## Input validation

The program checks that:

- the user enters a valid number
- the number is greater than 0

If the input is invalid, the program asks again.

## How to run

Use this command in the project folder:

```bash
python3 main.py
```

## Example

```text
Rectangular Land Calculator
--------------------------
Enter the length of the land: 10
Enter the width of the land: 5

Results
Area: 50.0 square units
Perimeter: 30.0 units
```

## Summary

This project is a beginner-friendly OOP example. It uses one class and multiple methods across at least two Python files, which matches the classwork requirement.
