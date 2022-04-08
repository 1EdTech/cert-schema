import os
import json
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class ContextUrls:
    def __init__(self):
        with open(os.path.join(BASE_DIR, 'context_urls.json')) as context_data:
            self.CONTEXT_URLS = json.load(context_data)

    def v2(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V2_CONTEXT']

    def v2_canonical(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V2_CANONICAL_CONTEXT']

    def v2_blockcerts_org(self):
        return self.CONTEXT_URLS['BLOCKCERTS_ORG_V2_CONTEXT']

    def v2_all(self):
        return [
            self.v2(),
            self.v2_canonical(),
            self.v2_blockcerts_org()
        ]