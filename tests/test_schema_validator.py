import json
import unittest

from werkzeug.contrib.cache import SimpleCache

from cert_schema import BlockcertValidationError
from cert_schema import validate_v1_2, validate_unsigned_v1_2, validate_v2, normalize_jsonld, jsonld_document_loader
from cert_schema.schema_tools import schema_validator

cache = SimpleCache()


def cached_document_loader(url, override_cache=False):
    if not override_cache:
        result = cache.get(url)
        if result:
            return result
    doc = jsonld_document_loader(url)
    cache.set(url, doc)
    return doc


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

    def test_v2(self):
        with open('../examples/2.0/sample_valid-2.0.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v2(certificate)
            self.assertTrue(valid)

    def test_v2_unmapped_fields(self):
        with self.assertRaises(BlockcertValidationError):
            with open('../examples/2.0/tampered_unmapped_fields.json') as data_f:
                certificate = json.load(data_f)
                normalize_jsonld(certificate, document_loader=cached_document_loader, detect_unmapped_fields=True)
