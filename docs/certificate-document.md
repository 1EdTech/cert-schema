## Certificate Document Schema Version 1.2

The complete certificate document, including the assertion, certificate, and issuer. Doesn’t include the blockchain receipt. This part is hashed and placed on the blockchain

The schema defines the following properties:

### `@context` (JsonLdContext)

A link to a valid JSON-LD context file, that maps term names to contexts. Blockchain Certificate contexts may also define JSON-schema to validate Blockchain Certificates against. In a Blockchain Certificate Object, this will almost always be a string:uri to a single context file, but might rarely be an array of links or context objects instead. This schema also allows direct mapping of terms to IRIs by using an object as an option within an array.

This property must be one of the following types:

*   `string`
*   `array`

### `type` (JsonLdType, required)

A type or an array of types that the Blockchain Certificate object represents. The first or only item should be ‘CertificateDocument’, and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: ‘CertificateDocument’

This property must be one of the following types:

*   `string`
*   `array`

### `certificate` (Certificate, required)

[Certificate](certificate-schema.html)

### `assertion` (Assertion, required)

[Assertion](assertion-schema.html)

### `verify` (VerificationObject, required)

V1.2 notice: the Blockchain Certificates VerificationObject will change in the next schema version to be consistent with OBI VerificationObjects. This work is in progress.

Properties of the `VerificationObject` object:

`attribute-signed` (string, required)

Name of the attribute in the json that is signed by the issuer’s private key. Default is ‘uid’, referring to the uid attribute.

`type` (string, enum, required)

Name of the signing method. Default is ‘ECDSA(secp256k1)’, referring to the Blockchain Certificates method of signing messages with the issuer’s private key.

This element must be one of the following enum values:

*   `hosted`
*   `signed`
*   `ECDSA(secp256k1)`

`signer` (string)

URI where issuer’s public key is presented. Default is https://[domain]/keys/[org-abbr]-certs-public-key.asc. V1.2 change: this field is optional

### `recipient` (Recipient, required)

Properties of the `Recipient` object:

`familyName` (string, required)

Family name of the recipient. http://schema.org/Person#familyName

`identity` (string, required)

String that represents a recipient’s identity. By default, it is an email address.

`type` (string, required)

Type of value in the identity field. Default is ‘email’.

`hashed` (boolean, required)

Describes if the value in the identity field is hashed or not. We strongly recommend that the issuer hash the identy to protect the recipient.

`salt` (string)

per the OBI standard, if the recipient identity is hashed, then this should contain the string used to salt the hash

`publicKey` (string, required)

Bitcoin address (compressed public key, usually 24 characters) of the recipient. V1.2 change: renamed from pubkey

`revocationKey` (string)

Issuer revocation key for the recipient, optional. Bitcoin address (compressed public key, usually 24 characters) of the recipient.

`givenName` (string, required)

Given name of the recipient. http://schema.org/Person#givenName
