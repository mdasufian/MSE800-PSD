class BMICalculator:
    """Encapsulates BMI calculation and classification logic."""

    def __init__(self, weight_kg: float, height_m: float):
        # Store the user's weight (kg) and height (m)
        self.weight_kg = weight_kg
        self.height_m = height_m

    def calculate(self) -> float:
        # BMI = weight (kg) / height (m) squared
        return self.weight_kg / (self.height_m ** 2)

    def classify(self) -> str:
        # Standard WHO BMI categories
        bmi = self.calculate()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
