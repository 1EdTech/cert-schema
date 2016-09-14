[![Build Status](https://travis-ci.org/blockchain-certificates/cert-schema.svg?branch=master)](https://travis-ci.org/blockchain-certificates/cert-schema)
[![PyPI version](https://badge.fury.io/py/cert-schema.svg)](https://badge.fury.io/py/cert-schema)

# cert-schema

The cert-schema project contains the Blockchain Certificate JSON schema and JSON LD specification.
These are extensions to [Open Badges](http://openbadges.org/) schemas allowing the entire
certificate contents to be registered and verified on a blockchain.

The cert-schema python package allows verification of a Blockchain Certificate against the JSON
schemas. This is not the same as validating the contents of a certificate against what is stored
on the blockchain. See the cert-verifier project.


## JSON LD

- [Certificate JSON LD](cert_schema/schema/certificate/1.2/context.json)

## JSON Schema Markdown

- [Blockchain Certificate JSON Schema](docs/1.2/blockchain-certificate-1.2.md)
  - [Certificate Document JSON Schema](docs/1.2/certificate-document-1.2.md)  
    - [Assertion JSON Schema](docs/1.2/assertion-1.2.md)
    - [Certificate JSON Schema](docs/1.2/certificate-1.2.md)
        - [Issuer JSON Schema](docs/1.2/issuer-1.2.md) 
  - [Blockchain Receipt JSON Schema](docs/1.2/blockchain-receipt-1.2.md)

## JSON Schema Raw

- [Blockchain Certificate JSON Schema](cert_schema/schema/certificate/1.2/blockchain-certificate-1.2.json)
  - [Certificate Document JSON Schema](cert_schema/schema/certificate/1.2/certificate-document-1.2.json)  
    - [Assertion JSON Schema](cert_schema/schema/certificate/1.2/assertion-1.2.json)
    - [Certificate JSON Schema](cert_schema/schema/certificate/1.2/certificate-1.2.json)
        - [Issuer JSON Schema](cert_schema/schema/certificate/1.2/issuer-1.2.json) 
  - [Blockchain Receipt JSON Schema](cert_schema/schema/certificate/1.2/blockchain-receipt-1.2.json)


## Compile markdown from schema
`scripts/generate_markdown.js` builds the markdown-formatted schemas from json

## Publishing package to pypi
- [First time info](http://peterdowns.com/posts/first-time-with-pypi.html)
- Publish script: `./release_package.sh`


## Contact

Contact [certs@mit.edu](mailto:certs@mit.edu) with questions

