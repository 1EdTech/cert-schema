# Blockchain Certificates Assertion Schema, Version 1.2

Extends the Open Badges Assertion Schema for certificates on the blockchain

The schema defines the following properties:

## `@context` (JsonLdContext)

## `type` (JsonLdType, required)

## `id` (string, required)

URI that links to the certificate on the viewer.

## `uid` (string, required)

Unique identifier, in GUID format. V1.2 change: string pattern changed to guid

Additional restrictions:

* Regex pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## `issuedOn` (, required)

Date the the certificate JSON was created.

## `evidence` (string)

URL of the work that the recipient did to earn the achievement. This can be a page that links out to other pages if linking directly to the work is infeasible. V1.2 made this field optional, which is consistent with OBI spec.

## `expires`

If the achievement has some notion of expiry, this indicates a date when a badge should no longer be considered valid.

## `image:signature` (object)

A single signature image, or array of objects with fields image and jobTitle. V1.2 change: support multiple signatures

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdContext` (undefined)

A link to a valid JSON-LD context file, that maps term names to contexts. Blockchain Certificate contexts may also define JSON-schema to validate Blockchain Certificates against. In a Blockchain Certificate Object, this will almost always be a string:uri to a single context file, but might rarely be an array of links or context objects instead. This schema also allows direct mapping of terms to IRIs by using an object as an option within an array.

This property must be one of the following types:

* `string`
* `array`

## `JsonLdType` (undefined)

A type or an array of types that the Blockchain Certificate object represents. The first or only item should be 'Assertion', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'Assertion'

This property must be one of the following types:

* `string`
* `array`