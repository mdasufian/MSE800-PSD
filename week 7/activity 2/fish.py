"""Fish classes for the Auckland Aquarium."""


class Fish:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def describe(self) -> str:
        return f"{self.name} ({self.species})"


class Goldfish(Fish):
    def __init__(self):
        super().__init__("Goldfish", "Freshwater")


class Shark(Fish):
    def __init__(self):
        super().__init__("Shark", "Saltwater")


class Angelfish(Fish):
    def __init__(self):
        super().__init__("Angelfish", "Freshwater")


class Tuna(Fish):
    def __init__(self):
        super().__init__("Tuna", "Saltwater")


class Salmon(Fish):
    def __init__(self):
        super().__init__("Salmon", "Freshwater/Saltwater")