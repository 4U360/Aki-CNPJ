from .base import AkiReader
from ..object.socios import AkiSocio
from typing import Iterator


class AkiSociosReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiSocio]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiSocio(socio_tuple=row)

    @property
    def header(self) -> list:
        return [
            "cnpj_basico",
            "identificador_socio",
            "nome_socio",
            "cpfcnpj_socio",
            "qualificacao_socio",
            "data_entrada_sociedade",
            "pais",
            "representante_legal",
            "nome_representante_legal",
            "qualificacao_representante_legal",
            "faixa_etaria"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
