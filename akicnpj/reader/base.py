from __future__ import annotations

import pathlib
from typing import Iterator
from akicnpj.settings import CHUNKSIZE
from akicnpj.object.base import AkiObject
from pandas import read_csv
from pandas.io.parsers import TextFileReader
from pandas import DataFrame
from ..logger import get_logger


class AkiReader(object):
    __pd_reader: TextFileReader = None
    __open_settings: dict = {}
    __filename: str = ""
    __logger = get_logger()

    @property
    def chunk_size(self) -> int:
        return CHUNKSIZE

    @property
    def dataframes(self) -> Iterator[DataFrame]:
        for chunk in self.reader:
            yield chunk

    @property
    def rows(self) -> Iterator[AkiObject]:
        yield None

    def __rows_list(self):
        for row in self.rows:
            yield row.to_csv()

    def rows_to_dataframe(self) -> DataFrame:
        self.__logger.info("Converting rows to dataframe, this can take a while")
        col_iterator = zip(*self.__rows_list())

        # Due to the limitation of only being able to iterate the chunks once, it is necessary to "re-open" the file.
        self.open(True)
        col_names = next(self.rows).header()
        return DataFrame({cn: cv for (cn, cv) in zip(col_names, col_iterator)})

    @property
    def reader(self) -> TextFileReader:
        return self.__pd_reader

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def settings(self) -> dict:
        return self.__open_settings

    @property
    def header(self) -> list:
        return []

    @property
    def delimiter(self) -> str:
        return ';'

    def open(self, force: bool = False):
        if self.__pd_reader is None or force:
            self.__pd_reader = read_csv(self.filename, chunksize=self.chunk_size, sep=self.delimiter,
                                        header=None,
                                        index_col=False,
                                        names=self.header,
                                        **self.settings)

    def __init__(self, filename: str | pathlib.Path, **settings):

        if isinstance(filename, pathlib.Path):
            filename = str(filename)

        assert isinstance(filename, str)
        self.__filename = filename

        if isinstance(settings, dict):
            self.__open_settings.update(settings)

    def __enter__(self):
        if not isinstance(self.__pd_reader, TextFileReader):
            self.open(force=True)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__pd_reader.close()
