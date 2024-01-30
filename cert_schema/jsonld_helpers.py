#! /usr/bin/env python
import json
import os
import re
from copy import deepcopy

import requests
from pyld import jsonld
from pyld.jsonld import JsonLdProcessor
import validators

from cert_schema.errors import *
from cert_schema.context_urls import ContextUrls

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

ContextUrlsInstance = ContextUrls()

OPEN_BADGES_V2_CONTEXT = ContextUrlsInstance.open_badge()
OPEN_BADGES_V2_CANONICAL_CONTEXT = ContextUrlsInstance.open_badge_canonical()

VERIFIABLE_CREDENTIAL_V1_CONTEXT = ContextUrlsInstance.verifiable_credential_v1()
VERIFIABLE_CREDENTIAL_V2_CONTEXT = ContextUrlsInstance.verifiable_credential_v2()

BLOCKCERTS_V2_ALPHA_CONTEXT = 'https://w3id.org/blockcerts/schema/2.0-alpha/context.json'
BLOCKCERTS_ORG_V2_ALPHA_CONTEXT = 'https://www.blockcerts.org/schema/2.0-alpha/context.json'

BLOCKCERTS_V2_CONTEXT = ContextUrlsInstance.v2()
BLOCKCERTS_ORG_V2_CONTEXT = ContextUrlsInstance.v2_blockcerts_org()
BLOCKCERTS_V2_CANONICAL_CONTEXT = ContextUrlsInstance.v2_canonical()

BLOCKCERTS_V2_1_CONTEXT = ContextUrlsInstance.v2_1()
BLOCKCERTS_ORG_V2_1_CONTEXT = ContextUrlsInstance.v2_1_blockcerts_org()
BLOCKCERTS_V2_1_CANONICAL_CONTEXT = ContextUrlsInstance.v2_1_canonical()

BLOCKCERTS_V3_ALPHA_CONTEXT = 'https://w3id.org/blockcerts/schema/3.0-alpha/context.json'
BLOCKCERTS_V3_ORG_ALPHA_CONTEXT = 'https://www.blockcerts.org/schema/3.0-alpha/context.json'
BLOCKCERTS_V3_ALPHA_CANONICAL_CONTEXT = 'https://w3id.org/blockcerts/v3.0-alpha'

BLOCKCERTS_V3_BETA_CONTEXT = 'https://w3id.org/blockcerts/schema/3.0-beta/context.json'
BLOCKCERTS_V3_ORG_BETA_CONTEXT = 'https://www.blockcerts.org/schema/3.0-beta/context.json'
BLOCKCERTS_V3_BETA_CANONICAL_CONTEXT = 'https://w3id.org/blockcerts/v3.0-beta'

BLOCKCERTS_V3_CONTEXT = ContextUrlsInstance.v3()
BLOCKCERTS__ORG_V3_CONTEXT = ContextUrlsInstance.v3_blockcerts_org()
BLOCKCERTS_V3_CANONICAL_CONTEXT = ContextUrlsInstance.v3_canonical()

BLOCKCERTS_VOCAB = 'https://w3id.org/blockcerts/3.0#'

JSONLD_OPTIONS = {'algorithm': 'URDNA2015', 'format': 'application/nquads'}

FALLBACK_VOCAB = 'http://fallback.org/'
FALLBACK_CONTEXT = {'@vocab': FALLBACK_VOCAB}

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

JSON_LD_CONTEXT_V1_2 = os.path.join(BASE_DIR, '1.2/context.json')
JSON_LD_CONTEXT_V2_0_ALPHA = os.path.join(BASE_DIR, '2.0-alpha/context.json')
JSON_LD_CONTEXT_V2_0 = os.path.join(BASE_DIR, '2.0/context.json')
OBI_JSON_LD_CONTEXT_V2 = os.path.join(BASE_DIR, '2.0/obi.json')

JSON_LD_CONTEXT_V2_1 = os.path.join(BASE_DIR, '2.1/context.json')
OBI_JSON_LD_CONTEXT_V2_1 = os.path.join(BASE_DIR, '2.1/obi.json')

JSON_LD_CONTEXT_V3_0_ALPHA = os.path.join(BASE_DIR, '3.0-alpha/context.json')

JSON_LD_CONTEXT_V3_0_BETA = os.path.join(BASE_DIR, '3.0-beta/context.json')

