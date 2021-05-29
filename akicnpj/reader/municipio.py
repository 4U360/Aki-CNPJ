from .base import AkiReader
from ..object.table.municipio import AkiMunicipio
from typing import Iterator


class AkiMunicipioReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiMunicipio]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiMunicipio(cnae_tuple=row)

    @property
    def header(self) -> list:
        return [
            "codigo",
            "descricao"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
