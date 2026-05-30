"""
main.py
Driver demo for the Air New Zealand flight management system.

Demonstrates HYBRID inheritance = hierarchical + multi-level:
  - Flight (base)
  - DomesticFlight, InternationalFlight  (hierarchical from Flight)
  - RegionalFlight     (multi-level: Flight -> DomesticFlight -> Regional)
"""

from domestic_flight import DomesticFlight
from international_flight import InternationalFlight
from regional_flight import RegionalFlight


def section(title):
    """Small helper to keep the output readable."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    # -------------------------------------------------------------------
    # 1. DomesticFlight (hierarchical: Flight -> DomesticFlight)
    # -------------------------------------------------------------------
    section("DOMESTIC FLIGHT")
    domestic = DomesticFlight(
        flight_number="NZ425",
        origin="Auckland (AKL)",
        destination="Wellington (WLG)",
        departure_time="08:30",
        duration_hours=1.25,
        weight_kg=42500,                # Airbus A320 typical operating weight
        region="North Island",
        baggage_allowance_kg=23,
    )
    domestic.board_passengers()         # inherited from Flight
    domestic.assign_gate("12B")         # DomesticFlight method
    domestic.display_domestic_info()    # DomesticFlight method
    domestic.check_baggage(28)          # DomesticFlight method

    # -------------------------------------------------------------------
    # 2. InternationalFlight (hierarchical: Flight -> InternationalFlight)
    # -------------------------------------------------------------------
    section("INTERNATIONAL FLIGHT")
    intl = InternationalFlight(
        flight_number="NZ99",
        origin="Auckland (AKL)",
        destination="Los Angeles (LAX)",
        departure_time="19:45",
        duration_hours=12.5,
        weight_kg=181000,               # Boeing 777-300ER operating weight
        destination_country="United States",
        visa_required=True,
    )
    intl.board_passengers()                  # inherited from Flight
    intl.display_international_info()        # InternationalFlight method
    intl.check_passport(has_passport=True)   # InternationalFlight method
    intl.declare_customs(["1L wine", "NZ honey"])

    # -------------------------------------------------------------------
    # 3. RegionalFlight (multi-level under DomesticFlight)
    # -------------------------------------------------------------------
    section("REGIONAL FLIGHT (Multi-level under DomesticFlight)")
    regional = RegionalFlight(
        flight_number="NZ8123",
        origin="Auckland (AKL)",
        destination="Gisborne (GIS)",
        departure_time="07:10",
        duration_hours=1.0,
        weight_kg=13500,                # ATR 72 operating empty weight
        region="North Island",
        baggage_allowance_kg=23,
        aircraft_type="ATR 72-600",
        max_takeoff_weight_kg=22800,
    )
    regional.board_passengers()       # inherited from Flight
    regional.assign_gate("RGN-3")     # inherited from DomesticFlight
    regional.check_baggage(20)        # inherited from DomesticFlight
    regional.check_weight_balance(15000)  # RegionalFlight method
    regional.announce_small_airport()     # RegionalFlight method
    regional.display_regional_info()      # RegionalFlight method

    # -------------------------------------------------------------------
    # 4. Method Resolution Order - shows the multi-level chain
    # -------------------------------------------------------------------
    section("METHOD RESOLUTION ORDER")
    print("RegionalFlight MRO:")
    for cls in RegionalFlight.__mro__:
        print(" -", cls.__name__)


if __name__ == "__main__":
    main()
