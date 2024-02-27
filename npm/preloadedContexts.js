import CONTEXT_URLS from './schemas/context_urls.json' assert { type: 'json' };

import OPEN_BADGES_V2_CONTEXT from './schemas/2.1/obi.json' assert { type: 'json' };
import VERIFIABLE_CREDENTIALS_CONTEXT from './schemas/3.0/credential.json' assert { type: 'json' };
import VERIFIABLE_CREDENTIALS_V2_CONTEXT from './schemas/3.2/credential_v2.json' assert { type: 'json' };

import V2_CONTEXT from './schemas/2.0/context.json' assert { type: 'json' };
import V2_1_CONTEXT from './schemas/2.1/context.json' assert { type: 'json' };
import V3_CONTEXT from './schemas/3.0/context.json' assert { type: 'json' };
import V3_1_CONTEXT from './schemas/3.1/context.json' assert { type: 'json' };
import MERKLE_PROOF_2019_CONTEXT from './schemas/3.1/merkleProof2019Context.json' assert { type: 'json' };
import CHAINED_PROOF_2021_CONTEXT from './schemas/3.1/chainedProof2021Context.json' assert { type: 'json' };
import STATUS_LIST_2021_CONTEXT from './schemas/3.1/statusList2021Context.json' assert { type: 'json' };
import DATA_INTEGRITY_PROOF_V2_CONTEXT from './schemas/3.2/dataIntegrityProof.json' assert { type: 'json' };

const preloadedContexts = {};

preloadedContexts[CONTEXT_URLS.OPEN_BADGES_V2_CANONICAL_CONTEXT] = OPEN_BADGES_V2_CONTEXT;
preloadedContexts[CONTEXT_URLS.OPEN_BADGES_V2_CONTEXT] = OPEN_BADGES_V2_CONTEXT;

preloadedContexts[CONTEXT_URLS.VERIFIABLE_CREDENTIAL_V1_CONTEXT] = VERIFIABLE_CREDENTIALS_CONTEXT;
preloadedContexts[CONTEXT_URLS.VERIFIABLE_CREDENTIAL_V2_CONTEXT] = VERIFIABLE_CREDENTIALS_V2_CONTEXT;

preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_CONTEXT] = V2_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_ORG_V2_CONTEXT] = V2_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_CANONICAL_CONTEXT] = V2_CONTEXT;

preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_1_CONTEXT] = V2_1_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_ORG_V2_1_CONTEXT] = V2_1_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V2_1_CANONICAL_CONTEXT] = V2_1_CONTEXT;

preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V3_CONTEXT] = V3_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_ORG_V3_CONTEXT] = V3_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V3_CANONICAL_CONTEXT] = V3_CONTEXT;

preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V3_1_CONTEXT] = V3_1_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_ORG_V3_1_CONTEXT] = V3_1_CONTEXT;
preloadedContexts[CONTEXT_URLS.BLOCKCERTS_V3_1_CANONICAL_CONTEXT] = V3_1_CONTEXT;
preloadedContexts[CONTEXT_URLS.MERKLE_PROOF_2019_CONTEXT] = MERKLE_PROOF_2019_CONTEXT;
preloadedContexts[CONTEXT_URLS.CHAINED_PROOF_2021_CONTEXT] = CHAINED_PROOF_2021_CONTEXT;
preloadedContexts[CONTEXT_URLS.STATUS_LIST_2021_CONTEXT] = STATUS_LIST_2021_CONTEXT;
preloadedContexts[CONTEXT_URLS.DATA_INTEGRITY_PROOF_V2_CONTEXT] = DATA_INTEGRITY_PROOF_V2_CONTEXT;

export default preloadedContexts;
