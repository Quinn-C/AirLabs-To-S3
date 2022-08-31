""" Uploading a file to S3"""

import logging
import boto3
from botocore.exceptions import ClientError


def upload_to_s3(file_name: str, bucket_name: str, object_name: str) -> None:
    """Upload a file to an S3 bucket"""
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as error:
        logging.error(error)
