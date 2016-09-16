#! /usr/bin/env python

import json
import os

import jsonschema

from pyld import jsonld

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
SCHEMA_FILE_V1_1 = os.path.join(BASE_DIR, 'schema/certificate/1.1/certificate-schema-v1-1.json')
SCHEMA_FILE_V1_2 = os.path.join(BASE_DIR, 'schema/certificate/1.2/blockchain-certificate-1.2.json')
SCHEMA_UNSIGNED_FILE_V1_2 = os.path.join(BASE_DIR, 'schema/certificate/1.2/certificate-document-1.2.json')
JSON_LD_CONTEXT_V1_2 = os.path.join(BASE_DIR, 'schema/certificate/1.2/context.json')


def validate_v1_1(certificate_json):
    """
    throws jsonschema.exceptions.ValidationError on failure
    :param certificate_json:
    :return:
    """

    with open(SCHEMA_FILE_V1_1) as schema_f:
        schema_json = json.load(schema_f)
        return validate_json(certificate_json, schema_json)


def validate_v1_2(certificate_json):
    """
    throws jsonschema.exceptions.ValidationError on failure
    :param certificate_json:
    :return:
    """

    with open(SCHEMA_FILE_V1_2) as schema_f:
        schema_json = json.load(schema_f)
        return validate_json(certificate_json, schema_json)


def validate_unsigned_v1_2(certificate_json):
    """
    throws jsonschema.exceptions.ValidationError on failure
    :param certificate_json:
    :return:
    """

    with open(SCHEMA_UNSIGNED_FILE_V1_2) as schema_f:
        schema_json = json.load(schema_f)
        # first a conditional check not done in the json schema
        if certificate_json['recipient']['hashed'] and not certificate_json['recipient']['salt']:
            # TODO: error reporting
            print('certificate is hashed but has no salt!')
            return False

        return validate_json(certificate_json, schema_json)



def validate_json(certificate_json, schema_json):
    # If no exception is raised by validate(), the instance is valid.
    try:
        jsonschema.validate(certificate_json, schema_json)
        return True
    except jsonschema.exceptions.ValidationError as ve:
        print(ve)
        raise ve


def validate(data_file, schema_file):
    with open(data_file) as data_f, open(schema_file) as schema_f:
        data = json.load(data_f)
        schema = json.load(schema_f)
        return validate_json(data, schema)


def compact_with_json_ld_context(input_json):
    with open(JSON_LD_CONTEXT_V1_2) as context_f:
        ctx = json.load(context_f)
        compacted = jsonld.compact(input_json, ctx)
        return compacted


def _parse_json_ld(filename):
    # just some experiments
    with open(filename) as data_f:
        data = json.load(data_f)
        compacted = compact_with_json_ld_context(data)

        expanded = jsonld.expand(compacted)
        normalized = jsonld.normalize(
            data, {'algorithm': 'URDNA2015', 'format': 'application/nquads'})
        print(json.dumps(expanded, indent=2))


if __name__ == '__main__':
    valid = validate('../../examples/1.1/sample_unsigned_cert-1.1.json',
                     '../schema/certificate/1.1/certificate-schema-v1-1.json')
    print('certificate is valid? ' + str(valid))

    valid = validate('../../examples/1.1/sample_signed_cert-1.1.json',
                     '../schema/certificate/1.1/certificate-schema-v1-1.json')
    print('certificate is valid? ' + str(valid))

    #valid = validate('../../examples/1.2/sample_unsigned_cert-1.2.json',
    #                 '../schema/certificate/1.2/digital-certificate-1.2.json')
    #print('certificate is valid? ' + str(valid))

    valid = validate('../../examples/1.2/sample_signed_cert-1.2.json',
                     '../schema/certificate/1.2/blockchain-certificate-1.2.json')
    print('certificate is valid? ' + str(valid))

    _parse_json_ld('../../examples/1.2/sample_signed_cert-1.2.json')