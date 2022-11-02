""" Main Module """

from pyspark.sql import SparkSession
from src.repo import log
from src.repo.constants import NETFLIX
from src.repo.arguments import arguments
from src.usecases.netflix.handle_sanitizer import sanitizer_usecase_netflix

def main():
    """ Main Function """
    spark = SparkSession.builder.appName("test-confitec").getOrCreate()
    args = arguments()
    log.info(args)
    
    if args["pipeline"] == NETFLIX:
        sanitizer_usecase_netflix(spark)

if __name__ == "__main__":
    main()
