"""
flight.py
Base class for the Air New Zealand flight management system.

Part of a HYBRID inheritance design:
    Flight                          (base)
      |
      |-- DomesticFlight            (hierarchical, level 1)
      |     |
      |     `-- RegionalFlight      (multi-level, level 2)
      |
      `-- InternationalFlight       (hierarchical, level 1)
            |
            `-- LongHaulFlight      (multi-level, level 2)

Hybrid = hierarchical inheritance + multi-level inheritance.
"""


class Flight:
    """A general flight operated by an airline."""

    def __init__(self, flight_number, airline, origin, destination,
                 departure_time, duration_hours, weight_kg):
        # Attributes shared by EVERY flight in the system
        self.flight_number = flight_number      # e.g. "NZ425"
        self.airline = airline                  # e.g. "Air New Zealand"
        self.origin = origin                    # departure city
        self.destination = destination          # arrival city
        self.departure_time = departure_time    # e.g. "08:30"
        self.duration_hours = duration_hours    # flight length in hours
        self.weight_kg = weight_kg              # aircraft weight in kilograms
        self.status = "Scheduled"               # default lifecycle state

    # ---- Method 1 ----------------------------------------------------------
    def display_info(self):
        """Print the basic information common to every flight."""
        print("---- Flight Information ----")
        print(f"Airline       : {self.airline}")
        print(f"Flight Number : {self.flight_number}")
        print(f"Route         : {self.origin} -> {self.destination}")
        print(f"Departure     : {self.departure_time}")
        print(f"Duration      : {self.duration_hours} hour(s)")
        print(f"Weight        : {self.weight_kg} kg")
        print(f"Status        : {self.status}")

    # ---- Method 2 ----------------------------------------------------------
    def board_passengers(self):
        """Generic boarding announcement."""
        print(f"Boarding passengers for flight {self.flight_number}...")
        self.status = "Boarding"

    # ---- Method 3 ----------------------------------------------------------
    def cancel_flight(self, reason):
        """Mark the flight as cancelled with a reason."""
        self.status = "Cancelled"
        print(f"Flight {self.flight_number} cancelled. Reason: {reason}")
