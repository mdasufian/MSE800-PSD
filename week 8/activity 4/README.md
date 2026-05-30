# Week 8 - Activity 4: Hybrid Inheritance (Air New Zealand Flight Management System)

A Python project that extends Activity 3 to a **flight management system**
covering both **Domestic** and **International** flights, using
**hybrid inheritance** (hierarchical + multi-level).

## What Hybrid Inheritance Means Here

Hybrid inheritance = a combination of two or more inheritance types in the
same class hierarchy. This project combines:

1. **Hierarchical inheritance** - `DomesticFlight` and `InternationalFlight`
   both inherit from `Flight`.
2. **Multi-level inheritance**
   - `Flight -> DomesticFlight -> RegionalFlight`

```
                       Flight
                      /      \
          DomesticFlight    InternationalFlight     (hierarchical)
                |
          RegionalFlight                            (multi-level)
```

Python MRO for the multi-level chain:
- `RegionalFlight -> DomesticFlight -> Flight -> object`

## Files

| File | Purpose |
|------|---------|
| `flight.py` | Base class `Flight`. |
| `domestic_flight.py` | `DomesticFlight(Flight)` - hierarchical inheritance. |
| `international_flight.py` | `InternationalFlight(Flight)` - hierarchical inheritance. |
| `regional_flight.py` | `RegionalFlight(DomesticFlight)` - multi-level inheritance. |
| `main.py` | Demo / driver code exercising each class. |
| `Flight Class Diagram.drawio` | UML class diagram (open with [draw.io](https://app.diagrams.net/)). |
| `README.md` | This file. |

## Classes and Their Methods (>=3 each)

### `Flight` (base)
- **Attributes**: `flight_number`, `airline`, `origin`, `destination`,
  `departure_time`, `duration_hours`, `status`
- **Methods**:
  1. `display_info()` - print common flight details
  2. `board_passengers()` - generic boarding announcement
  3. `cancel_flight(reason)` - mark the flight cancelled

### `DomesticFlight(Flight)`
- **Adds**: `region`, `baggage_allowance_kg`, `gate`
- **Methods**:
  1. `display_domestic_info()` - calls parent `display_info()` then prints domestic-only fields
  2. `check_baggage(bag_weight_kg)` - validate bag against allowance
  3. `assign_gate(gate_number)` - assign a domestic terminal gate

### `InternationalFlight(Flight)`
- **Adds**: `destination_country`, `visa_required`, `customs_required`
- **Methods**:
  1. `display_international_info()` - calls parent `display_info()` then prints international-only fields
  2. `check_passport(has_passport)` - simple passport check
  3. `declare_customs(items)` - print a customs declaration

### `RegionalFlight(DomesticFlight)` (multi-level)
- **Adds**: `aircraft_type`, `max_takeoff_weight_kg`, `current_load_kg`
- **Methods**:
  1. `display_regional_info()` - reuses `display_domestic_info()` then adds regional fields
  2. `check_weight_balance(added_weight_kg)` - turboprop weight check
  3. `announce_small_airport()` - regional airport reminder

## What Is Inherited / Shared

| Member | Defined in | Available in |
|--------|------------|--------------|
| `flight_number`, `airline`, `origin`, `destination`, `departure_time`, `duration_hours`, `status` | `Flight` | All subclasses |
| `display_info()`, `board_passengers()`, `cancel_flight()` | `Flight` | All subclasses |
| `region`, `baggage_allowance_kg`, `gate`, `assign_gate()`, `check_baggage()`, `display_domestic_info()` | `DomesticFlight` | `DomesticFlight`, `RegionalFlight` |
| `destination_country`, `visa_required`, `customs_required`, `check_passport()`, `declare_customs()`, `display_international_info()` | `InternationalFlight` | `InternationalFlight` |

## Run the Demo

```bash
python3 main.py
```

The demo creates one of each flight type and exercises inherited plus
specialised methods. At the end it prints the MRO for the multi-level
chain so the hybrid structure is explicit.

## Class Diagram

Open `Flight Class Diagram.drawio` in [draw.io](https://app.diagrams.net/)
(or the VS Code Draw.io Integration extension). The diagram shows the four
classes with their attributes and methods, the two hierarchical arrows
from `DomesticFlight` and `InternationalFlight` up to `Flight`, and the
multi-level arrow from `RegionalFlight` up to `DomesticFlight` - the
combination that defines hybrid inheritance.
