""" Function used for fetching data from api"""

# from dataclasses import dataclass
from typing import TypedDict
import requests
import params

# @dataclass
class FlightInfo(TypedDict):
    """Original each flight data"""
    hex_address: str
    reg_number: str
    flag: str
    latitude: float
    longitude: float
    alt: int
    head_direction: int
    horizontal_speed: int
    vertical_speed: int
    squawk: str
    flight_number: str
    flight_icao: str
    flight_iata: str
    dep_airport_icao: str
    dep_airport_iata: str
    arr_airport_icao: str
    arr_airport_iata: str
    airline_icao: str
    airline_iata: str
    aircraft_icao: str
    updated: int
    status: str



API_PARAMS = params.API_PARAMS


def get_flight_data(api_params=API_PARAMS) -> list[FlightInfo]:
    """Download the real-time data from the api"""
    api_result = requests.get("https://airlabs.co/api/v9/flights", api_params)
    return api_result.json()["response"]
