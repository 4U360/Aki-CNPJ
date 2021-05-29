from dataclasses import dataclass


@dataclass
class Simples:
    index: int = 0
    cnpj_basico: str = ""
    opcao_simples: str = ""
    data_opcao_simples: str = ""
    data_exclusao_simple: str = ""
    opcao_mei: str = ""
    data_opcao_mei: str = ""
    data_exclusao_mei: str = ""
