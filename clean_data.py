"""Functions used for cleaning data"""

from typing import Generator
from structures.data_classes import FlightInfo, CleanedFlightInfo

def rm_unuseful_cols(flight: FlightInfo) -> CleanedFlightInfo:
    """ Remove unuseful fields and renaming them to be more understandable"""
    cleaned_flight_info = CleanedFlightInfo(
        latitude = flight.lat,
        longitude = flight.lng,
        airline_country = flight.flag,
        dep_airport = flight.dep_icao,
        arr_airport = flight.arr_icao
    )
    return cleaned_flight_info


def clean_flight_data(
    all_flights_data: Generator[FlightInfo, None, None],
) -> list[CleanedFlightInfo]:
    """ Filter out unuseful columns"""
    cleaned_flights = [rm_unuseful_cols(flight) for flight in all_flights_data]
    return cleaned_flights
