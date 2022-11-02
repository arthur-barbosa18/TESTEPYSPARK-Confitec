"""Module to Abstract Process class """

from abc import ABC, abstractmethod
from pyspark.sql.session import SparkSession
from src.tables.table import Table


class Process(ABC):
    """Abstract Process Class
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, spark: SparkSession, table: Table):
        self.spark = spark
        self.table = table

    @abstractmethod
    def process(self):
        """Method to process the step
        """
