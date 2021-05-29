from .base import AkiReader
from ..object.table.situacao_cadastral import AkiSituacaoCadastral
from typing import Iterator


class AkiSituacaoCadastralReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiSituacaoCadastral]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiSituacaoCadastral(situacao_tuple=row)

    @property
    def header(self) -> list:
        return [
            "codigo",
            "descricao"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
