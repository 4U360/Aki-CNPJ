from .base import AkiDownloader
from ..settings import ROOT, Path
from os import makedirs


class AkiEmpresaDownloader(AkiDownloader):

    def download(self, path: Path = ROOT.parent.joinpath("data")):
        makedirs(str(path), exist_ok=True)

        for file in self.files:
            if file.name.endswith("EMPRECSV.zip"):

                full_path = path.joinpath(file.name)
                self.logger.info(f"Downloading {full_path} [{file.size_str}]")

                with open(full_path, "wb") as handler:
                    for chunk in self.get_file_content(file):
                        handler.write(chunk)
