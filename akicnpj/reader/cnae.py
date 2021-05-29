from .base import AkiReader
from ..object.table.cnae import AkiCnae
from typing import Iterator


class AkiCnaeReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiCnae]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiCnae(cnae_tuple=row)

    @property
    def header(self) -> list:
        return [
            "codigo",
            "descricao"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
