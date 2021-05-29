from ..base import AkiObject
from ...data.municipio import Municipio
from typing import NamedTuple


class AkiMunicipio(AkiObject):
    __tuple: Municipio = None

    def __init__(self, cnae_tuple: NamedTuple):
        self.__original = cnae_tuple

        codigo = int(getattr(cnae_tuple, "codigo", 0))
        descricao = str(getattr(cnae_tuple, "descricao", ""))

        self.__tuple = Municipio(
            codigo=codigo,
            descricao=descricao
        )

    @property
    def tuple(self) -> Municipio:
        return self.__tuple
