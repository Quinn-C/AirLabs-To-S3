""" All dataclasses needed for this project"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class FlightInfo:
    """Original each flight data"""
    hex: Optional[str] = None
    reg_number: Optional[str] = None
    flag: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    alt: Optional[int] = None
    dir: Optional[int] = None
    speed: Optional[int] = None
    v_speed: Optional[int] = None
    squawk: Optional[str] = None
    flight_number: Optional[str] = None
    flight_icao: Optional[str] = None
    flight_iata: Optional[str] = None
    dep_icao: Optional[str] = None
    dep_iata: Optional[str] = None
    arr_icao: Optional[str] = None
    arr_iata: Optional[str] = None
    airline_icao: Optional[str] = None
    airline_iata: Optional[str] = None
    aircraft_icao: Optional[str] = None
    updated: Optional[int] = None
    status: Optional[str] = None

@dataclass
class CleanedFlightInfo:
    """Cleaned each flight data"""
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    airline_country: Optional[str] = None
    dep_airport: Optional[str] = None
    arr_airport: Optional[str] = None
