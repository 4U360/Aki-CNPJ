import zipfile
from .settings import ROOT, Path
from .logger import get_logger


class AkiExtractor(object):
    logger = get_logger()

    def run(self, input_path: Path, output_path: Path = ROOT.parent.joinpath("data").joinpath("extract")) -> bool:

        output_path.mkdir(parents=True, exist_ok=True)

        if input_path is str:
            input_path = Path(input_path)

        if output_path is str:
            output_path = Path(output_path)

        assert input_path.suffix == ".zip"
        assert output_path.is_dir()

        self.logger.info(f"Extracting files from {input_path}")

        with zipfile.ZipFile(input_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)

        self.logger.info(f"Extraction complete!")
        return True
