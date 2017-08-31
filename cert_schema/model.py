"""
class ProofType(Enum):
    merkle_proof_2017 = 0


class SignatureType(Enum):
    signed_content = 0,
    signed_transaction = 1


Signature
---------
  |
  |-- EmbeddedSignature: signs "contents" directly
  |
  |-- TransactionSignature: "contents" are embedded in transaction. Merkle proof for multiple

"""

import re
import sys

import pytz
from dateutil.parser import parse

from cert_schema import *

V1_1_REGEX = re.compile('[0-9a-fA-F]{24}')
V1_2_REGEX = re.compile('[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}')

USE_PREFIX = False


def scope_name(name):
    """
    TBD whether we want to include prefix. Doing this for now. Default is no prefix
    :param name:
    :return:
    """
    if USE_PREFIX:
        return BLOCKCERTS_PREFIX + name
    else:
        return name


class SignatureLine(object):
    def __init__(self, image, name=None, job_title=None):
        self.image = image
        self.name = name
        self.job_title = job_title


class ProofType(Enum):
    merkle_proof_2017 = 0


class SignatureType(Enum):
    signed_content = 0,
    signed_transaction = 1


class Signature(object):
    def __init__(self, signature_type, content_to_verify):
        self.signature_type = signature_type
        self.content_to_verify = content_to_verify


class TransactionSignature(Signature):
    """
    Content is embedded in transaction in some manner
    """

    def __init__(self, content_to_verify, transaction_id, merkle_proof=None):
        super(TransactionSignature, self).__init__(SignatureType.signed_transaction, content_to_verify)
        self.transaction_id = transaction_id
        self.merkle_proof = merkle_proof


class EmbeddedSignature(Signature):
    """
    Content is signed directly
    """

    def __init__(self, content_to_verify, signature_value):
        super(EmbeddedSignature, self).__init__(SignatureType.signed_content, content_to_verify)
        self.signature_value = signature_value


class MerkleProof(object):
    def __init__(self, target_hash, merkle_root, proof_type, original_proof_json):
        self.target_hash = target_hash
        self.merkle_root = merkle_root
        self.proof_type = proof_type
        self.proof_json = original_proof_json
        from copy import deepcopy
        merkle_proof = deepcopy(original_proof_json)
        self.merkle_proof = merkle_proof


class Issuer(object):
    def __init__(self, id, name, image, revocation_url=None):
        self.id = id
        self.name = name
        self.image = image
        self.revocation_url = revocation_url


class BlockchainCertificate(object):
    def __init__(self, version, uid, recipient_name, recipient_public_key, title, description, signature_image,
                 issued_on, expires, subtitle, signatures, certificate_json, txid, issuer, revocation_addresses=[]):
        self.version = version
        self.uid = uid
        self.recipient_name = recipient_name
        self.recipient_public_key = recipient_public_key
        self.title = title
        self.description = description
        self.signature_image = signature_image
        self.issued_on = issued_on
        self.expires = expires
        self.subtitle = subtitle
        self.signatures = signatures
        self.certificate_json = certificate_json
        self.txid = txid
        self.issuer = issuer
        self.revocation_addresses = revocation_addresses

    def __str__(self):
        sb = []
        for key in self.__dict__:
            _value = self.__dict__[key]

            if _value and isstring(_value) and 'data:image/png;base64' in str(_value):
                mapped_value = '<base64_encoded_image>'
            elif _value:
                mapped_value = _value
            else:
                mapped_value = '<None>'
            sb.append("{key}='{value}'".format(key=key, value=mapped_value))

        return ', '.join(sb)

    def __repr__(self):
        return self.__str__()


def isstring(s):
    if (sys.version_info[0] >= 3):
        return isinstance(s, str)
    return isinstance(s, basestring)


def parse_issuer(issuer_json):
    if 'revocationList' in issuer_json:
        revocation_list = issuer_json['revocationList']
    else:
        revocation_list = None
    return Issuer(issuer_json['id'], issuer_json['name'], issuer_json['image'], revocation_list)


def detect_version(certificate_json):
    # assumes it's a certificate. Maybe add some schema validation
    if not '@context' in certificate_json:
        return BlockcertVersion.V1_1
    context = certificate_json['@context']
    if isinstance(context, list):
        version_marker = context[-1]
    else:
        version_marker = context

    if 'v1' in version_marker:
        return BlockcertVersion.V1_2
    elif '2.0-alpha' in version_marker:
        return BlockcertVersion.V2_ALPHA
    elif '2.0' in version_marker or 'v2' in version_marker:
        return BlockcertVersion.V2

    raise UnknownBlockcertVersionException()


def is_v1_uid(uid):
    if V1_1_REGEX.search(uid):
        return True
    else:
        return False


def parse_merkle_proof(proof_json):
    proof_type = ProofType.merkle_proof_2017
    return MerkleProof(proof_json['targetHash'], proof_json['merkleRoot'], proof_type, proof_json)


def parse_date(raw_date):
    if raw_date is None:
        return None
    parsed_date = parse(raw_date)
    utc = pytz.UTC
    if parsed_date.tzinfo is None or parsed_date.tzinfo.utcoffset(parsed_date) is None:
        parsed_date = utc.localize(parsed_date)
    return parsed_date


def parse_expires_date(assertion):
    if 'expires' in assertion:
        return parse_date(assertion['expires'])
    else:
        return None


def get_value_or_default(node, field):
    value = None
    if field in node:
        value = node[field]
    return value


