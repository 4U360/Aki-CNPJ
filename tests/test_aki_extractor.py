from akicnpj.finder import AkiFinder
from akicnpj.extractor import AkiExtractor
import pathlib
ROOT = pathlib.Path(__file__).parent.parent
if __name__ == "__main__":

    for file in AkiFinder(path=ROOT.joinpath("data").joinpath("extract")).search():

        if file.suffix == ".zip":
            AkiExtractor(file)
