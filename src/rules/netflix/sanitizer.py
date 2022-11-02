""" Module To Sanitizer process """

from pyspark.sql.functions import (col, to_date, when,
                                   lower,
                                   current_timestamp,
                                   from_utc_timestamp)
from src.repo import log
from src.rules.process import Process


class Sanitizer(Process):
    """Class to Sanitizer data
    """

    def convert_cols_to_datetime(self):
        """ Convert columns Premiere and dt_inclusao to date """
        self.table.dataframe = self.table.dataframe.withColumn(
            "Premiere", to_date(col("Premiere"), "d-MMM-yy"))
        self.table.dataframe = self.table.dataframe = self.table.dataframe\
            .withColumn("dt_inclusao",
                        from_utc_timestamp(col("dt_inclusao"),
                                           "America/Sao_Paulo"))

    def order_gender_active_desc(self):
        """Sort by gender column and active columns descending
        """
        log.info("Start sort by gender column and active columns descending")
        self.table.dataframe = self.table.dataframe\
            .withColumn("Genre", lower(col("Genre")))\
            .orderBy(col("Genre").desc(), col("Active").desc())

    def remove_duplicated(self):
        """Remove duplicated rows in dataframe """
        log.info("Remove duplicate rows in dataframe")
        self.table.dataframe = self.table.dataframe.distinct()

    def change_seasons(self):
        """ Change value 'TBA' to 'a ser anunciado' from Seasons """
        log.info("Changeg value 'TBA' to 'a ser anunciado'"
                 "from 'Seasons' column")
        self.table.dataframe = self.table.dataframe.withColumn("Seasons", when(
            col("Seasons") == "TBA", "a ser anunciado")
            .otherwise(col("Seasons")))

    def create_column_alter_date(self):
        """ Create a column 'Data de Alteração' with current timestamp """
        log.info("Create column 'Data de Alteração' with current timestamp")
        self.table.dataframe = self.table.dataframe.withColumn(
            "Data de Alteração", current_timestamp())

    def column_names_standardization(self):
        """ Standardization of column names in Portuguese """
        log.info("Start of column renaming process")
        self.table.dataframe = self.table.dataframe\
            .withColumnRenamed("Title", "Título")\
            .withColumnRenamed("Genre", "Gênero")\
            .withColumnRenamed("GenreLabels", "Rótulos de Gênero")\
            .withColumnRenamed("Premiere", "Pré-estreia")\
            .withColumnRenamed("Seasons", "Temporadas")\
            .withColumnRenamed("SeasonsParsed", "Temporadas Analisadas")\
            .withColumnRenamed("EpisodesParsed", "Episódios Analisados")\
            .withColumnRenamed("Length", "Duração")\
            .withColumnRenamed("MinLength", "Duração Mínima")\
            .withColumnRenamed("MaxLength", "Duração Máxima")\
            .withColumnRenamed("Status", "Status")\
            .withColumnRenamed("Active", "Ativo")\
            .withColumnRenamed("Table", "Tabela")\
            .withColumnRenamed("Language", "Linguagem")\
            .withColumnRenamed("dt_inclusao", "Data de Inclusão")

    def process(self):
        """ Process Function """
        log.info("Start Sanitizer process")
        if self.table.dataframe:
            self.convert_cols_to_datetime()
            self.order_gender_active_desc()
            self.remove_duplicated()
            self.change_seasons()
            self.create_column_alter_date()
            self.column_names_standardization()
