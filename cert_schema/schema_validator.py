#! /usr/bin/env python

import json
import logging

import jsonschema
import os

from cert_schema.errors import BlockcertValidationError

V2_SCHEMA_LOCAL_PATH = '2.0/schema.json'
V2_1_SCHEMA_LOCAL_PATH = '2.0/schema.json'
V3_ALPHA_SCHEMA_LOCAL_PATH = '3.0-alpha/schema.json'
V3_BETA_SCHEMA_LOCAL_PATH = '3.0-beta/schema.json'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SCHEMA_FILE_V1_1 = os.path.join(BASE_DIR, '1.1/certificate-schema-v1-1.json')
SCHEMA_FILE_V1_2 = os.path.join(BASE_DIR, '1.2/blockchain-certificate-1.2.json')
SCHEMA_FILE_V2_0_ALPHA = os.path.join(BASE_DIR, '2.0-alpha/schema.json')
SCHEMA_FILE_V2_0 = os.path.join(BASE_DIR, V2_SCHEMA_LOCAL_PATH)
SCHEMA_FILE_V2_1 = os.path.join(BASE_DIR, V2_1_SCHEMA_LOCAL_PATH)
SCHEMA_FILE_V3_ALPHA = os.path.join(BASE_DIR, V3_ALPHA_SCHEMA_LOCAL_PATH)
SCHEMA_FILE_V3_BETA = os.path.join(BASE_DIR, V3_BETA_SCHEMA_LOCAL_PATH)

SCHEMA_UNSIGNED_FILE_V1_2 = os.path.join(BASE_DIR, '1.2/certificate-document-1.2.json')


def validate_v1_1(certificate_json):
    """
    Propagates BlockcertValidationError on failure
    :param certificate_json:
    :return:
    """

    with open(SCHEMA_FILE_V1_1) as schema_f:
        schema_json = json.load(schema_f)
        return validate_json(certificate_json, schema_json)


def validate_v1_2(certificate_json):
    """
    Propagates BlockcertValidationError on failure
    :param certificate_json:
    :return:
    """

    with open(SCHEMA_FILE_V1_2) as schema_f:
        schema_json = json.load(schema_f)
        return validate_json(certificate_json, schema_json)


def validate_v2(certificate_json):
    with open(SCHEMA_FILE_V2_0) as schema_f:
        schema_json = json.load(schema_f)
        return validate_json(certificate_json, schema_json)


def validate_v2_alpha(certificate_json):
    with open(SCHEMA_FILE_V2_0_ALPHA) as blockcerts_schema:
        schema_v2 = json.load(blockcerts_schema)
        result = validate_json(certificate_json, schema_v2)
        return result


def validate_v2_1(certificate_json):
    with open(SCHEMA_FILE_V2_1) as blockcerts_schema:
        schema_v2_1 = json.load(blockcerts_schema)
        result = validate_json(certificate_json, schema_v2_1)
        return result


def validate_unsigned_v1_2(certificate_json):
    """
    Raises or propagates BlockcertValidationError on failure
    :param certificate_json:
    :return:
    """
    with open(SCHEMA_UNSIGNED_FILE_V1_2) as schema_f:
        schema_json = json.load(schema_f)
        # first a conditional check not done in the json schema
        if certificate_json['recipient']['hashed'] and not certificate_json['recipient']['salt']:
            logging.error('certificate is hashed but has no salt')
            raise jsonschema.exceptions.ValidationError('certificate is hashed but has no salt')

        return validate_json(certificate_json, schema_json)


def validate_v3_alpha(certificate_json, ignore_proof=False):
    with open(SCHEMA_FILE_V3_ALPHA) as schema_f:
        schema_json = json.load(schema_f)
        if ignore_proof:
            schema_json['required'].remove('proof')
        return validate_json(certificate_json, schema_json)


def validate_v3_beta(certificate_json, ignore_proof=False):
    with open(SCHEMA_FILE_V3_BETA) as schema_f:
        schema_json = json.load(schema_f)
        if ignore_proof:
            schema_json['required'].remove('proof')
        return validate_json(certificate_json, schema_json)


def validate_json(certificate_json, schema_json):
    """
    If no exception is raised, the instance is valid. Raises BlockcertValidationError is validation fails.
    :param certificate_json:
    :param schema_json:
    :return:
    """
    try:
        jsonschema.validate(certificate_json, schema_json)
        return True
    except jsonschema.exceptions.ValidationError as ve:
        logging.error(ve, exc_info=True)
        raise BlockcertValidationError(ve)


def validate(data_file, schema_file):
    with open(data_file) as data_f, open(schema_file) as schema_f:
        data = json.load(data_f)
        schema = json.load(schema_f)
        return validate_json(data, schema)


if __name__ == '__main__':
    valid = validate('../../examples/1.1/sample_unsigned_cert-1.1.json',
                     '../1.1/certificate-schema-v1-1.json')
    print('certificate is valid? ' + str(valid))

    valid = validate('../../examples/1.1/sample_signed_cert-1.1.json',
                     '../1.1/certificate-schema-v1-1.json')
    print('certificate is valid? ' + str(valid))

    valid = validate('../../examples/1.2/sample_signed_cert-1.2.json',
                     '../1.2/blockchain-certificate-1.2.json')
    print('certificate is valid? ' + str(valid))
