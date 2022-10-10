import decimal
import itertools
from typing import Iterator
from requests import Session
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag
from dehumanizer import parse_string
from ..settings import DOWNLOAD_URL, CHUNKSIZE
from ..data.akifile import AkiFile
from ..logger import get_logger
from tqdm import tqdm


class AkiDownloader(object):
    __session: Session = Session()
    __url: str = DOWNLOAD_URL
    logger = get_logger()

    def __html_to_file(self, tds: Iterator[Tag]) -> AkiFile:
        _, name_el, modified_el, size_el, description_el = tds
        name = name_el.find("a").get("href")
        url = f"{self.__url}{name}"
        modified = datetime.strptime(modified_el.text.strip(), '%Y-%m-%d %H:%M')
        size_str = size_el.text.strip()
        size = parse_string(size_str)
        description = description_el.text

        return AkiFile(name=name, url=url, last_modified=modified, size_str=size_str, size=size,
                       description=description)

    def get_file_content(self, file: AkiFile) -> Iterator[bytes]:

        with self.__session.get(file.url, stream=True) as r:

            r.raise_for_status()
            total_length = r.headers.get('content-length')
            assert total_length is not None
            total_length = int(total_length)

            with tqdm(total=total_length, unit='iB', unit_scale=True, position=0, leave=True) as progress_bar:
                for chunk in r.iter_content(chunk_size=CHUNKSIZE):
                    if isinstance(chunk, bytes):
                        progress_bar.update(len(chunk))
                        yield chunk

    @property
    def files(self) -> Iterator[AkiFile]:
        page = self.__session.get(self.__url).content
        soup = BeautifulSoup(page, "html.parser")
        title = soup.find("title").text
        assert title == "Index of /CNPJ"
        for tr in soup.find_all("tr"):
            tds = tr.find_all("td")

            if len(tds) == 5:
                chain_tds = itertools.chain(*map(lambda td: td.find_all("img"), tds))
                is_parent = any(filter(lambda img: img.get("alt") == "[PARENTDIR]", chain_tds))

                if is_parent:
                    continue
                else:
                    try:
                        yield self.__html_to_file(tr.find_all("td"))
                    except decimal.InvalidOperation:
                        continue

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
