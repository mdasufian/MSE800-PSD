"""Factory Design Pattern: creates Fish objects based on the requested type."""

from fish import Fish, Goldfish, Shark, Angelfish, Tuna, Salmon


class FishFactory:
    _registry = {
        "goldfish": Goldfish,
        "shark": Shark,
        "angelfish": Angelfish,
        "tuna": Tuna,
        "salmon": Salmon,
    }

    @classmethod
    def create_fish(cls, fish_type: str) -> Fish:
        key = fish_type.strip().lower()
        if key not in cls._registry:
            raise ValueError(
                f"Unknown fish type '{fish_type}'. "
                f"Available: {', '.join(t.capitalize() for t in cls._registry)}"
            )
        return cls._registry[key]()

    @classmethod
    def available_types(cls):
        return [t.capitalize() for t in cls._registry]