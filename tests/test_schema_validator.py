import unittest

from cert_schema.schema_tools import schema_validator


class TestSchemaValidator(unittest.TestCase):

    def test_v1_unsigned(self):
        valid = schema_validator.validate('../examples/1.1/sample_unsigned_cert-1.1.json',
                                  '../cert_schema/schema/certificate/1.1/certificate-schema-v1-1.json')
        self.assertTrue(valid)

    def test_v1_signed(self):
        valid = schema_validator.validate('../examples/1.1/sample_signed_cert-1.1.json',
                                  '../cert_schema/schema/certificate/1.1/certificate-schema-v1-1.json')
        self.assertTrue(valid)

    def test_v1_2_signed(self):
        valid = schema_validator.validate('../examples/1.2/sample_signed_cert-1.2.json',
                                  '../cert_schema/schema/certificate/1.2/blockchain-certificate-1.2.json')
        self.assertTrue(valid)
        #_parse_json_ld('../../examples/1.2/sample_signed_cert-1.2.json')