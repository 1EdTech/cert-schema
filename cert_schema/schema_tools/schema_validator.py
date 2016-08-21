#! /usr/bin/env python

import json
import os

import jsonschema

from pyld import jsonld

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def validate_v1_1_0(certificate_json):
    """
    throws jsonschema.exceptions.ValidationError on failure
    :param certificate_json:
    :return:
    """
    schema_file_v1_1_0 = os.path.join(BASE_DIR, 'schema/certificate/1.1.0/certificate-schema-v1-1.json')

    with open(schema_file_v1_1_0) as schema_f:
        schema_json = json.load(schema_f)
        return validate_json(certificate_json, schema_json)


def validate_v1_2_0(certificate_json):
    """
    throws jsonschema.exceptions.ValidationError on failure
    :param certificate_json:
    :return:
    """
    schema_file_v1_2_0 = os.path.join(BASE_DIR, 'schema/certificate/1.2.0/digital-certificate-1.2.0.json')

    with open(schema_file_v1_2_0) as schema_f:
        schema_json = json.load(schema_f)
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


def parse_jsonld():
    # context or @context
    v1_2_file = '../../examples/1.2.0/sample_signed_cert-1.2.0.json'
    context = '../schema/certificate/1.2.0/context.json'
    with open(v1_2_file) as data_f, open(context) as context_f:
        data = json.load(data_f)
        cnt = json.load(context_f)

        compacted = jsonld.compact(data, cnt)
        expanded = jsonld.expand(compacted)

        normalized = jsonld.normalize(
            data, {'algorithm': 'URDNA2015', 'format': 'application/nquads'})
        print(json.dumps(expanded, indent=2))


if __name__ == '__main__':
    valid = validate('../../examples/1.1.0/sample_unsigned_cert-1.1.0.json',
                     '../schema/certificate/1.1.0/certificate-schema-v1-1.json')
    print('certificate is valid? ' + str(valid))

    valid = validate('../../examples/1.1.0/sample_signed_cert-1.1.0.json',
                     '../schema/certificate/1.1.0/certificate-schema-v1-1.json')
    print('certificate is valid? ' + str(valid))

    valid = validate('../../examples/1.2.0/sample_unsigned_cert-1.2.0.json',
                     '../schema/certificate/1.2.0/digital-certificate-1.2.0.json')
    print('certificate is valid? ' + str(valid))

    valid = validate('../../examples/1.2.0/sample_signed_cert-1.2.0.json',
                     '../schema/certificate/1.2.0/digital-certificate-1.2.0.json')
    print('certificate is valid? ' + str(valid))

    #parse_jsonld()



