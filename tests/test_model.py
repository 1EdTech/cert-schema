import json
import unittest

from cert_schema import BlockcertVersion
from cert_schema import helpers
from cert_schema import model
from cert_schema.model import ProofType, parse_date
from cert_schema.model import SignatureType


class TestModel(unittest.TestCase):
    def test_detect_version_v1_1(self):
        with open('data/1.1/sample_signed_cert-1.1.json', 'rb') as cert_file:
            certificate_bytes = cert_file.read()
            certificate_json = helpers.certificate_bytes_to_json(certificate_bytes)
            version = model.detect_version(certificate_json)
            self.assertEquals(version, BlockcertVersion.V1_1)

    def test_detect_version_v1_2(self):
        with open('data/1.2/609c2989-275f-4f4c-ab02-b245cfb09017.json', 'rb') as cert_file:
            certificate_bytes = cert_file.read()
            certificate_json = helpers.certificate_bytes_to_json(certificate_bytes)
            version = model.detect_version(certificate_json)
            self.assertEquals(version, BlockcertVersion.V1_2)

    def test_to_certificate_model_v1_1(self):
        with open('data/1.1/sample_signed_cert-1.1.json', 'rb') as cert_file:
            certificate_bytes = cert_file.read()
            certificate_json = helpers.certificate_bytes_to_json(certificate_bytes)
            txid = '1703d2f5d706d495c1c65b40a086991ab755cc0a02bef51cd4aff9ed7a8586aa'
            certificate_model = model.to_certificate_model(certificate_json, txid, certificate_bytes)
            self.assertEquals(certificate_model.issuer.id,
                              'http://www.blockcerts.org/mockissuer/issuer/got-issuer.json')
            self.assertEquals(certificate_model.txid,
                              '1703d2f5d706d495c1c65b40a086991ab755cc0a02bef51cd4aff9ed7a8586aa')
            self.assertEquals(certificate_model.title, 'Game of Thrones Character')
            self.assertEquals(certificate_model.description,
                              'This certifies that the named character is an official Game of Thrones character.')
            self.assertEquals(certificate_model.uid, '75857d18-0e1c-4933-b4c8-33484396e06b')
            self.assertEquals(certificate_model.subtitle, None)
            self.assertEquals(certificate_model.expires, None)

            self.assertEquals(certificate_model.issuer.name, 'Game of thrones characters')
            self.assertEquals(certificate_model.recipient_public_key, 'mgCNaPM3TFhh8Yn6U6VcEM9jWLhQbizy1x')
            self.assertEquals(certificate_model.issued_on, parse_date('2016-08-29 00:00:00+00:00'))
            # self.assertEquals(certificate_model.blockcert_signature, None)
            self.assertIsNotNone(certificate_model.signature_image[0].image)

            self.assertEquals(certificate_model.signatures[0].signature_type, SignatureType.signed_content)
            self.assertEquals(certificate_model.signatures[1].signature_type, SignatureType.signed_transaction)
            self.assertIsNone(certificate_model.signatures[1].merkle_proof)

    def test_to_certificate_model_v1_2(self):
        """
        Note this is a mainnet certificate with different uid
        :return:
        """
        with open('data/1.2/609c2989-275f-4f4c-ab02-b245cfb09017.json', 'rb') as cert_file:
            certificate_bytes = cert_file.read()
            certificate_json = helpers.certificate_bytes_to_json(certificate_bytes)
            certificate_model = model.to_certificate_model(certificate_json)
            self.assertEquals(certificate_model.version, BlockcertVersion.V1_2)
            self.assertEquals(certificate_model.issuer.id,
                              'http://www.blockcerts.org/mockissuer/issuer/got-issuer_live.json')
            self.assertEquals(certificate_model.txid,
                              '8623beadbc7877a9e20fb7f83eda6c1a1fc350171f0714ff6c6c4054018eb54d')
            self.assertEquals(certificate_model.title, 'Game of Thrones Character')
            self.assertEquals(certificate_model.description,
                              'This certifies that the named character is an official Game of Thrones character.')
            self.assertEquals(certificate_model.uid, '609c2989-275f-4f4c-ab02-b245cfb09017')
            self.assertEquals(certificate_model.subtitle, None)
            self.assertEquals(certificate_model.expires, None)

            self.assertEquals(certificate_model.issuer.name, 'Game of thrones issuer')
            self.assertEquals(certificate_model.recipient_public_key, '1AAGG6jirbu9XwikFpkHokbbiYpjVtFe1G')
            self.assertEquals(certificate_model.issued_on, parse_date('2016-10-03 00:00:00+00:00'))
            self.assertIsNotNone(certificate_model.signature_image[0].image)

    def test_to_proof(self):
        with open('data/1.2/receipt.json') as receipt_file:
            receipt_json = json.load(receipt_file)
            proof = model.parse_merkle_proof(receipt_json['receipt'])
            self.assertEquals(proof.target_hash, '2d3d0f49416587c4ce14c05d47c4193f0da3dd56f7244a568b06484cb8d2fe78')
            self.assertEquals(proof.merkle_root, '3268386feb897f6cab2c100a0edb6f66b4bb3a8745e3e3e8a54b1cb7151a6d96')
            self.assertEquals(proof.proof_type, ProofType.merkle_proof_2017)

    def test_to_v2_proof(self):
        with open('data/2.0/receipt.json') as receipt_file:
            receipt_json = json.load(receipt_file)
            proof = model.parse_merkle_proof(receipt_json)
            self.assertEquals(proof.target_hash,
                              'c9ead76a54426b4ce4899bb921e48f5b55ea7592e5cee4460c86ebf4698ac3a6')
            self.assertEquals(proof.merkle_root,
                              '68f3ede17fdb67ffd4a5164b5687a71f9fbb68da803b803935720f2aa38f7728')
            self.assertEquals(proof.proof_type, ProofType.merkle_proof_2017)

    def test_to_certificate_model_v2_alpha(self):
        with open('data/2.0-alpha/8e0b8a28-beff-43de-a72c-820bc360db3d.json', 'rb') as cert_file:
            certificate_bytes = cert_file.read()
            certificate_json = helpers.certificate_bytes_to_json(certificate_bytes)
            certificate_model = model.to_certificate_model(certificate_json)
            self.assertEquals(certificate_model.version, BlockcertVersion.V2_ALPHA)
            self.assertEquals(certificate_model.issuer.id,
                              'https://www.blockcerts.org/blockcerts_v2_alpha/samples/issuer_testnet.json')
            self.assertEquals(certificate_model.txid,
                              '08e205566662b97f149ad677649bbb94ebc2f46c0ac72bc7c9b57d2d207015f4')
            self.assertEquals(certificate_model.title, 'This is the certificate title')
            self.assertEquals(certificate_model.description, 'This is the display description of the certificate.')
            self.assertEquals(certificate_model.uid, 'urn:uuid:8e0b8a28-beff-43de-a72c-820bc360db3d')
            self.assertEquals(certificate_model.subtitle, None)
            self.assertEquals(certificate_model.expires, None)

            self.assertEquals(certificate_model.issuer.name, 'Issuer Institution Name')
            self.assertEquals(certificate_model.recipient_public_key, 'mkwntSiQmc14H65YxwckLenxY3DsEpvFbe')
            self.assertEquals(certificate_model.issued_on, parse_date('2017-05-01 00:00:00+00:00'))

    def test_to_certificate_model_v2(self):
        with open('data/2.0/bbba8553-8ec1-445f-82c9-a57251dd731c.json', 'rb') as cert_file:
            certificate_bytes = cert_file.read()
            certificate_json = helpers.certificate_bytes_to_json(certificate_bytes)
            certificate_model = model.to_certificate_model(certificate_json)
            self.assertEquals(certificate_model.version, BlockcertVersion.V2)
            self.assertEquals(certificate_model.issuer.id,
                              'https://www.blockcerts.org/samples/2.0/issuer-testnet.json')
            self.assertEquals(certificate_model.txid,
                              'd75b7a5bdb3d5244b753e6b84e987267cfa4ffa7a532a2ed49ad3848be1d82f8')
            self.assertEquals(certificate_model.title, 'Certificate of Accomplishment')
            self.assertEquals(certificate_model.description, 'Lorem ipsum dolor sit amet, mei docendi concludaturque ad, cu nec partem graece. Est aperiam consetetur cu, expetenda moderatius neglegentur ei nam, suas dolor laudem eam an.')
            self.assertEquals(certificate_model.uid, 'urn:uuid:bbba8553-8ec1-445f-82c9-a57251dd731c')
            self.assertEquals(certificate_model.subtitle, None)
            self.assertEquals(certificate_model.expires, None)

            self.assertEquals(certificate_model.issuer.name, 'University of Learning')
            self.assertEquals(certificate_model.recipient_public_key, 'mtr98kany9G1XYNU74pRnfBQmaCg2FZLmc')
            self.assertEquals(certificate_model.issued_on, parse_date('2017-06-29T14:58:57.461422+00:00'))

if __name__ == '__main__':
    unittest.main()
