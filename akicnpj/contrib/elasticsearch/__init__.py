import pathlib

from akicnpj.data.finder import FileCategory


class ElasticInjest:
    from elasticsearch import Elasticsearch
    from akicnpj.settings import (ROOT, AKI_ELASTIC_CNAE_INDEX, AKI_ELASTIC_SITUACAO_CADASTRAL_INDEX,
                                  AKI_ELASTIC_MUNICIPIO_INDEX)
    from akicnpj.reader import (AkiCnaeReader, AkiSituacaoCadastralReader, AkiMunicipioReader)
    from akicnpj.finder import AkiFinder
    from elasticsearch import helpers

    client: Elasticsearch = None

    def __init__(self, client: Elasticsearch):
        assert isinstance(client, self.Elasticsearch)
        self.client = client

    def get_files(self, data_path: pathlib.Path, category: FileCategory):
        assert isinstance(data_path, pathlib.Path)
        for file in self.AkiFinder(path=data_path).search():
            if file.category == category:
                yield file

    def import_cnae(self, data_path: pathlib.Path = ROOT.parent.joinpath('data')):
        extract_path = data_path.joinpath('extract')
        actions = []

        for file in self.get_files(extract_path, FileCategory.CNAE):

            with self.AkiCnaeReader(file.path, encoding="iso-8859-1") as reader:
                for row in reader.rows:
                    doc = row.to_dict()
                    actions.append({
                        "_index": self.AKI_ELASTIC_CNAE_INDEX,
                        "_id": doc.get("codigo"),
                        "_source": doc
                    })

        return self.helpers.bulk(self.client, actions)

    def import_situacao_cadastral(self, data_path: pathlib.Path = ROOT.parent.joinpath('data')):
        extract_path = data_path.joinpath('extract')
        actions = []

        for file in self.get_files(extract_path, FileCategory.CADASTRAL_SITUATION):
            with self.AkiSituacaoCadastralReader(file.path, encoding="iso-8859-1") as reader:
                for row in reader.rows:
                    doc = row.to_dict()
                    actions.append({
                        "_index": self.AKI_ELASTIC_SITUACAO_CADASTRAL_INDEX,
                        "_id": doc.get("codigo"),
                        "_source": doc
                    })

        return self.helpers.bulk(self.client, actions)

    def import_municipios(self, data_path: pathlib.Path = ROOT.parent.joinpath('data')):
        extract_path = data_path.joinpath('extract')
        actions = []

        for file in self.get_files(extract_path, FileCategory.CITY):
            with self.AkiMunicipioReader(file.path, encoding="iso-8859-1") as reader:
                for row in reader.rows:
                    doc = row.to_dict()
                    actions.append({
                        "_index": self.AKI_ELASTIC_MUNICIPIO_INDEX,
                        "_id": doc.get("codigo"),
                        "_source": doc
                    })

        return self.helpers.bulk(self.client, actions)
