"""
flight.py
Parent class for the Air New Zealand domestic flight system.
"""


class Flight:
    """A general flight operated by an airline."""

    def __init__(self, flight_number, airline, origin, destination,
                 departure_time, duration_hours):
        # Shared attributes that every flight has
        self.flight_number = flight_number      # e.g. "NZ123"
        self.airline = airline                  # e.g. "Air New Zealand"
        self.origin = origin                    # departure city
        self.destination = destination          # arrival city
        self.departure_time = departure_time    # e.g. "08:30"
        self.duration_hours = duration_hours    # flight length in hours

    # Shared method - available to both Flight and DomesticFlight
    def display_info(self):
        """Print basic information common to every flight."""
        print("---- Flight Information ----")
        print(f"Airline       : {self.airline}")
        print(f"Flight Number : {self.flight_number}")
        print(f"Route         : {self.origin} -> {self.destination}")
        print(f"Departure     : {self.departure_time}")
        print(f"Duration      : {self.duration_hours} hour(s)")

    # Shared method - reused by the subclass through inheritance
    def board_passengers(self):
        """Generic boarding announcement."""
        print(f"Boarding passengers for flight {self.flight_number}...")
