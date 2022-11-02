from src.rules.netflix.sanitizer import Sanitizer
from src.tables.table import Table


def test_convert_cols_to_datetime(create_spark_session, close_spark_session):
    columns = ["Premiere", "dt_inclusao"]
    data = [("19-Apr-13", "2021-03-16T21:20:24.167-03:00"),
            ("19-Apr-13", "2021-03-16T21:20:24.167-03:00"),
            ("12-Dec-14", "2021-03-16T21:20:24.167-03:00")]
    spark = create_spark_session
    table = Table(spark)
    table.dataframe = spark.createDataFrame(data).toDF(*columns)
    Sanitizer(spark, table).convert_cols_to_datetime()
    assert table.dataframe.select("Premiere").dtypes[0][1] == "date"
    assert table.dataframe.select("dt_inclusao").dtypes[0][1] == "timestamp"
    close_spark_session(spark)


def test_order_gender_active_desc(create_spark_session, close_spark_session):
    columns = ["Genre", "Active"]
    data = [("A", 1), ("A", 0), ("B", 0)]
    data_result_expected = [("b", 0), ("a", 1), ("a", 0)]
    spark = create_spark_session
    table = Table(spark)
    table_expected = Table(spark)
    table.dataframe = spark.createDataFrame(data).toDF(*columns)
    table_expected.dataframe = spark.createDataFrame(
        data_result_expected).toDF(*columns)
    Sanitizer(spark, table).order_gender_active_desc()
    assert table.dataframe.collect() == table_expected.dataframe.collect()
    close_spark_session(spark)


def test_remove_duplicated(create_spark_session, close_spark_session):
    columns = ["COL1", "COL2", "COL3"]
    data = [("A", "B", "C"), ("A", "B", "C"), ("G", "H", "I")]
    spark = create_spark_session
    table = Table(spark)
    table.dataframe = spark.createDataFrame(data).toDF(*columns)
    Sanitizer(spark, table).remove_duplicated()
    assert table.dataframe.count() == 2
    close_spark_session(spark)


def test_change_seasons(create_spark_session, close_spark_session):
    columns = ["Seasons", "Qualquer Outra"]
    data = [("A", "B"), ("TBA", "B"), ("G", "B"), ("TBA", "B")]
    spark = create_spark_session
    table = Table(spark)
    table.dataframe = spark.createDataFrame(data).toDF(*columns)
    Sanitizer(spark, table).change_seasons()
    assert table.dataframe.collect()[0].Seasons == "A"
    assert table.dataframe.collect()[1].Seasons == "a ser anunciado"
    assert table.dataframe.collect()[2].Seasons == "G"
    assert table.dataframe.collect()[3].Seasons == "a ser anunciado"
    close_spark_session(spark)


def test_create_column_alter_date(create_spark_session, close_spark_session):
    columns = ["COL1", "COL2", "COL3"]
    data = [("A", "B", "C"), ("A", "B", "C"), ("G", "H", "I")]
    spark = create_spark_session
    table = Table(spark)
    table.dataframe = spark.createDataFrame(data).toDF(*columns)
    Sanitizer(spark, table).create_column_alter_date()
    assert "Data de Alteração" in table.dataframe.columns
    assert table.dataframe.select(
        "Data de Alteração").dtypes[0][1] == "timestamp"
    close_spark_session(spark)


def test_column_names_standardization(create_spark_session, close_spark_session):
    columns = ["Title", "Genre", "GenreLabels", "Premiere", "Seasons",
               "SeasonsParsed", "EpisodesParsed", "Length", "MinLength", "MaxLength",
               "Status", "Active", "Table", "Language", "dt_inclusao", ]
    data = [("1", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", 11, 12, 13, 14, 15)]
    spark = create_spark_session
    table = Table(spark)
    table.dataframe = spark.createDataFrame(data).toDF(*columns)
    Sanitizer(spark, table).column_names_standardization()
    columns_expected = ["Título", "Gênero", "Rótulos de Gênero", "Pré-estreia", "Temporadas",
                        "Temporadas Analisadas", "Episódios Analisados", "Duração", "Duração Mínima",
                        "Duração Máxima", "Status", "Ativo", "Tabela", "Linguagem", "Data de Inclusão"]
    assert set(columns_expected) == set(table.dataframe.columns)
    close_spark_session(spark)
