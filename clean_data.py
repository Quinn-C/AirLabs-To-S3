"""Functions used for cleaning data"""

from typing import Generator, TypedDict
#from dataclasses import dataclass
from fetch_data import FlightInfo

# @dataclass
class CleanedFlights(TypedDict):
    """Type annotation for flights info in Heathrow airport"""

    lat: float
    lng: float
    airline_country: str
    dep_airport: str
    arr_airport: str

NORTH_AMER_LEFT_TOP = {"latitude": 71.3, "longitude": -167.3}

NORTH_AMER_RIGHT_BTM = {"latitude": 7.2, "longitude": -77.8}


def is_in_north_amer(flight_lat: float, flight_lng: float) -> bool:
    """Helper function: Check if the flight is inside the Heathrow airport"""
    if NORTH_AMER_RIGHT_BTM["latitude"] < flight_lat < NORTH_AMER_LEFT_TOP["latitude"]:
        if NORTH_AMER_LEFT_TOP["longitude"] < flight_lng < NORTH_AMER_RIGHT_BTM["longitude"]:
            return True
    return False


def get_flights_in_north_amer(
    flight_data: list[FlightInfo],
) -> Generator[FlightInfo, None, None]:
    """Store real-time flights in north america in a generator"""
    north_amer_flight_data = (
        fl for fl in flight_data if is_in_north_amer(fl["lat"], fl["lng"])
    )
    # use flight.lat and flight.lng can avoid the mypy error,
    # but the code does not work
    return north_amer_flight_data

def rm_unuseful_cols(flight: FlightInfo):
    """ Helper funciton: filter out unuseful columns from each flight"""
    new_flight = {
        "latitude": None,
        "longitude": None,
        "airline_country": None,
        "dep_airport": None,
        "arr_airport": None
    }
    # Due to the quality of the api, always missing columns, this is the only way
    # that I found to avoid keyerrors
    for key, value in flight.items():
        if key == "lat":
            new_flight["latitude"] = value
        elif key == "lng":
            new_flight["longitude"] = value
        elif key == "flag":
            new_flight["airline_country"] = value
        elif key == "dep_icao":
            new_flight["dep_airport"] = value
        elif key == "arr_icao":
            new_flight["arr_airport"] = value
    return new_flight

def clean_flight_data(
    north_amer_data: list[FlightInfo],
) -> Generator[CleanedFlights, None, None]:
    """ Filter out unuseful columns"""
    cleaned_flights = (rm_unuseful_cols(flight) for flight in north_amer_data)
    return cleaned_flights
