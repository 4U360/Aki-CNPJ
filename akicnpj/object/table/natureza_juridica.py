from ..base import AkiObject
from ...data.natureza_juridica import NaturezaJuridica
from typing import NamedTuple

class AkiNaturezaJuridica(AkiObject):
    __tuple: NaturezaJuridica = None

    def __init__(self, cnae_tuple: NamedTuple):
        self.__original = cnae_tuple

        codigo = int(getattr(cnae_tuple, "codigo", 0))
        descricao = str(getattr(cnae_tuple, "descricao", ""))

        self.__tuple = NaturezaJuridica(
            codigo=codigo,
            descricao=descricao
        )

    @property
    def tuple(self) -> NaturezaJuridica:
        return self.__tuple
