import pathlib
from dataclasses import dataclass
from enum import Enum


class FileCategory(Enum):
    COMPANY = "company"
    CNAE = "cnae"
    ESTABLISHMENT = "establishment"
    PARTNER = "partner"
    SIMPLE = "simple"
    CITY = "city"
    LEGAL_NATURE = "legal_nature"
    COUNTRY = "country"
    CORPORATE_STRUCTURE = "qsa"
    CADASTRAL_SITUATION = "cadastral_situation"


@dataclass
class FinderFile:
    path: pathlib.Path
    category: FileCategory
