# Blockchain Certificates Certificate Schema, Version 1.2

Extends the Open Badges Certificate Schema for certificates on the blockchain

The schema defines the following properties:

## `id` (string, required)

URI link to a JSON that describes the type of certificate. Default format is https://[domain]/criteria/[year]/[month]/[certificate_title].json.

## `name` (string)

## `description` (string, required)

## `image` (string, required)

Data URI; a base-64 encoded png image of the certificate's image. https://en.wikipedia.org/wiki/Data_URI_scheme

Additional restrictions:

* Regex pattern: `data:image/png;base64,`

## `criteria` (string)

## `alignment`

## `tags`

## `issuer` (Issuer, required)

## `language` (string)

Represents the ieft language and ieft country codes. Format is [ieft_language]-[IEFT_COUNTRY]. 1.2 changes: this field is optional

Additional restrictions:

* Regex pattern: `[a-z]{2}-[A-Z]{2}`

## `subtitle` (string)

Subtitle of the certificate. 1.2 changes: this type is now string, and this field is optional

## `title` (string, required)

Title of the certificate. Note: this is called 'name' in the OBI schema

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdType`

A type or an array of types that the certificate represents. The first or only item should be 'Certificate', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'Certificate'

This property must be one of the following types:

* `string`
* `array`

## `Issuer` [Issuer](issuer-1.2.md)