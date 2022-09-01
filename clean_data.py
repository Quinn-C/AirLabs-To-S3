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
