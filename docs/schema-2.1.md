## Assertion schema

Blockcerts 2.1 Assertion schema. Extends Open Badges v2.0 schema: [https://w3id.org/openbadges#Assertion](https://w3id.org/openbadges#Assertion)

The schema defines the following properties:

### `id` (string, required)

Defined by `id` property in https://w3id.org/openbadges#Assertion. This may be an HTTP IRI, but only if the issuer plans to host the assertions on a long-term basis, or (at least) until their expiration. Otherwise it is recommended to use a `urn:uuid:<UUID>`-formatted IRI.

### `type` (JsonLdType, required)

Defined by `type` property of https://w3id.org/openbadges#Assertion

### `recipient` (IdentityObject, required)

Defined by `recipient` property of https://w3id.org/openbadges#Assertion, with Blockcerts extensions for recipient proof of ownership.

### `badge` (BadgeClass, required)

Defined by `badge` property of https://w3id.org/openbadges#Assertion, with Blockcerts extensions for (display) signature images.

### `verification` (VerificationObject, required)

Defined by `verification` property of https://w3id.org/openbadges#Assertion, with Blockcerts extensions for verification of badges on a blockchain.

### `issuedOn` (DateTime, required)

Defined by `issuedOn` property of https://w3id.org/openbadges#Assertion

### `image` (ImageUri)

Defined by `image` property of https://w3id.org/openbadges#Assertion

### `evidence` (string)

Defined by `evidence` property of https://w3id.org/openbadges#Assertion

### `narrative` (string)

Defined by `narrative` property of https://w3id.org/openbadges#Assertion

### `expires` (DateTime)

Defined by `expires` property of https://w3id.org/openbadges#Assertion

### `recipientProfile` (RecipientProfile)

### `signature` (MerkleProof2017)



## Sub Schemas

The schema defines the following additional types:

### `JsonLdContext` (undefined)

A link to a valid JSON-LD context, or array of JSON-LD contexts

This property must be one of the following types:

* `string`
* `array`

### `JsonLdType` (undefined)

A type or an array of types defined in a referenced JSON-LD context.

This property must be one of the following types:

* `string`
* `array`

## `DateTime` (string)
#
Open Badges must express timestamps as strings compatible with ISO 8601 guidelines, including the time and a time zone indicator. It is recommended to publish all timestamps in UTC. Previous versions of Open Badges allowed Unix timestamps as integers. Open Badges v2.0 requires string ISO 8601 values with time zone indicators. For example, 2016-12-31T23:59:59+00:00 is a valid ISO 8601 timestamp. It contains the year, month, day, T separator, hour number 0-23, minute, optional seconds and decimal microsecond, and a time zone indicator (+/- an offset from UTC or the Z designator for UTC).

### `HashString` (string)

Open Badges SHA-256 Hash

### `IdentityObject` (object)

From https://w3id.org/openbadges#IdentityObject.

Properties of the `IdentityObject` object:

#### `identity` (, required)

Defined by `identity` property of https://w3id.org/openbadges#IdentityObject

The object must be one of the following types:

* `HashString`
* `undefined`

#### `type` (string, enum, required)

Defined by `type` property of https://w3id.org/openbadges#IdentityObject

This element must be one of the following enum values:

* `email`

#### `hashed` (boolean, required)

Defined by `hashed` property of https://w3id.org/openbadges#IdentityObject

#### `salt`

Defined by `salt` property of https://w3id.org/openbadges#IdentityObject

### `VerificationObject` (object)

From https://w3id.org/openbadges#VerificationObject, with extensions for Blockcerts verification

Properties of the `VerificationObject` object:

#### `type` (JsonLdType, required)

Defined by `type` property of https://w3id.org/openbadges#VerificationObject. Blockcerts extension: this should contain the entry `MerkleProofVerification2017`

#### `publicKey` (string)

Blockcerts extension: the expected blockchain address for the signer of the transaction containing the merkle proof. In Blockcerts `publicKey`s are typically represented with a `<scheme>:` prefix. For Bitcoin transactions, this would be the issuer public Bitcoin address prefixed with `ecdsa-koblitz-pubkey:`; e.g. `ecdsa-koblitz-pubkey:14RZvYazz9H2DC2skBfpPVxax54g4yabxe`

### `ImageUri` (string)

An image representative of the entity. In Blockcerts this is typically a data URI (https://en.wikipedia.org/wiki/Data_URI_scheme) embedded as a base-64 encoded PNG image, but it may also be a URI where the image may be found.

### `AlignmentObject` (object)

From https://w3id.org/openbadges#AlignmentObject

Properties of the `AlignmentObject` object:

#### `targetName` (string, required)

Defined by `targetName` property of https://w3id.org/openbadges#AlignmentObject

### `targetUrl` (string, required)

Defined by `targetUrl` property of https://w3id.org/openbadges#AlignmentObject

#### `targetDescription` (string)

Defined by `targetDescription` property of https://w3id.org/openbadges#AlignmentObject

### `AlignmentArray` (array)

List of objects describing which objectives or educational standards this badge aligns to, if any.

### `TagsArray` (array)

List of tags that describe the type of achievement.

### `SignatureLine` (undefined)

### `RecipientProfile` (undefined)

### `MerkleProof2017` (undefined)

### `BadgeClass` (object)

From https://w3id.org/openbadges#BadgeClass

Properties of the `BadgeClass` object:

#### `id` (string, required)

Defined by `id` property of https://w3id.org/openbadges#BadgeClass. This field is now required in V2. This may be an HTTP IRI, but only if the issuer plans to host the BadgeClass definitions on a long-term basis, or (at least) until expiration of certificates referencing this BadgeClass. Otherwise it is recommended to use a `urn:uuid:<UUID>`-formatted IRI.

#### `type` (JsonLdType)

Defined by `type` property of https://w3id.org/openbadges#BadgeClass

#### `name` (string, required)

Defined by `name` property of https://w3id.org/openbadges#BadgeClass

#### `subtitle` (string)

Blockcerts extension: optional subtitle of the certificate

#### `description` (string, required)

Defined by `description` property of https://w3id.org/openbadges#BadgeClass

#### `image` (ImageUri, required)

Defined by `image` property of https://w3id.org/openbadges#BadgeClass

#### `criteria` (object, required)

Defined by `criteria` property of https://w3id.org/openbadges#BadgeClass. This field is required in Open Badges. If migrating from an earlier version, a quick change is to reuse the `description` field

#### `issuer` (Profile, required)

Defined by `issuer` property of https://w3id.org/openbadges#BadgeClass, with Blockcerts extensions for blockchain verification of badges.

#### `alignment` (AlignmentArray)

Defined by `alignment` property of https://w3id.org/openbadges#BadgeClass

#### `tags` (TagsArray)

Defined by `tags` property of https://w3id.org/openbadges#BadgeClass

#### `signatureLines`

Blockcerts extension: array of signature lines for display.

### `Profile` (undefined)

Defined by https://w3id.org/openbadges#Profile. This type is used in certificates, and in the issuer-hosted identification page. The minimal set of properties required in the certificate are `id` and `type`. In this case, additional issuer-identification properties are assumed to be available at the issuer-hosted identification page.

#### `id` (string, required)

Defined by `id` property of https://w3id.org/openbadges#Profile

#### `type` (JsonLdType, required)

Defined by `type` property of https://w3id.org/openbadges#Profile

#### `name` (string)

Defined by `name` property of https://w3id.org/openbadges#Profile

#### `url` (string)

Defined by `url` property of https://w3id.org/openbadges#Profile

#### `telephone` (string)

Defined by `telephone` property of https://w3id.org/openbadges#Profile

#### `description` (string)

Defined by `description` property of https://w3id.org/openbadges#Profile

#### `image` (ImageUri)

Defined by `image` property of https://w3id.org/openbadges#Profile

#### `email` (string)

Defined by `email` property of https://w3id.org/openbadges#Profile

#### `revocationList`

Defined by `revocationList` property of https://w3id.org/openbadges#Profile. If embedded in a Blockcert and the issuer-hosted Profile, the value in the Blockcert should take preference.