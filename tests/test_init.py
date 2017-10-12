import unittest

from cert_schema import *


class TestInit(unittest.TestCase):
    def test_is_mainnet_address_true(self):
        is_mainnet = is_bitcoin_mainnet_address('1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v')
        self.assertTrue(is_mainnet)

    def test_is_mainnet_address_false(self):
        is_mainnet = is_bitcoin_mainnet_address('mjgZHpD1AzEixLgcnncod5df6CntYK4Jpi')
        self.assertFalse(is_mainnet)

    def test_blockchain_display_value_bitcoin(self):
        chain = BlockchainType.bitcoin
        self.assertEquals(chain.external_display_value, 'BTCOpReturn')

    def test_blockchain_display_value_ethereum(self):
        chain = BlockchainType.ethereum
        self.assertEquals(chain.external_display_value, 'ETHData')

    def test_blockchain_display_value_mock(self):
        chain = BlockchainType.mock
        self.assertEquals(chain.external_display_value, 'Mock')

    def test_parse_from_chain_string_bitcoin_mainnet(self):
        chain = Chain.parse_from_chain('bitcoin_mainnet')
        self.assertEquals(chain, Chain.bitcoin_mainnet)

    def test_parse_from_chain_string_bitcoin_testnet(self):
        chain = Chain.parse_from_chain('bitcoin_testnet')
        self.assertEquals(chain, Chain.bitcoin_testnet)

    def test_parse_from_chain_string_bitcoin_regtest(self):
        chain = Chain.parse_from_chain('bitcoin_regtest')
        self.assertEquals(chain, Chain.bitcoin_regtest)

    def test_parse_from_chain_string_ethereum_mainnet(self):
        chain = Chain.parse_from_chain('ethereum_mainnet')
        self.assertEquals(chain, Chain.ethereum_mainnet)

    def test_parse_from_chain_string_ethereum_testnet(self):
        chain = Chain.parse_from_chain('ethereum_testnet')
        self.assertEquals(chain, Chain.ethereum_testnet)

    def test_parse_from_chain_string_ethereum_ropsten(self):
        chain = Chain.parse_from_chain('ethereum_ropsten')
        self.assertEquals(chain, Chain.ethereum_ropsten)

    def test_parse_from_chain_string_mockchain(self):
        chain = Chain.parse_from_chain('mockchain')
        self.assertEquals(chain, Chain.mockchain)

    def test_parse_from_external_display_value_bitcoin_mainnet(self):
        chain = Chain.parse_from_external_display_value('bitcoinMainnet')
        self.assertEquals(chain, Chain.bitcoin_mainnet)

    def test_parse_from_external_display_value_bitcoin_testnet(self):
        chain = Chain.parse_from_external_display_value('bitcoinTestnet')
        self.assertEquals(chain, Chain.bitcoin_testnet)

    def test_parse_from_external_display_value_bitcoin_regtest(self):
        chain = Chain.parse_from_external_display_value('bitcoinRegtest')
        self.assertEquals(chain, Chain.bitcoin_regtest)

    def test_parse_from_external_display_value_ethereum_mainnet(self):
        chain = Chain.parse_from_external_display_value('ethereumMainnet')
        self.assertEquals(chain, Chain.ethereum_mainnet)

    def test_parse_from_external_display_value_ethereum_testnet(self):
        chain = Chain.parse_from_external_display_value('ethereumTestnet')
        self.assertEquals(chain, Chain.ethereum_testnet)

    def test_parse_from_external_display_value_ethereum_ropsten(self):
        chain = Chain.parse_from_external_display_value('ethereumRopsten')
        self.assertEquals(chain, Chain.ethereum_ropsten)

    def test_parse_from_external_display_value_mockchain(self):
        chain = Chain.parse_from_external_display_value('mockchain')
        self.assertEquals(chain, Chain.mockchain)

    def test_bitcoin_chain_to_netcode_bitcoin_mainnet(self):
        netcode = chain_to_bitcoin_network(Chain.bitcoin_mainnet)
        self.assertEquals(netcode, 'mainnet')

    def test_bitcoin_chain_to_netcode_bitcoin_testnet(self):
        netcode = chain_to_bitcoin_network(Chain.bitcoin_testnet)
        self.assertEquals(netcode, 'testnet')

    def test_bitcoin_chain_to_netcode_bitcoin_testnet(self):
        netcode = chain_to_bitcoin_network(Chain.bitcoin_regtest)
        self.assertEquals(netcode, 'regtest')

    def test_bitcoin_chain_to_netcode_mocknet(self):
        """
        This should fail. Assert that we get an UnknownChainError
        :return:
        """
        try:
            chain_to_bitcoin_network(Chain.mockchain)
            self.assertTrue(False)
        except UnknownChainError:
            self.assertTrue(True)

    def test_bitcoin_chain_to_netcode_ethereum_mainnet(self):
        """
        This should fail. Assert that we get an UnknownChainError
        :return:
        """
        try:
            chain_to_bitcoin_network(Chain.ethereum_mainnet)
            self.assertTrue(False)
        except UnknownChainError:
            self.assertTrue(True)

    def test_blockcerts_versions_v2(self):
        v2_alpha = BlockcertVersion.V2_ALPHA
        self.assertEquals(v2_alpha, BlockcertVersion.V2_ALPHA)

if __name__ == '__main__':
    unittest.main()
