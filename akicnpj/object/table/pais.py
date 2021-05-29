from ..base import AkiObject
from ...data.pais import Pais
from typing import NamedTuple


class AkiPais(AkiObject):
    __tuple: Pais = None

    def __init__(self, pais_tuple: NamedTuple):
        self.__original = pais_tuple

        codigo = int(getattr(pais_tuple, "codigo", 0))
        descricao = str(getattr(pais_tuple, "descricao", ""))

        self.__tuple = Pais(
            codigo=codigo,
            descricao=descricao
        )

    @property
    def tuple(self) -> Pais:
        return self.__tuple
