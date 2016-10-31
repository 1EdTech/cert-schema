# Blockchain Certificates Certificate Schema, Version 1.2

Extends the Open Badges Certificate Schema for certificates on the blockchain

The schema defines the following properties:

## `@context` (JsonLdContext)

## `type` (JsonLdType)

## `id` (string)

URI link to a JSON that describes the type of certificate. Default format is https://[domain]/criteria/[year]/[month]/[certificate_title].json. V1.2 change: this field is optional.

## `name` (string, required)

Name (or title) of the certificate. V1.2 change: renamed from 'title' to be consistent with OBI schema

## `description` (string, required)

## `image` (string, required)

Data URI; a base-64 encoded png image of the certificate's image. https://en.wikipedia.org/wiki/Data_URI_scheme

Additional restrictions:

* Regex pattern: `data:image/png;base64,`

## `criteria` (string)

## `issuer` (Issuer, required)

## `alignment`

## `tags`

## `language` (string)

Represents the ieft language and ieft country codes. Format is [ieft_language]-[IEFT_COUNTRY]. V1.2 changes: this field is optional

Additional restrictions:

* Regex pattern: `[a-z]{2}-[A-Z]{2}`

## `subtitle` (string)

Subtitle of the certificate. V1.2 changes: this type is now string, and this field is optional

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdContext` (undefined)

A link to a valid JSON-LD context file, that maps term names to contexts. Blockchain Certificate contexts may also define JSON-schema to validate Blockchain Certificates against. In a Blockchain Certificate Object, this will almost always be a string:uri to a single context file, but might rarely be an array of links or context objects instead. This schema also allows direct mapping of terms to IRIs by using an object as an option within an array.

This property must be one of the following types:

* `string`
* `array`

## `JsonLdType` (undefined)

A type or an array of types that the Blockchain Certificate object represents. The first or only item should be 'Certificate', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'Certificate'

This property must be one of the following types:

* `string`
* `array`

## `Issuer` (undefined)