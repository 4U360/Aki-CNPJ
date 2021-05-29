from ..base import AkiObject
from ...data.simples import Simples
from typing import NamedTuple

class AkiSimples(AkiObject):
    __tuple: Simples = None

    def __init__(self, simples_tuple: NamedTuple):
        self.__original = simples_tuple

        cnpj_basico = getattr(simples_tuple, "cnpj_basico", "0")
        opcao_simples = str(getattr(simples_tuple, "opcao_simples", ""))
        data_opcao_simples = str(getattr(simples_tuple, "data_opcao_simples", ""))
        data_exclusao_simple = str(getattr(simples_tuple, "data_exclusao_simple", ""))
        opcao_mei = str(getattr(simples_tuple, "opcao_mei", ""))
        data_opcao_mei = str(getattr(simples_tuple, "data_opcao_mei", ""))
        data_exclusao_mei = str(getattr(simples_tuple, "opcao_simples", ""))

        self.__tuple = Simples(
            index=int(cnpj_basico),
            cnpj_basico=str(cnpj_basico).ljust(14, "X"),
            opcao_simples=opcao_simples,
            data_opcao_simples=data_opcao_simples,
            data_exclusao_simple=data_exclusao_simple,
            opcao_mei=opcao_mei,
            data_opcao_mei=data_opcao_mei,
            data_exclusao_mei=data_exclusao_mei
        )

    @property
    def tuple(self) -> Simples:
        return self.__tuple
