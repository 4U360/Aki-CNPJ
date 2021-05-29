from .base import AkiObject
from ..data.socios import Socio
from typing import NamedTuple


class AkiSocio(AkiObject):
    __tuple: Socio = None

    def __init__(self, socio_tuple: NamedTuple):
        cnpj_basico = getattr(socio_tuple, "cnpj_basico", "0")
        identificador_socio = getattr(socio_tuple, "identificador_socio", "")
        nome_socio = getattr(socio_tuple, "nome_socio", "")
        cpfcnpj_socio = getattr(socio_tuple, "cpfcnpj_socio", "")
        qualificacao_socio = getattr(socio_tuple, "qualificacao_socio", "")
        data_entrada_sociedade = getattr(socio_tuple, "data_entrada_sociedade", "")
        pais = getattr(socio_tuple, "pais", "")
        representante_legal = getattr(socio_tuple, "representante_legal", "")
        nome_representante_legal = getattr(socio_tuple, "nome_representante_legal", "")
        qualificacao_representante_legal = getattr(socio_tuple, "qualificacao_representante_legal", "")
        faixa_etaria = getattr(socio_tuple, "faixa_etaria", "")

        self.__tuple = Socio(
            index=int(cnpj_basico),
            cnpj_basico=str(cnpj_basico).ljust(14, "X"),
            identificador_socio=identificador_socio,
            nome_socio=nome_socio,
            cpfcnpj_socio=cpfcnpj_socio,
            qualificacao_socio=qualificacao_socio,
            data_entrada_sociedade=data_entrada_sociedade,
            pais=pais,
            representante_legal=representante_legal,
            nome_representante_legal=nome_representante_legal,
            qualificacao_representante_legal=qualificacao_representante_legal,
            faixa_etaria=faixa_etaria
        )

    @property
    def tuple(self) -> Socio:
        return self.__tuple
