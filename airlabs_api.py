""" Download the data with initial cleanup and export to a csv file"""

import csv
import requests
import params

API_PARAMS = params.API_PARAMS

HEATHROW_LEFT_TOP = {"lat": 51.5, "lng": -0.5}

HEATHROW_RIGHT_BTM = {"lat": 51.4, "lng": -0.4}


def get_flight_data(api_params=API_PARAMS):
    """Download the real-time data from the api"""
    api_result = requests.get("https://airlabs.co/api/v9/flights", api_params)
    return api_result.json()["response"]


def is_in_heathrow(flight_lat: float, flight_lng: float) -> bool:
    """Helper function: Check if the flight is inside the Heathrow airport"""
    if HEATHROW_RIGHT_BTM["lat"] < flight_lat < HEATHROW_LEFT_TOP["lat"]:
        if HEATHROW_LEFT_TOP["lng"] < flight_lng < HEATHROW_RIGHT_BTM["lng"]:
            return True
    return False


def remove_unuseful_columns(flight: dict) -> dict:
    """Helper function: Filter out unuseful columns from the each flight"""
    new_dict = {}
    for key, value in flight.items():
        if key in ("lat", "lng"):
            new_dict[key] = value
    return new_dict


def get_flights_in_heathrow(flight_data):
    """Get list of flights in London Heathrow airport"""
    heathrow_flight_data = [
        flight for flight in flight_data if is_in_heathrow(flight["lat"], flight["lng"])
    ]
    return heathrow_flight_data


def clean_flight_data(heathrow_data):
    """Filter out unuseful columns"""
    cleaned_flights = [remove_unuseful_columns(flight) for flight in heathrow_data]
    return cleaned_flights


def to_csv(cleaned_data):
    """Transform data from python list to csv file directly"""
    with open("instance/flight_data.csv", "w", encoding="UTF-8") as csv_file:
        csv_columns = ["lat", "lng"]
        writer = csv.DictWriter(csv_file, csv_columns, restval="Null")
        writer.writeheader()
        for row in cleaned_data:
            writer.writerow(row)

def main():
    """ Run all functions in a specific order """
    all_flights_data = get_flight_data()
    flights_in_heathrow = get_flights_in_heathrow(all_flights_data)
    cleaned_flights_data = clean_flight_data(flights_in_heathrow)
    to_csv(cleaned_flights_data)


if __name__ == "__main__":
    main()
