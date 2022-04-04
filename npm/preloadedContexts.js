import CONTEXT_URLS from './schemas/context_urls.json';

import OPEN_BADGES_V2_CONTEXT from './schemas/2.1/obi.json';
import VERIFIABLE_CREDENTIALS_CONTEXT from './schemas/3.0/credential.json';

import V2_CONTEXT from './schemas/2.0/context.json';
import V2_1_CONTEXT from './schemas/2.1/context.json';
import V3_CONTEXT from './schemas/3.0/context.json';

const preloadedContexts = {};

preloadedContexts[CONTEXT_URLS.OPEN_BADGES_V2_CANONICAL_CONTEXT] = OPEN_BADGES_V2_CONTEXT;
preloadedContexts[CONTEXT_URLS.OPEN_BADGES_V2_CONTEXT] = OPEN_BADGES_V2_CONTEXT;

preloadedContexts[CONTEXT_URLS.VERIFIABLE_CREDENTIAL_V1_CONTEXT] = VERIFIABLE_CREDENTIALS_CONTEXT;

preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_CONTEXT] = V2_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_ORG_V2_CONTEXT] = V2_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_CANONICAL_CONTEXT] = V2_CONTEXT;

preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_1_CONTEXT] = V2_1_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_ORG_V2_1_CONTEXT] = V2_1_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_1_CANONICAL_CONTEXT] = V2_1_CONTEXT;

preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V3_CONTEXT] = V3_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_ORG_V3_CONTEXT] = V3_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V3_CANONICAL_CONTEXT] = V3_CONTEXT;

export default preloadedContexts;
