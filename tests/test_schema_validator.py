import json
import unittest

from cert_schema import BlockcertValidationError
from cert_schema import schema_validator
from cert_schema import validate_unsigned_v1_2
from cert_schema import validate_v1_2
from cert_schema import validate_v2
from cert_schema import validate_v2_1
from cert_schema import validate_v3
from cert_schema.schema_validator import validate_v2_alpha


class TestSchemaValidator(unittest.TestCase):
    def test_v1_unsigned(self):
        valid = schema_validator.validate('../examples/1.1/sample_unsigned_cert-1.1.json',
                                          '../cert_schema/1.1/certificate-schema-v1-1.json')
        self.assertTrue(valid)

    def test_v1_signed(self):
        valid = schema_validator.validate('../examples/1.1/sample_signed_cert-1.1.json',
                                          '../cert_schema/1.1/certificate-schema-v1-1.json')
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

    def test_v2_alpha(self):
        with open('../examples/2.0-alpha/sample_valid.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v2_alpha(certificate)
            self.assertTrue(valid)

    def test_v2(self):
        with open('../examples/2.0/bbba8553-8ec1-445f-82c9-a57251dd731c.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v2(certificate)
            self.assertTrue(valid)

    def test_v2_1(self):
        with open('../examples/2.1/sample_valid.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v2_1(certificate)
            self.assertTrue(valid)

    def test_v3(self):
        with open('../examples/3.0/bbba8553-8ec1-445f-82c9-a57251dd731c.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v3(certificate)
            self.assertTrue(valid)

        with open('../examples/3.0/cert-no-proof.json') as data_f:
            certificate = json.load(data_f)
            valid = validate_v3(certificate, True)
            self.assertTrue(valid)
