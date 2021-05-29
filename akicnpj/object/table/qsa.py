from ..base import AkiObject
from ...data.qsa import QSA
from typing import NamedTuple


class AkiQSA(AkiObject):
    __tuple: QSA = None

    def __init__(self, qsa_tuple: NamedTuple):
        self.__original = qsa_tuple

        codigo = int(getattr(qsa_tuple, "codigo", 0))
        descricao = str(getattr(qsa_tuple, "descricao", ""))

        self.__tuple = QSA(
            codigo=codigo,
            descricao=descricao
        )

    @property
    def tuple(self) -> QSA:
        return self.__tuple
