from typing import NamedTuple
import json


class AkiObject(object):
    __tuple: NamedTuple = None
    __original: NamedTuple = None

    @property
    def original(self) -> NamedTuple:
        return self.__original

    @property
    def tuple(self) -> NamedTuple:
        return self.__tuple

    def header(self) -> list:
        return list(self.tuple.__annotations__.keys())

    def to_csv(self) -> list:
        return list(self.to_dict().values())

    def to_json(self, **kwargs) -> str:
        return json.dumps(self.to_dict(), **kwargs)

    def to_dict(self) -> dict:
        keys = self.tuple.__annotations__.keys()
        return {key: getattr(self.tuple, key) for key in keys}
