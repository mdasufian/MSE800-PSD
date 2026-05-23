"""Singleton Design Pattern: ensures only one Auckland Aquarium instance exists."""

from collections import defaultdict
from fish import Fish


class Aquarium:
    _instance = None

    def __new__(cls, location: str = "Auckland"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, location: str = "Auckland"):
        if self._initialized:
            return
        self.location = location
        self._fish_counts = defaultdict(int)
        self._initialized = True

    def add_fish(self, fish: Fish, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self._fish_counts[fish.name] += quantity

    def get_count(self, fish_name: str) -> int:
        return self._fish_counts.get(fish_name, 0)

    def inventory(self) -> dict:
        return dict(self._fish_counts)

    def total_fish(self) -> int:
        return sum(self._fish_counts.values())

    def display(self) -> None:
        print(f"\n=== {self.location} Aquarium Inventory ===")
        if not self._fish_counts:
            print("No fish in the aquarium yet.")
            return
        for name, count in sorted(self._fish_counts.items()):
            print(f"  {name:<10} : {count}")
        print(f"  {'TOTAL':<10} : {self.total_fish()}")
        print("=" * 38)