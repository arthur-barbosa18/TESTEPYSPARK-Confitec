import pytest
from pyspark.sql.session import SparkSession


@pytest.fixture
def create_spark_session():
    spark = SparkSession.builder.appName("confitec-test").getOrCreate()
    return spark

@pytest.fixture
def close_spark_session():
    def close(spark):
        spark.stop()
    return close