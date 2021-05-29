from .base import AkiObject
from ..data.estabelecimento import Estabelecimento
from typing import NamedTuple


class AkiEstabelecimento(AkiObject):
    __tuple: Estabelecimento = None

    def __init__(self, estabelecimento_tuple: NamedTuple):
        cnpj_basico = getattr(estabelecimento_tuple, "cnpj_basico", "0")
        cnpj_ordem = getattr(estabelecimento_tuple, "cnpj_ordem", "")
        cnpj_dv = getattr(estabelecimento_tuple, "cnpj_dv", "")
        identificador = getattr(estabelecimento_tuple, "identificador", "")
        nome_fantasia = getattr(estabelecimento_tuple, "nome_fantasia", "")
        situacao_cadastral = getattr(estabelecimento_tuple, "situacao_cadastral", "")
        data_situacao_cadastral = getattr(estabelecimento_tuple, "data_situacao_cadastral", "")
        motivo_situacao_cadastral = getattr(estabelecimento_tuple, "motivo_situacao_cadastral", "")
        nome_cidade_no_exterior = getattr(estabelecimento_tuple, "nome_cidade_no_exterior", "")
        pais = getattr(estabelecimento_tuple, "pais", "")
        data_inicio_atividade = getattr(estabelecimento_tuple, "data_inicio_atividade", "")
        cnae_fiscal_principal = getattr(estabelecimento_tuple, "cnae_fiscal_principal", "")
        cnae_fiscal_secundario = getattr(estabelecimento_tuple, "cnae_fiscal_secundario", "")
        tipo_logradouro = getattr(estabelecimento_tuple, "tipo_logradouro", "")
        logradouro = getattr(estabelecimento_tuple, "logradouro", "")
        complemento = getattr(estabelecimento_tuple, "complemento", "")
        bairro = getattr(estabelecimento_tuple, "bairro", "")
        cep = getattr(estabelecimento_tuple, "cep", "")
        uf = getattr(estabelecimento_tuple, "uf", "")
        municipio = getattr(estabelecimento_tuple, "municipio", "")
        ddd1 = getattr(estabelecimento_tuple, "ddd1", "")
        telefone1 = getattr(estabelecimento_tuple, "telefone1", "")
        ddd2 = getattr(estabelecimento_tuple, "ddd2", "")
        telefone2 = getattr(estabelecimento_tuple, "telefone2", "")
        fax = getattr(estabelecimento_tuple, "fax", "")
        correio_eletronico = getattr(estabelecimento_tuple, "correio_eletronico", "")
        situacao_especial = getattr(estabelecimento_tuple, "situacao_especial", "")
        data_situacao_especial = getattr(estabelecimento_tuple, "data_situacao_especial", "")

        self.__tuple = Estabelecimento(
            index=int(cnpj_basico),
            cnpj_basico=str(cnpj_basico).ljust(14, "X"),
            cnpj_ordem=cnpj_ordem,
            cnpj_dv=cnpj_dv,
            identificador=identificador,
            nome_fantasia=nome_fantasia,
            situacao_cadastral=situacao_cadastral,
            data_situacao_cadastral=data_situacao_cadastral,
            motivo_situacao_cadastral=motivo_situacao_cadastral,
            nome_cidade_no_exterior=nome_cidade_no_exterior,
            pais=pais,
            data_inicio_atividade=data_inicio_atividade,
            cnae_fiscal_principal=cnae_fiscal_principal,
            cnae_fiscal_secundario=cnae_fiscal_secundario,
            tipo_logradouro=tipo_logradouro,
            logradouro=logradouro,
            complemento=complemento,
            bairro=bairro,
            cep=cep,
            uf=uf,
            municipio=municipio,
            ddd1=ddd1,
            telefone1=telefone1,
            ddd2=ddd2,
            telefone2=telefone2,
            fax=fax,
            correio_eletronico=correio_eletronico,
            situacao_especial=situacao_especial,
            data_situacao_especial=data_situacao_especial
        )

    @property
    def tuple(self) -> Estabelecimento:
        return self.__tuple
