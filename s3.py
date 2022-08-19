""" Uploading a file to S3"""

import os
import logging
import boto3
from botocore.exceptions import ClientError


def upload_to_s3(file_name, bucket_name, object_name = None):
    """ Upload a file to an S3 bucket """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as error:
        logging.error(error)
        return False
    return True


if __name__ == "__main__":
    upload_to_s3("instance/flight_data.csv", "testingcopy", None)
