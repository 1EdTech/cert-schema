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
            'https://www.blockcerts.org/schema/2.0/context.json'
        ])

    def test_v2_1(self):
        output = self.instance.v2_1()
        self.assertTrue(output == 'https://w3id.org/blockcerts/schema/2.1/context.json')

    def test_v2_1_canonical(self):
        output = self.instance.v2_1_canonical()
        self.assertTrue(output == 'https://w3id.org/blockcerts/v2.1')

    def test_v2_1_blockcerts_org(self):
        output = self.instance.v2_1_blockcerts_org()
        self.assertTrue(output == 'https://www.blockcerts.org/schema/2.1/context.json')

    def test_v2_1_all(self):
        output = self.instance.v2_1_all()
        self.assertEqual(output, [
            'https://w3id.org/blockcerts/schema/2.1/context.json',
            'https://w3id.org/blockcerts/v2.1',
            'https://www.blockcerts.org/schema/2.1/context.json'
        ])

    def test_v3(self):
        output = self.instance.v3()
        self.assertTrue(output == 'https://w3id.org/blockcerts/schema/3.0/context.json')

    def test_v3_canonical(self):
        output = self.instance.v3_canonical()
        self.assertTrue(output == 'https://w3id.org/blockcerts/v3')

    def test_v3_blockcerts_org(self):
        output = self.instance.v3_blockcerts_org()
        self.assertTrue(output == 'https://www.blockcerts.org/schema/3.0/context.json')

    def test_v3_all(self):
        output = self.instance.v3_all()
        self.assertEqual(output, [
            'https://w3id.org/blockcerts/schema/3.0/context.json',
            'https://w3id.org/blockcerts/v3',
            'https://www.blockcerts.org/schema/3.0/context.json'
        ])

    def test_v3_1(self):
        output = self.instance.v3_1()
        self.assertTrue(output == 'https://w3id.org/blockcerts/schema/3.1/context.json')

    def test_v3_1_canonical(self):
        output = self.instance.v3_1_canonical()
        self.assertTrue(output == 'https://w3id.org/blockcerts/v3.1')

    def test_v3_1_blockcerts_org(self):
        output = self.instance.v3_1_blockcerts_org()
        self.assertTrue(output == 'https://www.blockcerts.org/schema/3.1/context.json')

    def test_v3_1_all(self):
        output = self.instance.v3_1_all()
        self.assertEqual(output, [
            'https://w3id.org/blockcerts/schema/3.1/context.json',
            'https://w3id.org/blockcerts/v3.1',
            'https://www.blockcerts.org/schema/3.1/context.json'
        ])

    def test_open_badge(self):
        output = self.instance.open_badge()
        self.assertTrue(output == 'https://openbadgespec.org/v2/context.json')

    def test_open_badge_canonical(self):
        output = self.instance.open_badge_canonical()
        self.assertTrue(output == 'https://w3id.org/openbadges/v2')

    def test_verifiable_credentials(self):
        output = self.instance.verifiable_credential()
        self.assertTrue(output == 'https://www.w3.org/2018/credentials/v1')

    def test_merkle_proof_2019(self):
        output = self.instance.merkle_proof_2019()
        self.assertTrue(output == 'https://w3id.org/security/suites/merkle-2019/v1')

    def test_chained_proof_2021(self):
        output = self.instance.chained_proof_2021()
        self.assertTrue(output == 'https://w3id.org/security/suites/chained-2021/v1')