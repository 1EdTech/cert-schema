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


class Chain(Enum):
    mainnet = 0, 'BTC'
    testnet = 1, 'XTN'
    regtest = 2, 'XTN'
    # Made up code; hopefully it will never cause a conflict =/
    mocknet = 3, 'MOK'

    def __new__(cls, enum_value, netcode):
        obj = object.__new__(cls)
        obj._value_ = enum_value
        obj.netcode = netcode
        return obj

    @staticmethod
    def parse_from_chain(chain_string):
        if chain_string == 'mainnet':
            return Chain.mainnet
        elif chain_string == 'testnet':
            return Chain.testnet
        elif chain_string == 'regtest':
            return Chain.regtest
        elif chain_string == 'mocknet':
            return Chain.mocknet
        else:
            raise UnknownChainError(chain_string)

    @staticmethod
    def parse_from_netcode(netcode_string):
        if netcode_string == 'BTC':
            return Chain.mainnet
        elif netcode_string == 'XTN':
            return Chain.testnet
        elif netcode_string == 'MOK':
            return Chain.mocknet
        else:
            raise UnknownChainError(netcode_string)


def parse_chain_from_address(address):
    if address.startswith('1'):
        return Chain.mainnet
    elif address.startswith('m') or address.startswith('n'):
        return Chain.testnet
    else:
        raise UnknownChainError('Unrecognized bitcoin address')


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
