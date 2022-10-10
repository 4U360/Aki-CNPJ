import pathlib


class ElasticInjest:
    from elasticsearch import Elasticsearch
    from akicnpj.settings import (ROOT, AKI_ELASTIC_CNAE_INDEX)
    from akicnpj.reader import (AkiCnaeReader, )
    from akicnpj.finder import AkiFinder
    from elasticsearch import helpers

    client: Elasticsearch = None

    def __init__(self, client: Elasticsearch):
        assert isinstance(client, self.Elasticsearch)
        self.client = client

    def import_cnae(self, data_path: pathlib.Path = ROOT.parent.joinpath('data')):
        assert isinstance(data_path, pathlib.Path)

        for file in self.AkiFinder(path=data_path.joinpath('extract')).search():
            if file.category == file.category.CNAE:
                with self.AkiCnaeReader(file.path, encoding="iso-8859-1") as reader:
                    actions = []
                    for row in reader.rows:
                        doc = row.to_dict()
                        actions.append({
                            "_index": self.AKI_ELASTIC_CNAE_INDEX,
                            "_id": doc.get("codigo"),
                            "_source": doc
                        })

        return self.helpers.bulk(self.client, actions)
