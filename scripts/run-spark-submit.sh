#!/usr/bin/env bash

#set -o errexit   # make your script exit when a command fails
#set -o pipefail  # exit status of the last command that threw a non-zero exit code is returned
#set -o nounset   # exit when your script tries to use undeclared variables

echo "$@"
spark-submit --name "data_project" \
  --master local \
  --files "/opt/spark/conf/log4j.properties" \
  --driver-java-options "-Dlog4j.configuration=file:/opt/spark/conf/log4j.properties" \
  "main.py" "$@"