JSON_LD_CONTEXT_V3_0 = os.path.join(BASE_DIR, '3.0/context.json')
JSON_LD_CONTEXT_V3_1 = os.path.join(BASE_DIR, '3.1/context.json')
MERKLE_PROOF_2019_LD_CONTEXT = os.path.join(BASE_DIR, '3.1/merkleProof2019Context.json')
CHAINED_PROOF_2021_LD_CONTEXT = os.path.join(BASE_DIR, '3.1/chainedProof2021Context.json')
STATUS_LIST_2021_LD_CONTEXT = os.path.join(BASE_DIR, '3.1/statusList2021Context.json')

VERIFIABLE_CREDENTIAL_JSON_LD_CONTEXT_V1 = os.path.join(BASE_DIR, '3.0/credential.json')
VERIFIABLE_CREDENTIAL_JSON_LD_CONTEXT_V2 = os.path.join(BASE_DIR, '3.0/credential_v2.json')

PRELOADED_CONTEXTS = {}

with open(OBI_JSON_LD_CONTEXT_V2) as data_file:
        obi_context = json.load(data_file)
        PRELOADED_CONTEXTS[ContextUrlsInstance.open_badge()] = obi_context
        PRELOADED_CONTEXTS[ContextUrlsInstance.open_badge_canonical()] = obi_context

with open(VERIFIABLE_CREDENTIAL_JSON_LD_CONTEXT_V1) as data_file:
    cred_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.verifiable_credential_v1()] = cred_context

with open(VERIFIABLE_CREDENTIAL_JSON_LD_CONTEXT_V2) as data_file:
    cred_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.verifiable_credential_v2()] = cred_context

with open(MERKLE_PROOF_2019_LD_CONTEXT) as data_file:
    cred_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.merkle_proof_2019()] = cred_context

with open(CHAINED_PROOF_2021_LD_CONTEXT) as data_file:
    cred_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.chained_proof_2021()] = cred_context

with open(STATUS_LIST_2021_LD_CONTEXT) as data_file:
    cred_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.status_list_2021()] = cred_context

with open(JSON_LD_CONTEXT_V2_0_ALPHA) as data_file:
    bc_context = json.load(data_file)
    PRELOADED_CONTEXTS[BLOCKCERTS_V2_ALPHA_CONTEXT] = bc_context
    PRELOADED_CONTEXTS[BLOCKCERTS_ORG_V2_ALPHA_CONTEXT] = bc_context

with open(JSON_LD_CONTEXT_V2_0) as data_file:
    bc_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.v2()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v2_blockcerts_org()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v2_canonical()] = bc_context

with open(JSON_LD_CONTEXT_V2_1) as data_file:
    bc_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.v2_1()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v2_1_blockcerts_org()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v2_1_canonical()] = bc_context

with open(JSON_LD_CONTEXT_V3_0_ALPHA) as data_file:
    bc_context = json.load(data_file)
    PRELOADED_CONTEXTS[BLOCKCERTS_V3_ALPHA_CONTEXT] = bc_context
    PRELOADED_CONTEXTS[BLOCKCERTS_V3_ORG_ALPHA_CONTEXT] = bc_context
    PRELOADED_CONTEXTS[BLOCKCERTS_V3_ALPHA_CANONICAL_CONTEXT] = bc_context

with open(JSON_LD_CONTEXT_V3_0_BETA) as data_file:
    bc_context = json.load(data_file)
    PRELOADED_CONTEXTS[BLOCKCERTS_V3_BETA_CONTEXT] = bc_context
    PRELOADED_CONTEXTS[BLOCKCERTS_V3_ORG_BETA_CONTEXT] = bc_context
    PRELOADED_CONTEXTS[BLOCKCERTS_V3_BETA_CANONICAL_CONTEXT] = bc_context

with open(JSON_LD_CONTEXT_V3_0) as data_file:
    bc_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.v3()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v3_canonical()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v3_blockcerts_org()] = bc_context

with open(JSON_LD_CONTEXT_V3_1) as data_file:
    bc_context = json.load(data_file)
    PRELOADED_CONTEXTS[ContextUrlsInstance.v3_1()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v3_1_canonical()] = bc_context
    PRELOADED_CONTEXTS[ContextUrlsInstance.v3_1_blockcerts_org()] = bc_context

