"""Airlabs API to S3 transfer"""
from datetime import date
from fetch_data import get_flight_data
from clean_data import (
    clean_flight_data
)

from file_conversion import to_csv

from s3 import upload_to_s3


def main():
    """From fetching data from api to local csv file with 4 steps below:
    1. Fetch data from api - get all global flights data in a list of JSON
    2. Remove unuseful fields for each flight in the list
    3. Dump the cleaned data into a csv file
    4. Upload the csv file to aws s3 testingcopy bucket
    """
    all_flights_data = get_flight_data()
    cleaned_flights_data = clean_flight_data(all_flights_data)
    to_csv(cleaned_flights_data)
    upload_to_s3(
        "instance/flight_data.csv", "testingcopy",
        f"jchen/dt={str(date.today())}/flight_data.csv"
    )


if __name__ == "__main__":
    main()
