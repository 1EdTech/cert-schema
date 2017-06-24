## Assertion schema

Blockcerts 2.0 Assertion schema. Extends Open Badges v2.0 schema: [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

The schema defines the following properties:

### `id` (string, required)

Defined by `id` property in [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion). This may be an HTTP IRI, but only if the issuer plans to host the assertions on a long-term basis, or (at least) until their expiration. Otherwise it is recommended to use a `urn:uuid:<UUID>`-formatted IRI.

The object may be any of the following types:

* `string`
  * Pattern: `^urn:uuid:`
* `string`
  * Format: `uri`

### `type` (JsonLdType, required)

Defined by `type` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

### `recipient` (IdentityObject, required)

Defined by `recipient` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion), with Blockcerts extensions for recipient proof of ownership.

### `badge` (BadgeClass, required)

Defined by `badge` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion), with Blockcerts extensions for (display) signature images.

### `verification` (VerificationObject, required)

Defined by `verification` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion), with Blockcerts extensions for verification of badges on a blockchain.

### `issuedOn` (DateTime, required)

Defined by `issuedOn` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

### `image` (ImageUri)

Defined by `image` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

### `evidence` (string)

Defined by `evidence` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

Additional restrictions:

* Format: `uri`

### `narrative` (string)

Defined by `narrative` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

### `expires` (DateTime)