def to_loader_response(data, url):
    return {
        'contextUrl': None,
        'documentUrl': url,
        'document': data
    }


def load_document(url):
    """
    :param url:
    :return:
    """
    result = validators.url(url)
    if result:
        response = requests.get(
            url, headers={'Accept': 'application/ld+json, application/json'}
        )
        return response.text
    raise InvalidUrlError('Could not validate ' + url)


def jsonld_document_loader(url):
    """
    Retrieves JSON-LD at the given URL. Propagates BlockcertValidationError is url is invalid
    or doesn't exist
    :param url: the URL to retrieve
    :return: JSON-LD at the URL
    """
    data = load_document(url)
    return to_loader_response(data, url)

# use this method prior to calling normalize_jsonld if you need to pass a specific context for normalization
def extend_preloaded_context(url, context):
    PRELOADED_CONTEXTS[url] = context
    pass

def preloaded_context_document_loader(url, override_cache=False):
    if url in PRELOADED_CONTEXTS:
        context = PRELOADED_CONTEXTS[url]
        return to_loader_response(context, url)
    else:
        return jsonld_document_loader(url)


def compact_with_json_ld_context(input_json, document_loader=preloaded_context_document_loader):
    options = {}
    if document_loader:
        options['documentLoader'] = document_loader
    with open(JSON_LD_CONTEXT_V1_2) as context_f:
        ctx = json.load(context_f)
        compacted = jsonld.compact(input_json, ctx, options=options)
        return compacted


def normalize_jsonld(json_ld_to_normalize, document_loader=preloaded_context_document_loader,
                     detect_unmapped_fields=False):
    """
    Canonicalize the JSON-LD certificate.

    The detect_unmapped_fields parameter is a temporary, incomplete, workaround to detecting fields that do not
    correspond to items in the JSON-LD schemas. It works in the Blockcerts context because:
    - Blockcerts doesn't use a default vocab
    - fallback.org is not expected to occur

    Because unmapped fields get dropped during canonicalization, this uses a trick of adding
     {"@vocab": "http://fallback.org/"} to the json ld, which will cause any unmapped fields to be prefixed with
     http://fallback.org/.

    If a @vocab is already there (i.e. an issuer adds this in their extensions), then tampering will change the
    normalized form, hence the hash of the certificate, so we will still detect this during verification.

    This issue will be addressed in a first-class manner in the future by the pyld library.

    :param json_ld_to_normalize:
    :param document_loader
    :param detect_unmapped_fields:
    :return:
    """
    json_ld = json_ld_to_normalize
    options = deepcopy(JSONLD_OPTIONS)
    if document_loader:
        options['documentLoader'] = document_loader

    if detect_unmapped_fields:
        json_ld = deepcopy(json_ld_to_normalize)
        prev_context = JsonLdProcessor.get_values(json_ld_to_normalize, '@context')
        add_fallback = True
        for pc in prev_context:
            if type(pc) is dict:
                for key, value in pc.items():
                    if key == '@vocab':
                        # this already has a vocab; unmapped fields will be detected in the hash
                        add_fallback = False
                        break
        if add_fallback:
            prev_context.append(FALLBACK_CONTEXT)
            json_ld['@context'] = prev_context

    normalized = jsonld.normalize(json_ld, options=options)

    if detect_unmapped_fields and FALLBACK_VOCAB in normalized:
        unmapped_fields = []
        for m in re.finditer('<http://fallback\.org/(.*)>', normalized):
            unmapped_fields.append(m.group(0))
        error_string = ', '.join(unmapped_fields)
        raise BlockcertValidationError(
            'There are some fields in the certificate that do not correspond to the expected schema. This has likely been tampered with. Unmapped fields are: ' + error_string)
    return normalized


if __name__ == '__main__':
    options = {}
    document_loader = preloaded_context_document_loader
    options['documentLoader'] = document_loader
    filename = '../examples/2.0/sample_valid-2.0.json'
    with open(filename) as data_f:
        data = json.load(data_f)
        compacted = compact_with_json_ld_context(data, document_loader)
        expanded = jsonld.expand(compacted, options=options)
        options = {'algorithm': 'URDNA2015', 'format': 'application/nquads'}
        if document_loader:
            options['documentLoader'] = document_loader
        normalized = jsonld.normalize(data, options)
        print(json.dumps(expanded, indent=2))
