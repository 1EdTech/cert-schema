# Blockchain Certificates Version 1.2 Schema

A schema for representing certificates on the blockchain

The schema defines the following properties:

## `@context` (JsonLdContext, required)

## `type` (JsonLdType, required)

## `document` (CertificateDocument, required)

## `receipt` (BlockchainReceipt, required)

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdContext` (undefined)

A link to a valid JSON-LD context file, that maps term names to contexts. Blockchain Certificate contexts may also define JSON-schema to validate Blockchain Certificates against. In a Blockchain Certificate Object, this will almost always be a string:uri to a single context file, but might rarely be an array of links or context objects instead. This schema also allows direct mapping of terms to IRIs by using an object as an option within an array.

This property must be one of the following types:

* `string`
* `array`

## `JsonLdType` (undefined)

A type or an array of types that the Blockchain Certificate object represents. The first or only item should be 'BlockchainCertificate', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'BlockchainCertificate'

This property must be one of the following types:

* `string`
* `array`

## `CertificateDocument` (undefined)

## `BlockchainReceipt` (undefined)