Defined by `expires` property of [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

### `signature` (MerkleProof2017)

Blockcerts extension [MerkleProof2017](merkleProofSignatureExtension_schema.html)


---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdContext`

A link to a valid JSON-LD context, or array of JSON-LD contexts

This property must be one of the following types:

* `string`
* `array`

## `JsonLdType`

A type or an array of types defined in a referenced JSON-LD context.

This property must be one of the following types:

* `string`
* `array`

## `ISODateTime` (string)

ISO 8601 date format string `yyyy-MM-dd'T'HH:mm:ss.SSS` with optional `.SSS` milliseconds

## `UNIXTimeStamp` (integer)

10-digit UNIX timestamp, epoch time

## `DateTime`

This property may be any of the following types:

* `ISODateTime`
* `UNIXTimeStamp`

## `HashString` (string)

Open Badges SHA-256 Hash

## `IdentityObject` (object)

From [https://w3id.org/openbadges#IdentityObject](https://w3id.org/openbadges#IdentityObject), with extensions for recipient profile.

Properties of the `IdentityObject` object:

### `identity` (object, required)

Defined by `identity` property of [https://w3id.org/openbadges#IdentityObject](https://w3id.org/openbadges#IdentityObject)

### `type` (string, enum, required)

Defined by `type` property of [https://w3id.org/openbadges#IdentityObject](https://w3id.org/openbadges#IdentityObject)

This element must be one of the following enum values:

* `email`

### `hashed` (boolean, required)

Defined by `hashed` property of [https://w3id.org/openbadges#IdentityObject](https://w3id.org/openbadges#IdentityObject)

### `salt` (object)

Defined by `salt` property of [https://w3id.org/openbadges#IdentityObject](https://w3id.org/openbadges#IdentityObject)

### `recipientProfile` (RecipientProfile)

Blockcerts extension: [RecipientProfile](recipientProfileExtension_schema.html), allowing the recipient to prove ownership.

## `VerificationObject` (object)

From [https://w3id.org/openbadges#VerificationObject](https://w3id.org/openbadges#VerificationObject), with extensions for Blockcerts verification

Properties of the `VerificationObject` object:

### `type` (JsonLdType, required)

Defined by `type` property of [https://w3id.org/openbadges#VerificationObject](https://w3id.org/openbadges#VerificationObject). Blockcerts extension: this should contain the entry `MerkleProofVerification2017`

### `creator` (string)

Blockcerts extension: the expected blockchain address for the signer of the transaction containing the merkle proof. In Blockcerts `creator` IRIs are typically represented with a `<scheme>:` prefix. For Bitcoin transactions, this would be the issuer public Bitcoin address prefixed with `ecdsa-koblitz-pubkey:`; e.g. `ecdsa-koblitz-pubkey:14RZvYazz9H2DC2skBfpPVxax54g4yabxe`

The object may be any of the following types:

* `string`
  * Pattern: `^ecdsa-koblitz-pubkey:`
  * Description: Issuer public key or blockchain address with `<scheme>:` prefix. For Bitcoin transactions, this would be the issuer public address prefixed with `ecdsa-koblitz-pubkey:`. Example: `ecdsa-koblitz-pubkey:14RZvYazz9H2DC2skBfpPVxax54g4yabxe`
* `string`
  * Format: `uri`

### `verificationProperty` (object)

Defined by `verificationProperty` property of [https://w3id.org/openbadges#VerificationObject](https://w3id.org/openbadges#VerificationObject)

### `startsWith` (string)

Defined by `startsWith` property of [https://w3id.org/openbadges#VerificationObject](https://w3id.org/openbadges#VerificationObject)

Additional restrictions:

* Format: `uri`

### `allowedOrigins` (string)

Defined by `allowedOrigins` property of [https://w3id.org/openbadges#VerificationObject](https://w3id.org/openbadges#VerificationObject)

Additional restrictions:

* Format: `uri`

## `ImageUri` (string)

An image representative of the entity. In Blockcerts this is typically a data URI ([https://en.wikipedia.org/wiki/Data_URI_scheme](https://en.wikipedia.org/wiki/Data_URI_scheme)) embedded as a base-64 encoded PNG image, but it may also be a URI where the image may be found.

This property may be any of the following types:

* `string`
  * Pattern: `^data:`
* `string`
  * Format: `uri`

## `AlignmentObject` (object)

From [https://w3id.org/openbadges#AlignmentObject](https://w3id.org/openbadges#AlignmentObject)

Properties of the `AlignmentObject` object:

### `targetName` (string, required)

Defined by `targetName` property of [https://w3id.org/openbadges#AlignmentObject](https://w3id.org/openbadges#AlignmentObject)

### `targetUrl` (string, required)

Defined by `targetUrl` property of [https://w3id.org/openbadges#AlignmentObject](https://w3id.org/openbadges#AlignmentObject)

Additional restrictions:

* Format: `uri`

### `targetDescription` (string)

Defined by `targetDescription` property of [https://w3id.org/openbadges#AlignmentObject](https://w3id.org/openbadges#AlignmentObject)

## `BadgeClass` (object)

From [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass)

Properties of the `BadgeClass` object:

### `id` (string)

Defined by `id` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass). This field is required in Open Badges but currently optional in Blockcerts for compatibility. This may be an HTTP IRI, but only if the issuer plans to host the BadgeClass definitions on a long-term basis, or (at least) until expiration of certificates referencing this BadgeClass. Otherwise it is recommended to use a `urn:uuid:<UUID>`-formatted IRI.

Additional restrictions:

* Format: `uri`

### `type` (JsonLdType)

Defined by `type` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass)

### `name` (string, required)

Defined by `name` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass)

### `subtitle` (string)

Blockcerts extension: optional subtitle of the certificate

### `description` (string, required)

Defined by `description` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass)

### `image` (ImageUri, required)

Defined by `image` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass)

### `criteria` (object)

Defined by `criteria` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass). This field is required in Open Badges, currently optional in Blockcerts for compatibility. 

### `issuer` (Profile, required)

Defined by `issuer` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass), with Blockcerts extensions for blockchain verification of badges.

[Profile schema](issuer_schema.html)


### `alignment` (AlignmentArray)

Defined by `alignment` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass)

### `tags` (TagsArray)

Defined by `tags` property of [https://w3id.org/openbadges#BadgeClass](https://w3id.org/openbadges#BadgeClass)

### `signatureLines` (object)

Blockcerts extension: array of [SignatureLine](signatureLineExtension_schema.html), for display in the certificate.

