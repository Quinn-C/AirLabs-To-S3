"""Functions used for cleaning data"""

from typing import Generator
from dataclasses import dataclass
from fetch_data import FlightInfo


@dataclass
class CleanedFlightsInHeathrow:
    """Type annotation for flights info in Heathrow airport"""

    lat: float
    lng: float
    airline_country: str
    dep_airport: str
    arr_airport: str


HEATHROW_LEFT_TOP = {"lat": 51.5, "lng": -0.5}

HEATHROW_RIGHT_BTM = {"lat": 51.4, "lng": -0.4}


def is_in_heathrow(flight_lat: float, flight_lng: float) -> bool:
    """Helper function: Check if the flight is inside the Heathrow airport"""
    if HEATHROW_RIGHT_BTM["lat"] < flight_lat < HEATHROW_LEFT_TOP["lat"]:
        if HEATHROW_LEFT_TOP["lng"] < flight_lng < HEATHROW_RIGHT_BTM["lng"]:
            return True
    return False


def rm_unuseful_col(flight: FlightInfo) -> CleanedFlightsInHeathrow:
    """Helper function: Filter out unuseful columns from the each flight"""
    new_dict = {}
    """ Does not work has incompatible issues
    for key in flight.__dataclass_fields__:
        if key in ("lat"):
            new_dict["lat"] = flight.lat
        elif key in ("lng"):
            new_dict["lng"] = flight.lng
        elif key in ("flag"):
            new_dict["airline_country"] = flight.flag
        elif key in ("dep_icao"):
            new_dict["dep_airport"] = flight.dep_icao
        elif key in ("arr_icao"):
            new_dict["arr_airport"] = flight.arr_icao
    return new_dict
    """
    for key, value in flight.items():
        if key in ("lat", "lng"):
            new_dict[key] = value
        elif key in ("flag"):
            new_dict["airline_country"] = value
        elif key in ("dep_icao"):
            new_dict["dep_airport"] = value
        elif key in ("arr_icao"):
            new_dict["arr_airport"] = value
    return new_dict


def get_flights_in_heathrow(
    flight_data: list[FlightInfo],
) -> Generator[FlightInfo, None, None]:
    """Store flights in London Heathrow airport in a generator"""
    heathrow_flight_data = (
        fl for fl in flight_data if is_in_heathrow(fl["lat"], fl["lng"])
    )
    # use flight.lat and flight.lng can avoid the mypy error,
    # but the code does not work
    return heathrow_flight_data


def clean_flight_data(
    heathrow_data: list[FlightInfo],
) -> Generator[CleanedFlightsInHeathrow, None, None]:
    """Filter out unuseful columns"""
    cleaned_flights = (rm_unuseful_col(flight) for flight in heathrow_data)
    return cleaned_flights
