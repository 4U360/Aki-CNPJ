from .base import AkiReader
from ..object.company import AkiCompany
from typing import Iterator

class AkiCompanyReader(AkiReader):

    @property
    def rows(self) -> Iterator[AkiCompany]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiCompany(company_tuple=row)

    @property
    def header(self) -> list:
        return [
            "cnpj_basico",
            "razao_social",
            "natureza_legal",
            "qualificacao_responsavel",
            "capital_social",
            "porte",
            "ente_federativo"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
