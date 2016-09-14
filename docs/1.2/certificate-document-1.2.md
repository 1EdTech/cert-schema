# Certificate Document Version 1.2 Schema

The complete certificate document, including the assertion, certificate, and issuer. Doesn't include the blockchain receipt. This part is hashed and placed on the blockchain

The schema defines the following properties:

## `@type` (JsonLdType, required)

## `certificate` (Certificate, required)

## `assertion` (Assertion, required)

## `verify` (VerificationObject, required)

## `recipient` (Recipient, required)

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdType`

A type or an array of types that the document object represents. The first or only item should be 'CertificateDocument', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'CertificateDocument'

This property must be one of the following types:

* `string`
* `array`

## `Certificate` [Certificate](certificate-1.2.md)

## `Assertion` [Assertion](assertion-1.2.md)

## `VerificationObject` (object)

Properties of the `VerificationObject` object:

### `type` (string, enum)

This element must be one of the following enum values:

* `hosted`
* `signed`
* `ECDSA(secp256k1)`

### `url` (string)

## `Recipient` (object)

Properties of the `Recipient` object:

### `@type` (JsonLdType, required)

### `familyName` (string, required)

Family name of the recipient. http://schema.org/Person#familyName

### `identity` (string, required)

String that represents a recipient's identity. By default, it is an email address.

### `type` (string, required)

Type of value in the identity field. Default is 'email'.

### `hashed` (boolean, required)

Describes if the value in the identity field is hashed or not. We strongly recommend that the issuer hash the identy to protect the recipient. Backcompatible change to allow 2 types that occurred in the wild before proper validation.

### `salt` (string)

per the OBI standard, if the recipient identity is hashed, then this should contain the string used to salt the hash

### `pubkey` (string, required)

Bitcoin address (compressed public key, usually 24 characters) of the recipient.

### `givenName` (string, required)

Given name of the recipient. http://schema.org/Person#givenName