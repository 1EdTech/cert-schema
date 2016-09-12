[![Build Status](https://travis-ci.org/blockchain-certificates/cert-schema.svg?branch=master)](https://travis-ci.org/blockchain-certificates/cert-schema)
[![PyPI version](https://badge.fury.io/py/cert-schema.svg)](https://badge.fury.io/py/cert-schema)

# cert-schema


The cert-schema project describes how to make a digital certificate. A digital certificate is essentially a JSON file with
the necessary fields needed for our issuer code to place it on the blockchain. We tried to keep the schema as close to
 the [Mozilla Open Badges](http://openbadges.org/) specifications as possible.


## Certificate schema

- [Certificate Schema V1](/docs/certificate-schema-v1-1.md)
- [Issuer Schema V1](/docs/certificate-schema-v1-1.md)

## JSON schema
- [Certificate JSON Schema V1](/schema/certificate-schema-v1-1.json)
- [Issuer JSON Schema V1](/schema/certificate-schema-v1-1.json)

## Examples
- [Example certificates](/docs/examples.md)


## Compile markdown from schema
`scripts/generate_markdown.js` builds the markdown-formatted schemas from json

## Publishing package to pypi
- [First time info](http://peterdowns.com/posts/first-time-with-pypi.html)
- Publish script: `./release_package.sh`


## Contact

Contact [certs@mit.edu](mailto:certs@media.mit.edu) with questions


