""" Function used for fetching data from api"""

from dataclasses import dataclass
import requests
import params

@dataclass
class FlightInfo:
    """Original each flight data"""
    hex: str
    reg_number: str
    flag: str
    lat: float
    lng: float
    alt: int
    dir: int
    speed: int
    v_speed: int
    squawk: str
    flight_number: str
    flight_icao: str
    flight_iata: str
    dep_icao: str
    dep_iata: str
    arr_icao: str
    arr_iata: str
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
