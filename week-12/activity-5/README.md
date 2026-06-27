# BMI Calculator — Flask Web App

A simple BMI (Body Mass Index) calculator built with Flask using object-oriented programming.

## Formula

```
BMI = weight (kg) / height (m)²
```

## BMI Categories

| BMI Range     | Category      |
|---------------|---------------|
| Below 18.5    | Underweight   |
| 18.5 – 24.9   | Normal weight |
| 25 – 29.9     | Overweight    |
| 30 and above  | Obese         |

## Project Structure

```
activity-5/
├── app.py                # Main Flask application class (BMIApp)
├── bmi_calculator.py     # BMI calculation class (BMICalculator)
├── static/
│   └── style.css         # Stylesheet
└── templates/
    ├── index.html        # Input form
    └── result.html       # Result page
```

## Requirements

- Python 3.x
- Flask

## Installation

```bash
pip install flask
```

## How to Run

```bash
python app.py
```

Then open your browser at: `http://127.0.0.1:5000/`

## Usage

1. Enter your weight in kilograms.
2. Enter your height in meters.
3. Click **Calculate BMI** to see your result and category.

## OOP Design

- **`BMICalculator`** — handles BMI computation and classification logic.
- **`BMIApp`** — main application class that wires Flask routes to the calculator.
