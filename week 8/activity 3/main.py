"""
main.py
Demo / driver code that uses the Flight and DomesticFlight classes.
"""

from domestic_flight import DomesticFlight   # subclass (parent comes with it)


def main():
    # Create a domestic Air New Zealand flight from Auckland to Wellington
    nz_flight = DomesticFlight(
        flight_number="NZ425",
        origin="Auckland (AKL)",
        destination="Wellington (WLG)",
        departure_time="08:30",
        duration_hours=1.25,
        region="North Island",
        baggage_allowance_kg=23,
    )

    # Inherited method from Flight
    nz_flight.board_passengers()

    # New method defined on the subclass (which also reuses display_info)
    nz_flight.display_domestic_info()

    # Subclass-specific behaviour
    print()
    nz_flight.check_baggage(20)   # within limit
    nz_flight.check_baggage(28)   # overweight


if __name__ == "__main__":
    main()
