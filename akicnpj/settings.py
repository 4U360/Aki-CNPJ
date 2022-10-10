import re
from os import getenv
from pathlib import Path

CHUNKSIZE: int = 10 ** 6 if getenv("AKI_CHUNKSIZE", None) else int(getenv("AKI_CHUNKSIZE", 10 ** 6))
DOWNLOAD_URL: str = getenv("AKI_URL", "http://200.152.38.155/CNPJ/")
ROOT: Path = Path(__file__).parent

AKI_FILE_PATTERN_CNAE = re.compile(getenv("AKI_FILE_PATTERN_CNAE", "Cnaes.zip"))
AKI_FILE_PATTERN_EMPRESA = re.compile(getenv("AKI_FILE_PATTERN_EMPRESA", "Empresas\d+.zip"))
AKI_FILE_PATTERN_SOCIOS = re.compile(getenv("AKI_FILE_PATTERN_SOCIOS", "Socios\d+.zip"))
AKI_FILE_PATTERN_ESTABELECIMENTO = re.compile(getenv("AKI_FILE_PATTERN_ESTABELECIMENTO", "Estabelecimentos\d+.zip"))
AKI_FILE_PATTERN_SIMPLES = re.compile(getenv("AKI_FILE_PATTERN_SIMPLES", "Simples.zip"))
AKI_FILE_PATTERN_MUNICIPIOS = re.compile(getenv("AKI_FILE_PATTERN_MUNICIPIOS", "Municipios.zip"))
AKI_FILE_PATTERN_NATUREZAS_JURIDICAS = re.compile(getenv("AKI_FILE_PATTERN_NATUREZAS_JURIDICAS", "Naturezas.zip"))
AKI_FILE_PATTERN_PAISES = re.compile(getenv("AKI_FILE_PATTERN_PAISES", "Paises.zip"))
AKI_FILE_PATTERN_QSA = re.compile(getenv("AKI_FILE_PATTERN_QSA", "Qualificacoes.zip"))
AKI_FILE_PATTERN_SITUACAO_CADASTRAL = re.compile(getenv("AKI_FILE_PATTERN_SITUACAO_CADASTRAL", "Motivos.zip"))

AKI_ELASTIC_CNAE_INDEX = getenv("AKI_ELASTIC_CNAE_INDEX", "cnae-index")
