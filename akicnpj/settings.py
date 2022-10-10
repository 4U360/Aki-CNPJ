import re
from os import getenv
from pathlib import Path
CHUNKSIZE: int = 10 ** 6 if getenv("AKI_CHUNKSIZE", None) else int(getenv("AKI_CHUNKSIZE", 10 ** 6))
DOWNLOAD_URL: str = getenv("AKI_URL", "http://200.152.38.155/CNPJ/")
ROOT : Path = Path(__file__).parent
AKI_FILE_PATTERN_CNAE = re.compile(getenv("AKI_FILE_PATTERN_CNAE", "Cnaes.zip"))