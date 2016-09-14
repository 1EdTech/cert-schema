# Blockchain Certificates Version 1.2 Schema

A schema for representing certificates on the blockchain

The schema defines the following properties:

## `@context` (JsonLdContext, required)

## `@type` (JsonLdType, required)

## `document` (CertificateDocument, required)

## `receipt` (BlockchainReceipt, required)

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdContext`

A link to a valid JSON-LD context file, that maps term names to contexts. Blockchain certificates contexts extend Open Badges contexts, and also define JSON-schema to validate blockchain certificates against.

This property must be one of the following types:

* `string`
* `array`

## `JsonLdType` (undefined)

A type or an array of types that the blockchain certificate object represents. The first or only item should be 'BlockchainCertificate', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'BlockchainCertificate'

This property must be one of the following types:

* `string`
* `array`

## `CertificateDocument` [CertificateDocument](certificate-document-1.2.md)

## `BlockchainReceipt` [BlockchainReceipt](blockchain-receipt-1.2.md)