import json
import unittest

from werkzeug.contrib.cache import SimpleCache

from cert_schema import validate_v1_2, validate_unsigned_v1_2
from cert_schema.schema_tools import schema_validator
from cert_schema import jsonld_document_loader, BlockcertValidationError

cache = SimpleCache()


class TestSchemaValidator(unittest.TestCase):
    def test_v1_unsigned(self):
        valid = schema_validator.validate('../examples/1.1/sample_unsigned_cert-1.1.json',
                                          '../cert_schema/schema/1.1/certificate-schema-v1-1.json')
        self.assertTrue(valid)

    def test_v1_signed(self):
        valid = schema_validator.validate('../examples/1.1/sample_signed_cert-1.1.json',
                                          '../cert_schema/schema/1.1/certificate-schema-v1-1.json')
        self.assertTrue(valid)

    def test_v1_2_signed(self):
        with open('../examples/1.2/sample_signed_cert-1.2.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v1_2(certificate)
            self.assertTrue(valid)

    def test_v1_2_invalid(self):
        with open('../examples/1.2/sample_invalid_cert-1.2.json') as data_f:
            certificate = json.load(data_f)
            try:
                valid = validate_v1_2(certificate)
            except BlockcertValidationError as bve:
                self.assertTrue(True, 'Got validation error, as expected')
                return
        self.fail('Did not get expected validation error')


    def test_v1_2_signed_multiple_signers(self):
        with open('../examples/1.2/sample_signed_cert_multiple_signers-1.2.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v1_2(certificate)
            self.assertTrue(valid)

    def test_v1_2_unsigned(self):
        with open('../examples/1.2/sample_unsigned_cert-1.2.json') as data_f:
            data = json.load(data_f)
            valid = validate_unsigned_v1_2(data['document'])
            self.assertTrue(valid)

    def test_v1_2_jsonld(self):
        schema_validator._parse_json_ld('../examples/1.2/sample_signed_cert-1.2.json')
        self.assertTrue(True)

    def test_caching(self):
        schema_validator._parse_json_ld('../examples/1.2/sample_signed_cert-1.2.json', cached_document_loader)
        self.assertTrue(True)


def cached_document_loader(url, override_cache=False):
    if not override_cache:
        result = cache.get(url)
        if result:
            return result
    doc = jsonld_document_loader(url)
    cache.set(url, doc)
    return doc
