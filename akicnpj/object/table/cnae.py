from ..base import AkiObject
from ...data.cnae import Cnae
from typing import NamedTuple

class AkiCnae(AkiObject):
    __tuple: Cnae = None

    def __init__(self, cnae_tuple: NamedTuple):
        self.__original = cnae_tuple

        codigo = int(getattr(cnae_tuple, "codigo", 0))
        descricao = str(getattr(cnae_tuple, "descricao", ""))

        self.__tuple = Cnae(
            codigo=codigo,
            descricao=descricao
        )

    @property
    def tuple(self) -> Cnae:
        return self.__tuple
