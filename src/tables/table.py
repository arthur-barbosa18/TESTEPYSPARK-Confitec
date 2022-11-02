""" Table Module """
from pyspark.sql.session import SparkSession
from src.repo import log


class Table():
    """Table is responsible to load dataset and create
    dataset object
    """

    def __init__(self, spark: SparkSession):
        self.spark = spark
        self.schema = None
        self.dataframe = None

    def load(self, path: str):
        """Load dataframe from raw path

        Args:
            path (str): path to load dataframe
        """
        log.info(f"Load dataframe at {path}")
        self.dataframe = self.spark.read.parquet(path)

    def save_dataframe_csv(self, path: str,
                           mode: str = "overwrite", delimiter: str = ";"):
        """Save dataframe in csv format

        Args:
            path (str): path where will be save csv
            mode (str, optional): Defaults to "overwrite".
            delimiter (str, optional): csv character delimiter.
            Defaults to ";".
        """
        log.info(f"Write dataframe in {path}")
        self.dataframe.coalesce(1).write.mode(
            mode).csv(path, header=True, sep=delimiter)
