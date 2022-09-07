""" Functions to dump data into csv files"""

from dataclass_csv import DataclassWriter
from clean_data import CleanedFlightInfo

def to_csv(cleaned_data: list[CleanedFlightInfo]) -> None:
    """Transform data from python dataclass to csv file directly"""
    with open("instance/flight_data.csv", "w", encoding="UTF-8") as csv_file:
        writer = DataclassWriter(csv_file, cleaned_data, CleanedFlightInfo)
        writer.write()
