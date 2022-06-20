import json
import unittest
import os

from cert_schema import normalize_jsonld

# with these tests we are ensuring that jsonld documents consider all properties for hashing
class TestHashingProperties(unittest.TestCase):
    # def test_context_property(self):
    #     with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
    #         certificate = json.load(data_f)
    #         initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
    #         certificate['@context'][1]['temperingContext'] = {
    #             "@id": "https://schema.org/Text"
    #         }
    #         tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
    #        self.assertFalse(initial_normalized == tempered_normalized)

    def test_id_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['id'] = 'modified-id'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_type_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['@context'][-1] =  {
                "BlockcertsCredentialTempered": {
                    "@id": "bc:BlockcertsCredentialTempered"
                }
            }
            certificate['type'][-1] = 'BlockcertsCredentialTempered'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_issuer_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['issuer'] = 'did:example:my-totally-legit-did'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_issuanceDate_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['issuanceDate'] = '2021-02-17T10:47:25Z'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_expirationDate_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['expirationDate'] = '2031-02-17T10:47:25Z'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_name_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['name'] = 'Blue Jeans'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_email_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['email'] = 'blue@jeans.com'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_publicKey_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['publicKey'] = '12QrRKgQmBtDxbcjWg1etTU9mr5xcDXkTX'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_id_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['id'] = 'modified-id'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_claim_image_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['image'] = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA0JCgsKCA0'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_claim_description_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['description'] = 'This description has been modified'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_claim_criteria_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['criteria'] = 'This criteria has been modified'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_credentialSubject_claim_url_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['credentialSubject']['claim']['url'] = 'https://another-url.com'
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_metadata_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['metadata'] = "{\"key\":\"other value\"}"
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_display_contentMediaType_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['display']['contentMediaType'] = "modified"
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)

    def test_display_content_property(self):
        with open(os.path.join(os.path.dirname(__file__), './fixtures/v3-display-html.json')) as data_f:
            certificate = json.load(data_f)
            initial_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            certificate['display']['content'] = "<div>Hello Mexico</div>"
            tempered_normalized = normalize_jsonld(certificate, detect_unmapped_fields=True)
            self.assertFalse(initial_normalized == tempered_normalized)
