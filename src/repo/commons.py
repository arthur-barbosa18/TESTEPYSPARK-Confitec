""" Commons module """

import os
import boto3


def upload_directory(path: str, bucketname: str):
    """Upload directory, is necessary to save dataframe csv in aws bucket

    Args:
        path (str): path to local directory
        bucketname (str): aws bucket name
    """
    _s3 = boto3.resource("s3")
    for root, _, files in os.walk(path):
        for file in files:
            _s3.meta.client.upload_file(os.path.join(
                root, file), bucketname, f"TRUSTED/{file}")