def parse_v2_blockchain_certificate(certificate_json, version_marker):
    assertion = certificate_json
    uid = assertion['id']
    badge = assertion['badge']
    recipient = assertion['recipient']
    issuer = parse_issuer(badge['issuer'])
    issued_on = parse_date(assertion['issuedOn'])
    signature = assertion[scope_name('signature')]
    txid = signature['anchors'][0]['sourceId']
    merkle_proof = parse_merkle_proof(signature)

    signature_lines = []
    if scope_name('signatureLines') in badge:
        signature_lines_raw = badge[scope_name('signatureLines')]
        for l in signature_lines_raw:
            image = l['image']
            name = get_value_or_default(l, 'name')
            job_title = get_value_or_default(l, 'job_title')
            signature_lines.append(SignatureLine(image, name, job_title))

    subtitle = get_value_or_default(badge, 'subtitle')

    if version_marker == BlockcertVersion.V2_ALPHA:
        recipient_profile = recipient[scope_name('recipientProfile')]
    else:
        recipient_profile = certificate_json[scope_name('recipientProfile')]

    recipient_public_key_full = recipient_profile['publicKey']
    recipient_public_key = str.split(str(recipient_public_key_full), ':')[1]

    import copy
    document_json = copy.deepcopy(certificate_json)
    del document_json['signature']

    transaction_signature = TransactionSignature(document_json, txid, merkle_proof)

    return BlockchainCertificate(version_marker,
                                 uid,
                                 recipient_profile['name'],
                                 recipient_public_key,
                                 badge['name'],
                                 badge['description'],
                                 signature_lines,
                                 issued_on,
                                 parse_expires_date(assertion),
                                 subtitle,
                                 [transaction_signature],
                                 certificate_json,
                                 txid,
                                 issuer)


def parse_v1_2_blockchain_certificate(certificate_json):
    document = certificate_json['document']
    receipt = certificate_json['receipt']
    certificate = document['certificate']
    assertion = document['assertion']
    recipient = document['recipient']

    recipient_public_key = recipient['publicKey']
    issued_on = parse_date(assertion['issuedOn'])
    issuer = parse_issuer(certificate['issuer'])
    assertion_uid = assertion['uid']
    txid = receipt['anchors'][0]['sourceId']

    signature_lines = []
    if 'image:signature' in assertion:
        signature_lines.append(SignatureLine(assertion['image:signature']))

    subtitle = get_value_or_default(certificate, 'subtitle')
    recipient_revocation_address = get_value_or_default(recipient, 'revocationKey')

    revocation_addresses = [recipient_public_key]
    if recipient_revocation_address:
        revocation_addresses.append(recipient_revocation_address)

    embedded_signature = EmbeddedSignature(assertion_uid, document['signature'])
    transaction_signature = TransactionSignature(document, txid, parse_merkle_proof(receipt))

    return BlockchainCertificate(BlockcertVersion.V1_2,
                                 assertion_uid,
                                 recipient['givenName'] + ' ' + recipient['familyName'],
                                 recipient_public_key,
                                 certificate['name'],
                                 certificate['description'],
                                 signature_lines,
                                 issued_on,
                                 parse_expires_date(assertion),
                                 subtitle,
                                 [embedded_signature, transaction_signature],
                                 certificate_json,
                                 txid,
                                 issuer,
                                 revocation_addresses)


def parse_v1_1_blockchain_certificate(json_certificate, txid, certificate_bytes):
    subtitle = json_certificate['certificate']['subtitle']['content']
    display_subtitle = json_certificate['certificate']['subtitle']['display']
    if display_subtitle in ['true', 'True', 'TRUE']:
        subtitle = subtitle
    else:
        subtitle = None

    issuer = parse_issuer(json_certificate['certificate']['issuer'])
    issued_on = parse_date(json_certificate['assertion']['issuedOn'])
    recipient_pubkey = json_certificate['recipient']['pubkey']
    assertion_uid = json_certificate['assertion']['uid']

    revocation_addresses = [recipient_pubkey]

    embedded_signature = EmbeddedSignature(assertion_uid, json_certificate['signature'])
    transaction_signature = TransactionSignature(certificate_bytes, txid)

    signature_lines = []
    if 'image:signature' in json_certificate['assertion']:
        signature_lines.append(SignatureLine(json_certificate['assertion']['image:signature']))
    return BlockchainCertificate(BlockcertVersion.V1_1,
                                 assertion_uid,
                                 json_certificate['recipient']['givenName'] + ' ' + json_certificate['recipient'][
                                     'familyName'],
                                 recipient_pubkey,
                                 json_certificate['certificate']['title'],
                                 json_certificate['certificate']['description'],
                                 signature_lines,
                                 issued_on,
                                 parse_expires_date(json_certificate['assertion']),
                                 subtitle,
                                 [embedded_signature, transaction_signature],
                                 json_certificate,
                                 txid,
                                 issuer,
                                 revocation_addresses)


def to_certificate_model(certificate_json, txid=None, certificate_bytes=None):
    version = detect_version(certificate_json)
    if version == BlockcertVersion.V1_1:
        if not txid or not certificate_bytes:
            raise InvalidCertificateError('V1.1 Blockchain Certificates require a transaction id and raw bytes')
        return parse_v1_1_blockchain_certificate(certificate_json, txid, certificate_bytes)
    elif version == BlockcertVersion.V1_2:
        return parse_v1_2_blockchain_certificate(certificate_json)
    elif version == BlockcertVersion.V2 or version == BlockcertVersion.V2_ALPHA:
        return parse_v2_blockchain_certificate(certificate_json, version)
    else:
        raise UnknownBlockcertVersionException(version)
