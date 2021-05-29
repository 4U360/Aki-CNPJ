from typing import Iterator, Any
from akicnpj.settings import CHUNKSIZE
from pandas import read_csv
from pandas.io.parsers import TextFileReader
from pandas import DataFrame



class AkiReader(object):
    __pd_reader: TextFileReader = None
    __open_settings: dict = {}
    __filename: str = ""

    @property
    def chunk_size(self) -> int:
        return CHUNKSIZE

    @property
    def dataframes(self) -> Iterator[DataFrame]:
        for chunk in self.reader:
            yield chunk

    @property
    def rows(self) -> Iterator[Any]:
        yield None

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

    def __init__(self, filename: str, **settings):
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
