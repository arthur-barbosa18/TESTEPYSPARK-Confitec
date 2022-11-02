""" Module to FmbApp Table"""


from pyspark.sql.session import SparkSession
from src.tables.table import Table
from src.repo.constants import BASE_PATH


class NetflixTable(Table):
    """ FmbApp Table """

    def __init__(self, spark: SparkSession):
        self.raw_path = f"{BASE_PATH}/DATALAKE/RAW"
        self.trusted_path = f"{BASE_PATH}/DATALAKE/TRUSTED"
        self.bucket_s3_name = "netflix-confitec"
        self.trusted_path_s3 = "TRUSTED/netflix_originals.csv"
        super().__init__(spark)
