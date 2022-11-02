""" Usecase to Trusted Pipeline Netflix Module """

from pyspark.sql.session import SparkSession
from src.tables.netflix_table import NetflixTable
from src.repo import log
from src.repo.commons import upload_directory
from src.rules.netflix.sanitizer import Sanitizer


def sanitizer_usecase_netflix(spark: SparkSession):
    """Function to usecase of sanitizer netflix originals dataset

    Args:
        spark (SparkSession): the spark session
    """
    log.info("Start usecase to sanitizer netflix originals data")
    netflix_table = NetflixTable(spark)
    netflix_table.load(netflix_table.raw_path)
    sanitizer = Sanitizer(spark, netflix_table)
    sanitizer.process()
    if netflix_table.dataframe:
        netflix_table.save_dataframe_csv(netflix_table.trusted_path)
        upload_directory(netflix_table.trusted_path,
                         netflix_table.bucket_s3_name)
