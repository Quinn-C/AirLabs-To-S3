""" All dataclasses needed for this project"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class FlightInfo:
    """Original each flight data"""
    hex: Optional[str] = None
    reg_number: Optional[str] = None
    flag: str = " "
    lat: float = 0.0
    lng: float = 0.0
    alt: Optional[int] = None
    dir: Optional[int] = None
    speed: Optional[int] = None
    v_speed: Optional[int] = None
    squawk: Optional[str] = None
    flight_number: Optional[str] = None
    flight_icao: Optional[str] = None
    flight_iata: Optional[str] = None
    dep_icao: str = " "
    dep_iata: Optional[str] = None
    arr_icao: str = " "
    arr_iata: Optional[str] = None
    airline_icao: Optional[str] = None
    airline_iata: Optional[str] = None
    aircraft_icao: Optional[str] = None
    updated: Optional[int] = None
    status: Optional[str] = None

@dataclass
class CleanedFlightInfo:
    """Cleaned each flight data"""
    latitude: float = 0.0
    longitude: float = 0.0
    airline_country: str = " "
    dep_airport: str = " "
    arr_airport: str = " "
