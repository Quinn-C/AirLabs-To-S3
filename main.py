""" Download the data with initial cleanup and export to a csv file"""

from fetch_data import get_flight_data
from clean_data import (
    get_flights_in_heathrow,
    clean_flight_data,
)
from file_conversion import to_csv

from s3 import upload_to_s3


def main():
    """From fetching data from api to local csv file with 5 steps below:
    1. Fetching data from api
    2. Only keep flights data in London Heathrow Airport in real-time
    3. Cleaned unuseful data for each flights in Heathrow Airport
    4. Dump the cleaned data into a csv file
    5. Upload the csv file to aws s3
    """
    all_flights_data = get_flight_data()
    flights_in_heathrow = get_flights_in_heathrow(all_flights_data)
    cleaned_flights_data = clean_flight_data(flights_in_heathrow)
    to_csv(cleaned_flights_data)
    upload_to_s3(
        "instance/flight_data.csv", "testingcopy", "jchen/flight_data.csv"
    )


if __name__ == "__main__":
    main()
