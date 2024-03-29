import unittest
from elasticsearch import Elasticsearch
from akicnpj.contrib.elasticsearch import ElasticInjest


class ElasticTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Elasticsearch("http://localhost:9200")

    def test_cnae_injest(self):
        injest = ElasticInjest(client=self.client)
        result = injest.import_cnae()
        self.assertIsInstance(result, tuple)
        self.assertGreater(result[0], 0)

    def test_situacao_cadastral_injest(self):
        injest = ElasticInjest(client=self.client)
        result = injest.import_situacao_cadastral()
        self.assertIsInstance(result, tuple)
        self.assertGreater(result[0], 0)

    def test_municipio_injest(self):
        injest = ElasticInjest(client=self.client)
        result = injest.import_municipios()
        self.assertIsInstance(result, tuple)
        self.assertGreater(result[0], 0)


if __name__ == '__main__':
    unittest.main()
