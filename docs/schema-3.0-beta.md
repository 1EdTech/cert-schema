# Blockcerts Credential schema

Blockcerts 3.0 Credential schema. Implements Verifiable Credential v1.0 schema: https://www.w3.org/TR/vc-data-model/

The schema defines the following properties:

## `id` (string, required)

Defined by `id` property in https://www.w3.org/TR/vc-data-model/#identifiers.

## `type` (JsonLdType, required)

Defined by `type` property of https://www.w3.org/TR/vc-data-model/#types

## `issuer` (Issuer, required)

Defined by `issuer` property of https://www.w3.org/TR/vc-data-model/#issuer.

## `issuanceDate` (DateTime, required)

Defined by `issuanceDate` property of https://www.w3.org/TR/vc-data-model/#issuance-date.

## `credentialSubject` (object, required)

Defined by `credentialSubject` property of https://www.w3.org/TR/vc-data-model/#credential-subject.

## `proof` (MerkleProof2019, required)

Defined by `proof` property of https://www.w3.org/TR/vc-data-model/#proofs-signatures.

---

# Sub Schemas

The schema defines the following additional types:

## `display` (object)
An optional object that sets a display for the Blockcerts document.

If defined, the object takes three properties:
* `contentMediaType`: the type of data to be displayed ([https://schema.org/encodingFormat](https://schema.org/encodingFormat)). Ex. `text-html`
* `contentEncoding`: the encoding used to store the content to be displayed. Optional. Ex. `base64`
* `content`: the content to display. Must be encoded following the `contentEncoding` property if set.

## `JsonLdContext` (undefined)

A link to a valid JSON-LD context, or array of JSON-LD contexts

This property must be one of the following types:

* `string`
* `array`

## `JsonLdType` (undefined)

A type or an array of types defined in a referenced JSON-LD context.

This property must be one of the following types:

* `string`
* `array`

## `DateTime` (string)

Verifiable Credentials must express timestamps as strings compatible with ISO 8601 guidelines, including the time and a time zone indicator. It is recommended to publish all timestamps in UTC. Previous versions of Open Badges allowed Unix timestamps as integers. Open Badges v2.0 requires string ISO 8601 values with time zone indicators. For example, 2016-12-31T23:59:59+00:00 is a valid ISO 8601 timestamp. It contains the year, month, day, T separator, hour number 0-23, minute, optional seconds and decimal microsecond, and a time zone indicator (+/- an offset from UTC or the Z designator for UTC).

## `Issuer` (undefined)

The value of the issuer property MUST be either a URI or an object containing an id property. It is RECOMMENDED that the URI in the issuer or its id be one which, if dereferenced, results in a document containing machine-readable information about the issuer that can be used to verify the information expressed in the credential.

This property must be one of the following types:

* `string`
* `object`

## `MerkleProof2019` (undefined)

Defined by https://w3c-dvcg.github.io/lds-merkle-proof-2019/
