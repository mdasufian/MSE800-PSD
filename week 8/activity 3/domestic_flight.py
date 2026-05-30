"""
domestic_flight.py
Subclass that inherits from Flight (single inheritance).
"""

from flight import Flight   # import the parent class from its own file


class DomesticFlight(Flight):
    """A domestic flight within New Zealand (inherits from Flight)."""

    def __init__(self, flight_number, origin, destination,
                 departure_time, duration_hours,
                 region, baggage_allowance_kg):
        # Call the parent constructor to reuse shared initialisation.
        # Airline is fixed to "Air New Zealand" for this domestic system.
        super().__init__(
            flight_number=flight_number,
            airline="Air New Zealand",
            origin=origin,
            destination=destination,
            departure_time=departure_time,
            duration_hours=duration_hours,
        )

        # Extra attributes that only apply to domestic flights
        self.region = region                              # "North Island" / "South Island"
        self.baggage_allowance_kg = baggage_allowance_kg  # checked-bag limit

    # New method specific to the subclass
    def display_domestic_info(self):
        """Show shared info first, then domestic-only details."""
        # Reuse the parent method - this is the inheritance benefit
        self.display_info()
        print(f"Region        : {self.region}")
        print(f"Baggage Limit : {self.baggage_allowance_kg} kg")
        print("Flight Type   : Domestic")

    # New method specific to the subclass
    def check_baggage(self, bag_weight_kg):
        """Check whether a bag is within the domestic allowance."""
        if bag_weight_kg <= self.baggage_allowance_kg:
            print(f"Bag {bag_weight_kg} kg accepted.")
        else:
            extra = bag_weight_kg - self.baggage_allowance_kg
            print(f"Bag {bag_weight_kg} kg is {extra} kg overweight - fee applies.")
