from dataclasses import dataclass
from datetime import datetime


@dataclass
class AkiFile:
    name: str = ""
    url: str = ""
    last_modified: datetime = None
    size: int = 0
    size_str: str = ""
    description: str = ""
