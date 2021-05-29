from ..base import AkiObject
from ...data.situacao_cadastral import SituacaoCadastral
from typing import NamedTuple


class AkiSituacaoCadastral(AkiObject):
    __tuple: SituacaoCadastral = None

    def __init__(self, situacao_tuple: NamedTuple):
        self.__original = situacao_tuple

        codigo = int(getattr(situacao_tuple, "codigo", 0))
        descricao = str(getattr(situacao_tuple, "descricao", ""))

        self.__tuple = SituacaoCadastral(
            codigo=codigo,
            descricao=descricao
        )

    @property
    def tuple(self) -> SituacaoCadastral:
        return self.__tuple
