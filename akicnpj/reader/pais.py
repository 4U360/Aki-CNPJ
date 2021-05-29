from .base import AkiReader
from ..object.table.pais import AkiPais
from typing import Iterator


class AkiPaisReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiPais]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiPais(pais_tuple=row)

    @property
    def header(self) -> list:
        return [
            "codigo",
            "descricao"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
