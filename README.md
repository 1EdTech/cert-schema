[![Build Status](https://travis-ci.org/blockchain-certificates/cert-schema.svg?branch=master)](https://travis-ci.org/blockchain-certificates/cert-schema)
[![PyPI version](https://badge.fury.io/py/cert-schema.svg)](https://badge.fury.io/py/cert-schema)

# cert-schema

Blockchain Certificate schemas implement those of [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/). As with Verifiable Credentials, we've provided both a JSON-LD context and JSON schema. The purpose of the JSON-LD context is to map types to Internationalized Resource Identifiers (IRIs), providing semantic context for data. The JSON Schema is used for syntactic validation.

This python package allows verification of a Blockchain Certificate against the JSON
schemas as a convenience. This is not the same as verifying the contents of a certificate against what is stored
on the blockchain. See the [cert-verifier-js](https://github.com/blockchain-certificates/cert-verifier-js) project.

*   [Blockcerts JSON Schema](docs/schema-3.0-alpha.md)

## Example

TODO update for V3 once cert-issuer issues one

The following is a Blockchain Certificate issued on the testnet Bitcoin network.

```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.blockcerts.org/schema/3.0-alpha/context.json",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
  "id": "urn:uuid:bbba8553-8ec1-445f-82c9-a57251dd731c",
  "type": [
    "VerifiableCredential"
  ],
  "issuer": "did:example:23adb1f712ebc6f1c276eba4dfa",
  "issuanceDate": "2010-01-01T19:73:24Z",
  "credentialSubject": {
    "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
    "alumniOf": {
      "id": "did:example:c276e12ec21ebfeb1f712ebc6f1"
    }
  },
  "signature": {
    "type": "MerkleProof2019",
    "created": "2020-01-21T12:32:11.693759",
    "proofValue": "z2LuLBVSfnVzaQtvzuA7EaPQsGEgYWeaMTH1p3uqAG3ESx9HYyFzFFrYsyPkZSbn1Ji5LN76jw6HBr3oiaa8KsQenCPqKk7dJvxEXsDnYvhuDHtsrSRbzHdJKd66jAowkzPxPFi3ivyAv7WRK1WV2VhegYVQEnCBTrGJWFUMFFXunTcus7ZyedQvS4sr61X2y8QuJ57ycB5JMEHvUgAVq3qh2g3ucehg2ERKLo98jmqTcsh9HThkECG3BTNYRD3QL7AHWPjxRbQNSA83QNYXcCNA7NaZnCWyjC17ZBj3xszp76XvqFRrLjQbRSbzjVTPtBSV8QjhxThT3KTfgwjRn5JeeXhYvebsTT9YGL3W4ufzFRDpH79n5KPiaj1BPbEUfUq7vf2dg26QWeZBi7ME56",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "ecdsa-koblitz-pubkey:0x7e30a37763e6Ba1fFeDE1750bBeFB4c60b17a1B3"
  }
}
```

## Publishing package to pypi

- [First time info](https://web.archive.org/web/20180501071551/http://peterdowns.com/posts/first-time-with-pypi.html)
- Publish script: `./release_package.sh`


## Unit tests

This project uses tox to validate against several python environments.

1. Ensure you have an python environment. [Recommendations](https://github.com/blockchain-certificates/cert-issuer/blob/master/docs/virtualenv.md)

2. Run tests
    ```
    ./run_tests.sh
    ```


## Compile markdown from schema

Note that json-schema-to-markdown doesn't handle ref schemas well, so you will 
need to manually update any 'undefined' references.

`scripts/generate_markdown.js` builds the markdown-formatted schemas from json

## Contact

Contact us at [the Blockcerts community forum](http://community.blockcerts.org/).

