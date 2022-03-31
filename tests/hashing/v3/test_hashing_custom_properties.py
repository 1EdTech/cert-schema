import json
import unittest
import os

from cert_schema import normalize_jsonld

# with these tests we are ensuring that jsonld documents consider all properties for hashing
class TestHashingProperties(unittest.TestCase):
    def test_credentialSubject_claim_degree_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-custom-context.json')) as data_f:
            certificate = json.load(data_f)
            initial_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['degree'] = 'Licence of Puppets'
            tempered_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_hash == tempered_hash)

    def test_credentialSubject_claim_yearsOfAttendance_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-custom-context.json')) as data_f:
            certificate = json.load(data_f)
            initial_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['yearsOfAttendance'] = '2023'
            tempered_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_hash == tempered_hash)

    def test_credentialSubject_claim_collegeName_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-custom-context.json')) as data_f:
            certificate = json.load(data_f)
            initial_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['collegeName'] = 'Blockcerts University'
            tempered_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_hash == tempered_hash)

    def test_credentialSubject_claim_certificateNumber_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-custom-context.json')) as data_f:
            certificate = json.load(data_f)
            initial_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['certificateNumber'] = '1234567890'
            tempered_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_hash == tempered_hash)

    def test_credentialSubject_claim_value_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-custom-context.json')) as data_f:
            certificate = json.load(data_f)
            initial_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['value'] = '{\"this\":\"is the full improved transcript as cheated\"}'
            tempered_hash = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_hash == tempered_hash)
