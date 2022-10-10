import pathlib
import unittest
from akicnpj.downloader import AkiSimplesDownloader
from akicnpj.extractor import AkiExtractor
from akicnpj.object.table.simples import AkiSimples
from akicnpj.reader import AkiSociosReader
from akicnpj.finder import AkiFinder

ROOT = pathlib.Path(__file__).parent.parent
DATA_PATH = ROOT.joinpath("data")
EXTRACT_PATH = DATA_PATH.joinpath("extract")


class SociosTestCase(unittest.TestCase):
    zip_files = []

    def test_download(self):
        files = list(AkiSimplesDownloader().download())
        self.assertGreater(len(files), 0)

        for file in files:
            self.assertIsInstance(file, pathlib.Path)
            self.zip_files.append(file)

    def test_extractor(self):
        self.assertGreater(len(self.zip_files), 0)

        for file in self.zip_files:
            self.assertTrue(AkiExtractor().run(input_path=file))

    def test_find_and_read(self):
        for file in AkiFinder(path=EXTRACT_PATH).search():
            if file.category == file.category.SIMPLE:
                with AkiSociosReader(file.path, encoding="iso-8859-1") as reader:
                    for row in reader.rows:
                        self.assertIsInstance(row, AkiSimples)


if __name__ == '__main__':
    unittest.main()
