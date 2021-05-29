from .base import AkiReader
from ..object.table.simples import AkiSimples
from typing import Iterator


class AkiSimplesReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiSimples]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiSimples(simples_tuple=row)

    @property
    def header(self) -> list:
        return [
            "cnpj_basico",
            "opcao_simples",
            "data_opcao_simples",
            "data_exclusao_simple",
            "opcao_mei",
            "data_opcao_mei",
            "data_exclusao_mei"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
