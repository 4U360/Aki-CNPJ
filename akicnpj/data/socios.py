from dataclasses import dataclass


@dataclass
class Socio:
    index: int = 0
    cnpj_basico: str = ""
    identificador_socio: str = ""
    nome_socio: str = ""
    cpfcnpj_socio: str = ""
    qualificacao_socio: str = ""
    data_entrada_sociedade: str = ""
    pais: str = ""
    representante_legal: str = ""
    nome_representante_legal: str = ""
    qualificacao_representante_legal: str = ""
    faixa_etaria: str = ""
