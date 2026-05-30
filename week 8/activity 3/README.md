# Week 8 - Activity 3: Single Inheritance (Air New Zealand Domestic Flight System)

A small Python project that demonstrates **single inheritance** using an
Air New Zealand domestic flight scenario.

## Files

| File | Purpose |
|------|---------|
| `flight.py` | Parent class `Flight`. |
| `domestic_flight.py` | Subclass `DomesticFlight` that inherits from `Flight`. |
| `main.py` | Demo / driver code that creates a domestic flight and uses both classes. |
| `Flight Class Diagram.drawio` | UML class diagram (open with [draw.io](https://app.diagrams.net/)). |
| `README.md` | This file. |

## Class Design

### Parent class - `Flight`
Represents a general flight that any airline could operate.

**Attributes**
- `flight_number`
- `airline`
- `origin`
- `destination`
- `departure_time`
- `duration_hours`

**Methods**
- `display_info()` - prints the shared flight details
- `board_passengers()` - generic boarding announcement

### Child class - `DomesticFlight` (inherits from `Flight`)
Represents a domestic flight within New Zealand operated by Air New Zealand.

**Inherited from `Flight`**
All attributes and methods listed above are reused via `super().__init__()`.

**Additional attributes**
- `region` (e.g. "North Island", "South Island")
- `baggage_allowance_kg`

**Additional methods**
- `display_domestic_info()` - calls the parent `display_info()` then prints
  domestic-only details
- `check_baggage(bag_weight_kg)` - validates a bag against the allowance

## How Inheritance Is Shown
1. `DomesticFlight(Flight)` declares the single-inheritance relationship.
2. `super().__init__(...)` reuses the parent constructor instead of
   duplicating attribute assignments.
3. `display_domestic_info()` calls `self.display_info()` - the inherited
   method is used directly by the subclass.
4. The subclass adds new attributes and methods that the parent does not
   have, showing specialisation.

## Run the Demo

```bash
python3 main.py
```

### Expected output
```
Boarding passengers for flight NZ425...
---- Flight Information ----
Airline       : Air New Zealand
Flight Number : NZ425
Route         : Auckland (AKL) -> Wellington (WLG)
Departure     : 08:30
Duration      : 1.25 hour(s)
Region        : North Island
Baggage Limit : 23 kg
Flight Type   : Domestic

Bag 20 kg accepted.
Bag 28 kg is 5 kg overweight - fee applies.
```

## Class Diagram

Open `Flight Class Diagram.drawio` in [draw.io](https://app.diagrams.net/)
(or the VS Code Draw.io Integration extension). The diagram shows:
- `Flight` (parent) with its attributes and methods.
- `DomesticFlight` (child) with its additional attributes and methods.
- An empty-triangle arrow from `DomesticFlight` to `Flight` denoting
  single inheritance.
- A side note listing the members that are inherited from the parent.
