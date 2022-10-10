from glob import iglob
from typing import Iterator
from .settings import ROOT, Path
from itertools import chain
from .data.finder import FinderFile, FileCategory


class AkiFinder(object):
    __path: Path = None
    __recursive: bool = False

    def __init__(self, path: Path = ROOT.parent.joinpath("data"), recursive: bool = False):

        if path is str:
            path = Path(path)

        self.__path = path
        self.__recursive = recursive

    def search(self) -> Iterator[FinderFile]:
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

    def __find_empresa(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.EMPRECSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.COMPANY)

    def __find_estabelecimento(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.ESTABELE*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.ESTABLISHMENT)

    def __find_socio(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.SOCIOCSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.PARTNER)

    def __find_simples(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.SIMPLES.CSV.*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.SIMPLE)

    def __find_cnae(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.CNAECSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.CNAE)

    def __find_municipio(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.MUNICCSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.CITY)

    def __find_natureza_juridica(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.NATJUCSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.LEGAL_NATURE)

    def __find_pais(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.PAISCSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.COUNTRY)

    def __find_qsa(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.QUALSCSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.CORPORATE_STRUCTURE)

    def __find_situacao_cadastral(self) -> Iterator[FinderFile]:
        path = self.__path.joinpath("*.MOTICSV*")

        for file in iglob(str(path), recursive=self.__recursive):
            yield FinderFile(path=Path(file), category=FileCategory.CADASTRAL_SITUATION)
