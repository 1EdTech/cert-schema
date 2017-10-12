from enum import Enum

SECURITY_CONTEXT_URL = 'https://w3id.org/security/v1'
OPEN_BADGES_V2_CONTEXT = 'https://openbadgespec.org/v2/context.json'
OPEN_BADGES_V2_CANONICAL_CONTEXT = 'https://w3id.org/openbadges/v2'
BLOCKCERTS_V2_ALPHA_CONTEXT = 'https://w3id.org/blockcerts/schema/2.0-alpha/context.json'
BLOCKCERTS_V2_ALPHA_SCHEMA = 'https://w3id.org/blockcerts/schema/2.0-alpha/schema.json'
BLOCKCERTS_V2_CONTEXT = 'https://w3id.org/blockcerts/schema/2.0/context.json'
BLOCKCERTS_V2_SCHEMA = 'https://w3id.org/blockcerts/schema/2.0/schema.json'
BLOCKCERTS_V2_CANONICAL_CONTEXT = 'https://w3id.org/blockcerts/v2'
PUBKEY_PREFIX = 'ecdsa-koblitz-pubkey:'
BLOCKCERTS_VOCAB = 'https://w3id.org/blockcerts/v2#'
BLOCKCERTS_PREFIX = 'bc:'
URN_UUID_PREFIX = 'urn:uuid:'

class BlockcertVersion(Enum):
    V1_1 = 0
    V1_2 = 1
    V2_ALPHA = -1
    V2 = 2


class BlockchainType(Enum):
    bitcoin = 0, 'BTCOpReturn'
    ethereum = 1, 'ETHData'
    mock = 2, 'Mock'
    
    def __new__(cls, enum_value,  external_display_value):
        obj = object.__new__(cls)
        obj._value_ = enum_value
        obj.external_display_value = external_display_value
        return obj


class Chain(Enum):
    bitcoin_mainnet = 0, BlockchainType.bitcoin, 'bitcoinMainnet'
    bitcoin_testnet = 1, BlockchainType.bitcoin, 'bitcoinTestnet'
    bitcoin_regtest = 2, BlockchainType.bitcoin, 'bitcoinRegtest'
    mockchain = 3, BlockchainType.mock, 'mockchain'
    ethereum_mainnet = 4, BlockchainType.ethereum, 'ethereumMainnet'
    ethereum_ropsten = 5, BlockchainType.ethereum, 'ethereumRopsten'
    ethereum_testnet = 6, BlockchainType.ethereum, 'ethereumTestnet'

    def __new__(cls, enum_value, blockchain_type, external_display_value):
        obj = object.__new__(cls)
        obj._value_ = enum_value
        obj.blockchain_type = blockchain_type
        obj.external_display_value = external_display_value
        return obj

    @staticmethod
    def parse_from_chain(chain_string):
        if chain_string == 'bitcoin_mainnet':
            return Chain.bitcoin_mainnet
        elif chain_string == 'bitcoin_testnet':
            return Chain.bitcoin_testnet
        elif chain_string == 'bitcoin_regtest':
            return Chain.bitcoin_regtest
        elif chain_string == 'mockchain':
            return Chain.mockchain
        elif chain_string == 'ethereum_mainnet':
            return Chain.ethereum_mainnet
        elif chain_string == 'ethereum_ropsten':
            return Chain.ethereum_ropsten
        elif chain_string == 'ethereum_testnet':
            return Chain.ethereum_testnet
        else:
            raise UnknownChainError(chain_string)

    @staticmethod
    def parse_from_external_display_value(external_display_value):
        if external_display_value == 'bitcoinMainnet':
            return Chain.bitcoin_mainnet
        elif external_display_value == 'bitcoinTestnet':
            return Chain.bitcoin_testnet
        elif external_display_value == 'bitcoinRegtest':
            return Chain.bitcoin_regtest
        elif external_display_value == 'mockchain':
            return Chain.mockchain
        elif external_display_value == 'ethereumMainnet':
            return Chain.ethereum_mainnet
        elif external_display_value == 'ethereumRopsten':
            return Chain.ethereum_ropsten
        elif external_display_value == 'ethereumTestnet':
            return Chain.ethereum_testnet
        else:
            raise UnknownChainError(external_display_value)


def chain_to_bitcoin_network(chain):
    """
    Used or bitcoin.SelectParams
    :param chain:
    :return:
    """
    if chain == Chain.bitcoin_mainnet:
        return 'mainnet'
    elif chain == Chain.bitcoin_testnet:
        return 'testnet'
    elif chain == Chain.bitcoin_regtest:
        return 'regtest'
    else:
        message = 'This chain cannot be converted to a bitcoin netcode; chain='
        if chain:
            message += chain.name
        else:
            message += '<NULL>'
        raise UnknownChainError(message)


def to_source_id(txid, chain):
    if chain == Chain.mainnet or Chain.testnet:
        return txid
    else:
        return 'This has not been issued on a blockchain and is for testing only'


def to_anchor_type(chain):
    """
    Return the anchor type to include in the Blockcert signature. In next version of Blockcerts schema we will be able
    to write XTNOpReturn for testnet
    :param chain:
    :return:
    """
    if chain == Chain.mainnet or chain == Chain.testnet:
        return 'BTCOpReturn'
    # non-standard
    elif chain == Chain.regtest:
        return 'REGOpReturn'
    # non-standard
    elif chain == Chain.mockchain:
        return 'MockOpReturn'


def is_bitcoin_mainnet_address(address):
    return address.startswith('1') or address.startswith(PUBKEY_PREFIX + '1')


class BlockcertValidationError(Exception):
    pass


class InvalidUrlError(Exception):
    pass


class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class InvalidCertificateError(Error):
    """
    Certificate lacks fields required to parse for display
    """
    pass


class UnknownChainError(Error):
    """
    Didn't recognize chain
    """
    pass


class UnknownBlockcertVersionException(Error):
    """
    Didn't recognize blockcert version
    """
    pass


from cert_schema.jsonld_helpers import jsonld_document_loader
from cert_schema.schema_validator import validate_unsigned_v1_2, validate_v1_2, validate_v2
from cert_schema.jsonld_helpers import normalize_jsonld
from cert_schema.jsonld_helpers import JSONLD_OPTIONS
