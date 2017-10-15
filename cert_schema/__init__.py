SECURITY_CONTEXT_URL = 'https://w3id.org/security/v1'
OPEN_BADGES_V2_CONTEXT = 'https://openbadgespec.org/v2/context.json'
OPEN_BADGES_V2_CANONICAL_CONTEXT = 'https://w3id.org/openbadges/v2'
BLOCKCERTS_V2_ALPHA_CONTEXT = 'https://w3id.org/blockcerts/schema/2.0-alpha/context.json'
BLOCKCERTS_V2_ALPHA_SCHEMA = 'https://w3id.org/blockcerts/schema/2.0-alpha/schema.json'
BLOCKCERTS_V2_CONTEXT = 'https://w3id.org/blockcerts/schema/2.0/context.json'
BLOCKCERTS_V2_SCHEMA = 'https://w3id.org/blockcerts/schema/2.0/schema.json'
BLOCKCERTS_V2_CANONICAL_CONTEXT = 'https://w3id.org/blockcerts/v2'
BLOCKCERTS_VOCAB = 'https://w3id.org/blockcerts/v2#'


class BlockcertValidationError(Exception):
    pass


class InvalidUrlError(Exception):
    pass


from cert_schema.jsonld_helpers import JSONLD_OPTIONS
from cert_schema.jsonld_helpers import jsonld_document_loader
from cert_schema.jsonld_helpers import normalize_jsonld
from cert_schema.schema_validator import validate_unsigned_v1_2, validate_v1_2, validate_v2
