import unittest

from cert_schema import *


class TestInit(unittest.TestCase):
    def test_parse_chain_from_address_mainnet(self):
        chain = parse_chain_from_address('1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v')
        self.assertEquals(chain, Chain.mainnet)
        self.assertEquals(chain.netcode, 'BTC')
        self.assertEquals(chain.name, 'mainnet')

    def test_parse_chain_from_address_testnet(self):
        chain = parse_chain_from_address('mjgZHpD1AzEixLgcnncod5df6CntYK4Jpi')
        self.assertEquals(chain, Chain.testnet)
        self.assertEquals(chain.netcode, 'XTN')
        self.assertEquals(chain.name, 'testnet')

    def test_parse_chain_from_chain_string_mainnet(self):
        chain = Chain.parse_from_chain('mainnet')
        self.assertEquals(chain, Chain.mainnet)

    def test_parse_chain_from_chain_string_testnet(self):
        chain = Chain.parse_from_chain('testnet')
        self.assertEquals(chain, Chain.testnet)

    def test_parse_chain_from_chain_string_regtest(self):
        chain = Chain.parse_from_chain('regtest')
        self.assertEquals(chain, Chain.regtest)

    def test_parse_chain_from_chain_string_mocknet(self):
        chain = Chain.parse_from_chain('mocknet')
        self.assertEquals(chain, Chain.mocknet)

    def test_parse_chain_from_netcode_mainnet(self):
        chain = Chain.parse_from_netcode('BTC')
        self.assertEquals(chain, Chain.mainnet)

    def test_parse_chain_from_chain_testnet(self):
        chain = Chain.parse_from_netcode('XTN')
        self.assertEquals(chain, Chain.testnet)

    def test_parse_chain_from_chain_testnet(self):
        chain = Chain.parse_from_netcode('MOK')
        self.assertEquals(chain, Chain.mocknet)

    def test_blockcerts_versions_v2(self):
        v2_alpha = BlockcertVersion.V2_ALPHA
        self.assertEquals(v2_alpha, BlockcertVersion.V2_ALPHA)

if __name__ == '__main__':
    unittest.main()
