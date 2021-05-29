from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Estabelecimento:
    index: int = 0
    cnpj_basico: str = ""
    cnpj_ordem: str = ""
    cnpj_dv: str = ""
    identificador: str = ""
    nome_fantasia: str = ""
    situacao_cadastral: str = ""
    data_situacao_cadastral: str = ""
    motivo_situacao_cadastral: str = ""
    nome_cidade_no_exterior: str = ""
    pais: str = ""
    data_inicio_atividade: str = ""
    cnae_fiscal_principal: str = ""
    cnae_fiscal_secundario: str = ""
    tipo_logradouro: str = ""
    logradouro: str = ""
    complemento: str = ""
    bairro: str = ""
    cep: str = ""
    uf: str = ""
    municipio: str = ""
    ddd1: str = ""
    telefone1: str = ""
    ddd2: str = ""
    telefone2: str = ""
    fax: str = ""
    correio_eletronico: str = ""
    situacao_especial: str = ""
    data_situacao_especial: str = ""