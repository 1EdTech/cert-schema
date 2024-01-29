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

    def v2_1(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V2_1_CONTEXT']

    def v2_1_canonical(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V2_1_CANONICAL_CONTEXT']

    def v2_1_blockcerts_org(self):
        return self.CONTEXT_URLS['BLOCKCERTS_ORG_V2_1_CONTEXT']

    def v2_1_all(self):
        return [
            self.v2_1(),
            self.v2_1_canonical(),
            self.v2_1_blockcerts_org()
        ]

    def v3(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V3_CONTEXT']

    def v3_canonical(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V3_CANONICAL_CONTEXT']

    def v3_blockcerts_org(self):
        return self.CONTEXT_URLS['BLOCKCERTS_ORG_V3_CONTEXT']

    def v3_all(self):
        return [
            self.v3(),
            self.v3_canonical(),
            self.v3_blockcerts_org()
        ]

    def v3_1(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V3_1_CONTEXT']

    def v3_1_canonical(self):
        return self.CONTEXT_URLS['BLOCKCERTS_V3_1_CANONICAL_CONTEXT']

    def v3_1_blockcerts_org(self):
        return self.CONTEXT_URLS['BLOCKCERTS_ORG_V3_1_CONTEXT']

    def v3_1_all(self):
        return [
            self.v3_1(),
            self.v3_1_canonical(),
            self.v3_1_blockcerts_org()
        ]

    def open_badge(self):
        return self.CONTEXT_URLS['OPEN_BADGES_V2_CONTEXT']

    def open_badge_canonical(self):
        return self.CONTEXT_URLS['OPEN_BADGES_V2_CANONICAL_CONTEXT']

    def verifiable_credential(self):
        return self.CONTEXT_URLS['VERIFIABLE_CREDENTIAL_V1_CONTEXT']

    def verifiable_credential_v1(self):
        return self.CONTEXT_URLS['VERIFIABLE_CREDENTIAL_V1_CONTEXT']

    def verifiable_credential_v2(self):
        return self.CONTEXT_URLS['VERIFIABLE_CREDENTIAL_V2_CONTEXT']

    def status_list_2021(self):
        return self.CONTEXT_URLS['STATUS_LIST_2021_CONTEXT']

    def merkle_proof_2019(self):
        return self.CONTEXT_URLS['MERKLE_PROOF_2019_CONTEXT']

    def chained_proof_2021(self):
        return self.CONTEXT_URLS['CHAINED_PROOF_2021_CONTEXT']
