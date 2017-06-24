## SignatureLine schema

An extension that allows issuers to add signature lines to the visual representation of the badge. This is not part of the cryptographic proof; it is for display purposes only.

The schema defines the following properties:

### `image` (ImageUri, required)

### `jobTitle` (string)

Job title of signer, [http://schema.org/jobTitle](http://schema.org/jobTitle)

### `name` (string)

Full name of signer, [http://schema.org/name](http://schema.org/name)

---

# Sub Schemas

The schema defines the following additional types:

## `ImageUri`

This property may be any of the following types:

* `string`
  * Pattern: `data:image/png;base64,`
  * Description: An image representative of the entity. In Blockcerts this is typically a data URI ([https://en.wikipedia.org/wiki/Data_URI_scheme](https://en.wikipedia.org/wiki/Data_URI_scheme)) embedded as a base-64 encoded PNG image, but it may also be a URI where the image may be found.
* `string`
  * Format: `uri`
  * Description: IRI (typically HTTP) representing this signature image.