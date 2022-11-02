""" Apply conf to log4j """
import inspect
from pyspark.context import SparkContext


def __caller_name():
    """ get the name of who called this function """
    events = inspect.stack()
    if len(events) < 3:
        return __name__
    return inspect.getmodule(events[3][0]).__name__


def __logger():
    """ get logger (log4j) instance """
    spark_context = SparkContext.getOrCreate()
    log4j = spark_context._jvm.org.apache.log4j
    return log4j.LogManager.getLogger(__caller_name())


def info(msg):
    """ info log """
    __logger().info(msg)


def error(msg):
    """ error log """
    __logger().error(msg)


def warning(msg):
    """
    Args:
        msg (str): warning logged message
    """
    __logger().warn(msg)
