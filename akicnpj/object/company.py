from .base import AkiObject
from ..data.company import Company
from typing import NamedTuple
from decimal import Decimal


class AkiCompany(AkiObject):
    __tuple: Company = None

    def __init__(self, company_tuple: NamedTuple):
        self.__original = company_tuple

        cnpj_basico = getattr(company_tuple, "cnpj_basico", "0")
        razao_social = getattr(company_tuple, "razao_social", "")
        natureza_legal = getattr(company_tuple, "natureza_legal", "0000")
        qualificacao_responsavel = getattr(company_tuple, "qualificacao_responsavel", "00")
        capital_social = str(getattr(company_tuple, "capital_social", "0.0")).replace(",", ".")
        porte = getattr(company_tuple, "porte", "1")

        if porte == "":
            porte = "1"

        ente_federativo = getattr(company_tuple, "ente_federativo", "")

        self.__tuple = Company(
            index=int(cnpj_basico),
            cnpj_basico=str(cnpj_basico).ljust(14, "X"),
            razao_social=str(razao_social),
            natureza_legal=str(natureza_legal),
            qualificacao_responsavel=str(qualificacao_responsavel),
            capital_social=Decimal(capital_social),
            porte=int(porte),
            ente_federativo=str(ente_federativo)
        )

    @property
    def tuple(self) -> Company:
        return self.__tuple
