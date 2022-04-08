import unittest

from cert_schema import ContextUrls

class TestContextUrls(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.instance = ContextUrls()

    def test_v2(self):
        output = self.instance.v2()
        self.assertTrue(output == 'https://w3id.org/blockcerts/schema/2.0/context.json')

    def test_v2_canonical(self):
        output = self.instance.v2_canonical()
        self.assertTrue(output == 'https://w3id.org/blockcerts/v2')

    def test_v2_blockcerts_org(self):
        output = self.instance.v2_blockcerts_org()
        self.assertTrue(output == 'https://www.blockcerts.org/schema/2.0/context.json')

    def test_v2_all(self):
        output = self.instance.v2_all()
        self.assertEqual(output, [
            'https://w3id.org/blockcerts/schema/2.0/context.json',
            'https://w3id.org/blockcerts/v2',
            'https://www.blockcerts.org/schema/3.0/context.json'
        ])