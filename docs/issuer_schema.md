## IssuerProfile schema

Blockcerts 2.0 Issuer Identification (Profile) schema. Extends [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile), a type that is embedded in an Open Badge and/or hosted at an issuer URI. Blockcerts specializes the Issuer Profile type into 2 schemas: the core that is embedded in the certificate (which matches the Open Badges Profile type), and one that is to be hosted at an issuer URI, to support blockchain verification of claims. This schema describes the latter. The issuer-hosted Profile is used in the Blockcerts verification process to look up the current list of public keys claimed by the issuer. This also defines an `introductionURL` which may be used by recipients (or software agents) to submit an introduction to the issuer. 

The schema defines the following additional properties to the Profile schema:

### `publicKeys` (array, required)

Array of CryptographicKey ([https://web-payments.org/vocabs/security#Key](https://web-payments.org/vocabs/security#Key)) references or objects. Entries may be dereferencable URIs of a document describing a CryptographicKey, or an embedded description of a CryptographicKey.

The elements of the array must match *at least one* of the following properties:

* `string`: Cryptographic key URI
    * Format: `uri`
* `CryptographicKey`

### `introductionURL` (string)

Blockcerts extension: URI where potential recipients (or their agents) should submit introductions, including recipient public key. If the issuer supports certificate wallet introductions, this field should specify the endpoint for use by certificate wallets. Otherwise, it can represent a URI enabling some other form of introduction; for example an HTTP IRI for a web form that to be filled out by the recipient.

Additional restrictions:

* Format: `uri`

### allOf (Profile)

The IssuerProfile schema includes all properties of the <a href="#profile">Profile schema</a>

### Required fields

*    `id`
*    `type`
*    `name`
*    `url`
*    `publicKeys`

---

# Sub Schemas


The schema defines the following additional types:

## `Profile`

Defined by [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile). This type is used in certificates, and in the issuer-hosted identification page. The minimal set of properties required in the certificate are `id` and `type`. In this case, additional issuer-identification properties are assumed to be available at the issuer-hosted identification page.

### `id` (string, required)

Defined by `id` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

Additional restrictions:

* Format: `uri`

### `type` (JsonLdType, required)

Defined by `type` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

### `name` (string)

Defined by `name` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

### `url` (string)

Defined by `url` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

Additional restrictions:

* Format: `uri`

### `telephone` (string)

Defined by `telephone` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

### `description` (string)

Defined by `description` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

### `image` (ImageUri)

Defined by `image` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

### `email` (string)

Defined by `email` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile)

### `revocationList` (string)

Defined by `revocationList` property of [https://w3id.org/openbadges#Profile](https://w3id.org/openbadges#Profile). If embedded in a Blockcert and the issuer-hosted Profile, the value in the Blockcert should take preference.

Additional restrictions:

* Format: `uri`


## `CryptographicKey` (object)

Defined by [https://web-payments.org/vocabs/security#Key](https://web-payments.org/vocabs/security#Key)

Properties of the `CryptographicKey` object:

### `publicKey` (string, required)

Issuer public key or blockchain address IRI with `<scheme>:` prefix. For Bitcoin transactions, this would be the issuer public address prefixed with `ecdsa-koblitz-pubkey:`; e.g. `ecdsa-koblitz-pubkey:14RZvYazz9H2DC2skBfpPVxax54g4yabxe`

Additional restrictions:

* Regex pattern: `^ecdsa-koblitz-pubkey:`

### `created` (DateTime, required)

### `expires` (DateTime)

### `revoked` (DateTime)

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

## `ImageUri` (string)

An image representative of the entity. In Blockcerts this is typically a data URI embedded as a base-64 encoded PNG image, but it may also be a URI where the image may be found.

This property may be any of the following types:

* `string`
  * Pattern: `^data:`
* `string`
  * Format: `uri`

## `ISODateTime` (string)

ISO 8601 date format string `yyyy-MM-dd'T'HH:mm:ss.SSS` with optional `.SSS` milliseconds

## `UNIXTimeStamp` (integer)

10-digit UNIX timestamp, epoch time

## `DateTime`

This property may be any of the following types:

* `ISODateTime`
* `UNIXTimeStamp`
