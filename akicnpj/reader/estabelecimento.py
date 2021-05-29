from .base import AkiReader
from ..object.estabelecimento import AkiEstabelecimento
from typing import Iterator


class AkiEstabelecimentoReader(AkiReader):

    def __init__(self, *args, **kwargs):

        if "low_memory" not in kwargs:
            kwargs["low_memory"] = False

        super(AkiEstabelecimentoReader, self).__init__(*args, **kwargs)

    @property
    def rows(self) -> Iterator[AkiEstabelecimento]:
        for dataframe in self.dataframes:
            for row in dataframe.fillna("").itertuples():
                yield AkiEstabelecimento(estabelecimento_tuple=row)

    @property
    def header(self) -> list:
        return [
            "cnpj_basico",
            "cnpj_ordem",
            "cnpj_dv",
            "identificador",
            "nome_fantasia",
            "situacao_cadastral",
            "data_situacao_cadastral",
            "motivo_situacao_cadastral",
            "nome_cidade_no_exterior",
            "pais",
            "data_inicio_atividade",
            "cnae_fiscal_principal",
            "cnae_fiscal_secundario",
            "tipo_logradouro",
            "logradouro",
            "complemento",
            "bairro",
            "cep",
            "uf",
            "municipio",
            "ddd1",
            "telefone1",
            "ddd2",
            "telefone2",
            "fax",
            "correio_eletronico",
            "situacao_especial",
            "data_situacao_especial"
        ]

    @property
    def delimiter(self) -> str:
        return ';'
