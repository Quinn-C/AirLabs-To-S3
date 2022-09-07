""" Function used for fetching data from api"""

from typing import Generator
import requests
import params
from structures.data_classes import FlightInfo


API_PARAMS = params.API_PARAMS


def get_flight_data(api_params=API_PARAMS) -> Generator[FlightInfo, None, None]:
    """Download the real-time data from the api"""
    api_result = requests.get("https://airlabs.co/api/v9/flights", api_params)
    all_flights = api_result.json()["response"]
    all_flights_data= (FlightInfo(**flight) for flight in all_flights)
    return all_flights_data
