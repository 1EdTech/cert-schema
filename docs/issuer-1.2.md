# Blockchain Certificates Issuer Schema, Version 1.2

Extends the Open Badges Issuer Schema for certificates on the blockchain

The schema defines the following properties:

## `@context` (JsonLdContext)

## `type` (JsonLdType)

## `id` (string, required)

Link to a JSON that details the issuer's issuing and recovation keys. Default is https://[domain]/issuer/[org_abbr]-issuer.json. Included for (near) backward compatibility with open badges specification 1.1

## `image` (BCBadgeImage)

## `name` (string, required)

Human-readable name of the issuing entity

## `url` (string, required)

The URL of the issuer's website or homepage

## `description` (string)

A text description of the issuing organization

## `email` (string)

Contact address for the individual or organization.

## `revocationList` (string)

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdContext` (undefined)

A link to a valid JSON-LD context file, that maps term names to contexts. Blockchain Certificate contexts may also define JSON-schema to validate Blockchain Certificates against. In a Blockchain Certificate Object, this will almost always be a string:uri to a single context file, but might rarely be an array of links or context objects instead. This schema also allows direct mapping of terms to IRIs by using an object as an option within an array.

This property must be one of the following types:

* `string`
* `array`

## `JsonLdType` (undefined)

A type or an array of types that the Blockchain Certificate object represents. The first or only item should be 'Issuer', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'Issuer'

This property must be one of the following types:

* `string`
* `array`

## `BCBadgeImage` (undefined)

An image representative of the entity. This overrides BadgeImage from OBI because oneOf, compared to anyOf, was failing validation