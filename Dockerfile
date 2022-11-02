FROM ubuntu:22.04

ENV SPARK_HOME="/opt/spark"
ENV SPARK_VERSION="3.3.1"
ENV SPARK_HADOOP_VERSION="3"
ENV PATH="${SPARK_HOME}/bin:${PATH}"

ENV PYSPARK_PYTHON=python3.7
ENV PATH="$SPARK_HOME/python:$PATH"

ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH

WORKDIR /opt

# Setting Ubuntu default timezone
RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

# Utilities
RUN apt-get update \
    && apt-get -y install zip curl

# Java 11
RUN apt-get -y install openjdk-11-jdk

# Python 3.7
RUN apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.7-distutils \
    && apt-get install -y python3.7 \
    && apt install -y python3-pip \
    && ln -sf /usr/bin/python3.7 /usr/bin/python3

RUN pip3 --version
RUN pip --version

ADD requirements.txt .
ADD requirements-dev.txt .
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

# Spark
ADD "https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}.tgz" .
RUN tar -xvf spark*.tgz && rm -f spark*.tgz && mv spark* spark

RUN touch /opt/spark/conf/log4j.properties
RUN echo 'log4j.rootLogger=INFO, console\n\
\n\
# Console Appender\n\
log4j.appender.console=org.apache.log4j.ConsoleAppender\n\
log4j.appender.console.layout=org.apache.log4j.PatternLayout\n\
log4j.appender.console.layout.ConversionPattern=\u001b[m%d{yyyy/MM/dd HH:mm:ss} \u001b[36;1m%p\u001b[m [\u001b[32;1m%t\u001b[m] \u001b[34;1m%c{1}\u001b[m: %m%n\n\
\n\
# Logging Level\n\
log4j.logger.org.apache=ERROR\n\
log4j.logger.org.spark_project=ERROR\n\
log4j.logger.parquet=ERROR\n' >> /opt/spark/conf/log4j.properties

WORKDIR /opt/app/
CMD tail -f /dev/null
