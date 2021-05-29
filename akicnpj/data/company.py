from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Company:
    index: int = 0
    cnpj_basico: str = ""
    razao_social: str = ""
    natureza_legal: str = "0000"
    qualificacao_responsavel: str = "00"
    capital_social: Decimal = Decimal(0)
    porte: int = 1
    ente_federativo: str = ""
