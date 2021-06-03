from akicnpj.finder import AkiFinder
from akicnpj.reader.company import AkiCompanyReader

import pathlib

ROOT = pathlib.Path(__file__).parent.parent

if __name__ == "__main__":

    for file in AkiFinder(path=ROOT.joinpath("data").joinpath("extract")).search():

        if file.suffix != ".zip":
            if file.suffix == ".EMPRECSV":
                with AkiCompanyReader(filename=str(file)) as reader:
                    for row in reader.rows:
                        print(row.to_csv())
