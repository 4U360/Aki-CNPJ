from os import getenv

CHUNKSIZE = 10 ** 6 if getenv("AKI_CHUNKSIZE", None) else int(getenv("AKI_CHUNKSIZE", 10 ** 6))
