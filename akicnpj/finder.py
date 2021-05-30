from glob import iglob
from typing import Iterator
from .settings import ROOT, Path
from itertools import chain


class AkiFinder(object):
    __path: Path = None
    __recursive: bool = False

    def __init__(self, path: Path = ROOT.parent.joinpath("data"), recursive: bool = False):

        if path is str:
            path = Path(path)

        self.__path = path
        self.__recursive = recursive

    def search(self) -> Iterator[Path]:
        empresa_ = self.__find_empresa()
        estabelecimento_ = self.__find_estabelecimento()
        socio_ = self.__find_socio()
        simples_ = self.__find_simples()
        cnae_ = self.__find_cnae()
        municipio_ = self.__find_municipio()
        natureza_juridica_ = self.__find_natureza_juridica()
        pais_ = self.__find_pais()
        qsa_ = self.__find_pais()
        situacao_cadastral_ = self.__find_situacao_cadastral()

        files = chain(empresa_, estabelecimento_, socio_, simples_, cnae_, municipio_, natureza_juridica_, pais_, qsa_,
                      situacao_cadastral_)

        for file in files:
            yield file

    def __find_empresa(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.EMPRECSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_estabelecimento(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.ESTABELE.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_socio(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.SOCIOCSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_simples(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.SIMPLES.CSV.*.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_cnae(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.CNAECSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_municipio(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.MUNICCSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_natureza_juridica(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.NATJUCSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_pais(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.PAISCSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_qsa(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.QUALSCSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)

    def __find_situacao_cadastral(self) -> Iterator[Path]:
        path = self.__path.joinpath("*.MOTICSV.zip")

        for file in iglob(str(path), recursive=self.__recursive):
            yield Path(file)
