"""
international_flight.py
Subclass for international flights (single / hierarchical inheritance from Flight).
"""

from flight import Flight


class InternationalFlight(Flight):
    """An international flight (inherits from Flight)."""

    def __init__(self, flight_number, origin, destination,
                 departure_time, duration_hours, weight_kg,
                 destination_country, visa_required,
                 customs_required=True):
        super().__init__(
            flight_number=flight_number,
            airline="Air New Zealand",
            origin=origin,
            destination=destination,
            departure_time=departure_time,
            duration_hours=duration_hours,
            weight_kg=weight_kg,
        )

        # Attributes specific to an international flight
        self.destination_country = destination_country   # e.g. "Australia"
        self.visa_required = visa_required               # True / False
        self.customs_required = customs_required         # almost always True

    # ---- Method 1 ----------------------------------------------------------
    def display_international_info(self):
        """Show shared info first, then international-only details."""
        self.display_info()
        print(f"Destination   : {self.destination_country}")
        print(f"Visa Required : {'Yes' if self.visa_required else 'No'}")
        print(f"Customs       : {'Yes' if self.customs_required else 'No'}")
        print("Flight Type   : International")

    # ---- Method 2 ----------------------------------------------------------
    def check_passport(self, has_passport):
        """Verify a passenger has a valid passport before boarding."""
        if has_passport:
            print("Passport verified. Passenger may proceed.")
        else:
            print("Boarding denied: passport required for international travel.")

    # ---- Method 3 ----------------------------------------------------------
    def declare_customs(self, items):
        """Print a simple customs declaration for the given items."""
        if not self.customs_required:
            print("No customs declaration required.")
            return
        print("Customs declaration:")
        for item in items:
            print(f"  - {item}")
