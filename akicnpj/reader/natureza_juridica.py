from .base import AkiReader
from ..object.table.natureza_juridica import AkiNaturezaJuridica
from typing import Iterator


class AkiNaturezaJuridicaReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiNaturezaJuridica]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiNaturezaJuridica(cnae_tuple=row)

    @property
    def header(self) -> list:
        return [
            "codigo",
            "descricao"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
