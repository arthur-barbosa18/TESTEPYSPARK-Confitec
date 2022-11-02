# TESTEPYSPARK-CONFITEC

## Introduction

This project exists to manager tables and their respective use cases and business rules.

### Requirements:
All source files are in python and bash.

- Python 3.7
- Docker
- Docker Compose

## Running the application locally

Build the images by docker-compose:

```sh
$ docker-compose build
```

Up containers:

```sh
$ docker-compose up -d
```

Run the application to trigger sanitization pipeline:

```sh
$ docker-compose exec app ./scripts/run_spark_submit.sh --pipeline netflix
```

Then, run the image to verify code health and test the application:

```sh
$ docker-compose exec app tox
```

And to run application:

```sh
$ docker-compose exec app ./scripts/run_spark_submit.sh
```

## AWS Credentials

To boto3 works is necessary configure [aws cli](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/install-cliv2.html) and [aws environment variables](https://docs.aws.amazon.com/pt_br/sdk-for-java/v1/developer-guide/setup-credentials.html) in local machine.


## Evidence

Below is the print that proves that the dataframe in csv was sent to the aws s3 bucket in my personal account.
![print aws datalake](https://github.com/arthur-barbosa18/TESTEPYSPARK-Confitec/blob/main/img/print_aws_datalake.png)
