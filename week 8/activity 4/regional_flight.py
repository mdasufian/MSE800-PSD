"""
regional_flight.py
Multi-level subclass: RegionalFlight -> DomesticFlight -> Flight.

A regional flight is a short-haul domestic service to smaller regional
airports (e.g. Hamilton, Nelson, Gisborne), usually on a turboprop aircraft
like the ATR 72.
"""

from domestic_flight import DomesticFlight


class RegionalFlight(DomesticFlight):
    """A short-haul regional flight (inherits from DomesticFlight)."""

    def __init__(self, flight_number, origin, destination,
                 departure_time, duration_hours, weight_kg,
                 region, baggage_allowance_kg,
                 aircraft_type, max_takeoff_weight_kg):
        # Reuse the DomesticFlight constructor (which in turn reuses Flight's)
        super().__init__(
            flight_number=flight_number,
            origin=origin,
            destination=destination,
            departure_time=departure_time,
            duration_hours=duration_hours,
            weight_kg=weight_kg,
            region=region,
            baggage_allowance_kg=baggage_allowance_kg,
        )

        # Attributes specific to a regional flight
        self.aircraft_type = aircraft_type                  # e.g. "ATR 72-600"
        self.max_takeoff_weight_kg = max_takeoff_weight_kg  # turboprops are weight-sensitive
        self.current_load_kg = 0                            # running total of loaded weight

    # ---- Method 1 ----------------------------------------------------------
    def display_regional_info(self):
        """Show domestic info, then regional-specific details."""
        # Reuse the inherited DomesticFlight method (which reuses Flight's).
        self.display_domestic_info()
        print(f"Aircraft Type : {self.aircraft_type}")
        print(f"Max Takeoff   : {self.max_takeoff_weight_kg} kg")
        print(f"Current Load  : {self.current_load_kg} kg")
        print("Flight Type   : Regional (Domestic)")

    # ---- Method 2 ----------------------------------------------------------
    def check_weight_balance(self, added_weight_kg):
        """Track loaded weight - regional turboprops are weight-sensitive."""
        self.current_load_kg += added_weight_kg
        if self.current_load_kg > self.max_takeoff_weight_kg:
            over = self.current_load_kg - self.max_takeoff_weight_kg
            print(f"WARNING: {over} kg over max takeoff weight - reduce load.")
        else:
            remaining = self.max_takeoff_weight_kg - self.current_load_kg
            print(f"Load OK. {remaining} kg of capacity remaining.")

    # ---- Method 3 ----------------------------------------------------------
    def announce_small_airport(self):
        """Reminder for passengers arriving at a small regional airport."""
        print(
            f"Reminder: {self.destination} is a regional airport. "
            "Limited facilities; walk-out boarding from the apron."
        )
