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

In 1.2 we've added a JSON LD schema to provide semantically rich linked data.

[Certificate JSON LD](cert_schema/schema/1.2/context.json)

## JSON Schema Raw

- [Blockchain Certificate JSON Schema](cert_schema/schema/1.2/blockchain-certificate-1.2.json)
  - [Certificate Document JSON Schema](cert_schema/schema/1.2/certificate-document-1.2.json)  
    - [Assertion JSON Schema](cert_schema/schema/1.2/assertion-1.2.json)
    - [Certificate JSON Schema](cert_schema/schema/1.2/certificate-1.2.json)
        - [Issuer JSON Schema](cert_schema/schema/1.2/issuer-1.2.json) 
  - [Blockchain Receipt JSON Schema](cert_schema/schema/1.2/blockchain-receipt-1.2.json)
- [Issuer Identification JSON Schema](cert_schema/schema/1.2/issuer-id-1.2.json)


## Running the python code locally

1. Ensure you have an python environment. [Recommendations](https://github.com/blockchain-certificates/developer-common-docs/blob/master/virtualenv.md)

2. Git clone the repository and change to the directory

  ```bash
  git clone https://github.com/blockchain-certificates/cert-schema.git && cd cert-schema
  ```

3. Run cert-schema setup

  ```bash
  pip install .
  ```


## Publishing package to pypi

- [First time info](http://peterdowns.com/posts/first-time-with-pypi.html)
- Publish script: `./release_package.sh`



## Unit tests

This project uses tox to validate against several python environments.

1. Ensure you have an python environment. [Recommendations](https://github.com/blockchain-certificates/developer-common-docs/blob/master/virtualenv.md)

2. Run tests
    ```
    ./run_tests.sh
    ```


## Compile markdown from schema

Note that json-schema-to-markdown doesn't handle ref schemas well, so you will 
need to manually update any 'undefined' references.

`scripts/generate_markdown.js` builds the markdown-formatted schemas from json

## Contact

Contact [info@blockcerts.org](mailto:info@blockcerts.org) with questions

