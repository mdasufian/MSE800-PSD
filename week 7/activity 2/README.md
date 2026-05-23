# Auckland Aquarium Manager

A simple Python project to manage an aquarium in Auckland, demonstrating the
**Factory** and **Singleton** design patterns.

The aquarium supports the following fish: **Goldfish, Shark, Angelfish, Tuna, Salmon**.
Users can add fish through the console, view the full inventory, and check the
count of any specific fish category.

---

## Design Patterns Used

### 1. Singleton Pattern — `Aquarium`
There is only ever **one** Auckland Aquarium. The `Aquarium` class in
`aquarium.py` overrides `__new__` so that every call to `Aquarium(...)` returns
the same instance. This guarantees the inventory is shared across the
application.

```python
a1 = Aquarium("Auckland")
a2 = Aquarium("Auckland")
assert a1 is a2   # same instance
```

### 2. Factory Pattern — `FishFactory`
Client code should not need to know which concrete `Fish` subclass to
instantiate. `FishFactory.create_fish("shark")` returns the appropriate object,
hiding the construction logic and making it easy to add new fish types later
without changing the calling code.

```python
fish = FishFactory.create_fish("Goldfish")
aquarium.add_fish(fish, quantity=5)
```

---

## Project Structure

```
activity 2/
├── aquarium.py       # Singleton: Auckland Aquarium
├── fish.py           # Fish base class + 5 concrete fish types
├── fish_factory.py   # Factory: creates Fish objects by name
├── main.py           # Console entry point (user input loop)
└── README.md
```

---

## How to Run

Requires **Python 3.8+**. No third-party dependencies.

```bash
cd "week 7/activity 2"
python3 main.py
```

### Example Session

```
Welcome to the Auckland Aquarium!

--- Auckland Aquarium Manager ---
Available fish types: Goldfish, Shark, Angelfish, Tuna, Salmon
1. Add fish to aquarium
2. View aquarium inventory
3. Check count of a specific fish
4. Exit
Choose an option (1-4): 1
Enter fish type: Goldfish
Enter quantity: 10
Added 10 x Goldfish (Freshwater) to the aquarium.

Choose an option (1-4): 1
Enter fish type: Shark
Enter quantity: 2
Added 2 x Shark (Saltwater) to the aquarium.

Choose an option (1-4): 2

=== Auckland Aquarium Inventory ===
  Goldfish   : 10
  Shark      : 2
  TOTAL      : 12
======================================
```

---

## Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add fish — prompts for the category and quantity, then uses the Factory to create the fish and adds it to the (Singleton) aquarium. |
| 2 | View the full inventory grouped by fish category. |
| 3 | Check the count of one specific fish category. |
| 4 | Exit the program. |

---

## Why These Patterns Fit

- **Singleton** matches the real-world constraint that *the* Auckland Aquarium
  is one shared resource — every part of the program must read and write the
  same inventory.
- **Factory** decouples the menu/input layer from the concrete `Fish`
  subclasses. Adding a new species (e.g. *Stingray*) only requires creating a
  new subclass and registering it in `FishFactory._registry` — no other code
  changes.

---

## Author

MSE800 — Professional Software Development, Week 7, Activity 2.