Blockchain Certificates cert-schema project
========================================

The cert-schema project describes how to make a digital certificate. A digital certificate is essentially a JSON file with
the necessary fields needed for our issuer code to place it on the blockchain. We tried to keep the schema as close to
 the [Mozilla Open Badges](http://openbadges.org/) specifications as possible.


###Certificate schema

- [Certificate Schema V1](/docs/certificate-schema-v1-1.md)
- [Issuer Schema V1](/docs/certificate-schema-v1-1.md)

###JSON schema
- [Certificate JSON Schema V1](/schema/certificate-schema-v1-1.json)
- [Issuer JSON Schema V1](/schema/certificate-schema-v1-1.json)

###Examples
- [Example certificates](/docs/examples.md)


###Compile markdown from schema
`scripts/generate_markdown.js` builds the markdown-formatted schemas from json

### Publishing package to pypi
- [First time info](http://peterdowns.com/posts/first-time-with-pypi.html)
- Publish script: `./release_package.sh`

Read The Docs
-------------
Cert-schema's [Read The Docs](http://cert-schema.readthedocs.io/) documentation -- a nicer display of the content here.

Disclaimer
--------------------------

[MIT Media Lab Blockchain Certificates](http://www.blockcerts.org/) is an incubation project. We're looking for feedback, contributions, and general
discussion. This is not currently intended for production release, but we are improving our approach for future releases.

Contact
-------

Contact [certs@media.mit.edu](mailto:certs@media.mit.edu) with questions


