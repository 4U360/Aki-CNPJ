from .base import AkiDownloader
from ..settings import ROOT, Path,AKI_FILE_PATTERN_EMPRESA
from os import makedirs


class AkiEmpresaDownloader(AkiDownloader):

    def download(self, path: Path = ROOT.parent.joinpath("data"), ignore_exists: bool = False):
        makedirs(str(path), exist_ok=True)

        for file in self.files:
            if bool(AKI_FILE_PATTERN_EMPRESA.match(file.name)):
                full_path = path.joinpath(file.name)
                yield full_path

                if not ignore_exists and full_path.exists():
                    self.logger.info(f"File {full_path} already exists, skipping...")
                    yield full_path
                    continue

                self.logger.info(f"Downloading {full_path} [{file.size_str}]")

                with open(full_path, "wb") as handler:
                    for chunk in self.get_file_content(file):
                        handler.write(chunk)
