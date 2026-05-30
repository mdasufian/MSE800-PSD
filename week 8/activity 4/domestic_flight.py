"""
domestic_flight.py
Subclass for domestic flights (single / hierarchical inheritance from Flight).
"""

from flight import Flight


class DomesticFlight(Flight):
    """A domestic flight within New Zealand (inherits from Flight)."""

    def __init__(self, flight_number, origin, destination,
                 departure_time, duration_hours, weight_kg,
                 region, baggage_allowance_kg):
        # Reuse the parent constructor; airline is fixed for domestic ops.
        super().__init__(
            flight_number=flight_number,
            airline="Air New Zealand",
            origin=origin,
            destination=destination,
            departure_time=departure_time,
            duration_hours=duration_hours,
            weight_kg=weight_kg,
        )

        # Attributes specific to a domestic flight
        self.region = region                              # "North Island" / "South Island"
        self.baggage_allowance_kg = baggage_allowance_kg  # checked-bag limit
        self.gate = None                                  # assigned later

    # ---- Method 1 ----------------------------------------------------------
    def display_domestic_info(self):
        """Show shared info first, then domestic-only details."""
        # Reuse the inherited parent method
        self.display_info()
        print(f"Region        : {self.region}")
        print(f"Baggage Limit : {self.baggage_allowance_kg} kg")
        print(f"Gate          : {self.gate if self.gate else 'TBA'}")
        print("Flight Type   : Domestic")

    # ---- Method 2 ----------------------------------------------------------
    def check_baggage(self, bag_weight_kg):
        """Check whether a bag is within the domestic allowance."""
        if bag_weight_kg <= self.baggage_allowance_kg:
            print(f"Bag {bag_weight_kg} kg accepted.")
        else:
            extra = bag_weight_kg - self.baggage_allowance_kg
            print(f"Bag {bag_weight_kg} kg is {extra} kg overweight - fee applies.")

    # ---- Method 3 ----------------------------------------------------------
    def assign_gate(self, gate_number):
        """Assign a domestic-terminal gate to this flight."""
        self.gate = gate_number
        print(f"Flight {self.flight_number} assigned to gate {gate_number}.")
