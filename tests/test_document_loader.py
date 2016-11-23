import unittest

from werkzeug.contrib.cache import SimpleCache

from cert_schema import jsonld_document_loader, BlockcertValidationError

cache = SimpleCache()


class TestDocumentLoader(unittest.TestCase):

    def test_bogus_url(self):
        try:
            cached_document_loader('bogus_url')
        except BlockcertValidationError as bve:
            self.assertTrue(True, 'caught expected validation exception')
            return

        self.fail('Did not catch BlockcertValidationError')

    def test_working_url(self):
        doc = cached_document_loader('https://w3id.org/blockcerts/v1')
        self.assertIsNotNone(doc)


def cached_document_loader(url, override_cache=False):
    if not override_cache:
        result = cache.get(url)
        if result:
            return result
    doc = jsonld_document_loader(url)
    cache.set(url, doc)
    return doc
