from .base import AkiReader
from ..object.table.qsa import AkiQSA
from typing import Iterator


class AkiQSAReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiQSA]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiQSA(cnae_tuple=row)

    @property
    def header(self) -> list:
        return [
            "codigo",
            "descricao"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
