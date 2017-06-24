## Assertion Schema

Extends the Open Badges Assertion Schema for certificates on the blockchain

The schema defines the following properties:

### `@context` (JsonLdContext)

A link to a valid JSON-LD context file, that maps term names to contexts. Blockchain Certificate contexts may also define JSON-schema to validate Blockchain Certificates against. In a Blockchain Certificate Object, this will almost always be a string:uri to a single context file, but might rarely be an array of links or context objects instead. This schema also allows direct mapping of terms to IRIs by using an object as an option within an array.

This property must be one of the following types:

*   `string`
*   `array`

### `type` (JsonLdType, required)

A type or an array of types that the Blockchain Certificate object represents. The first or only item should be ‘Assertion’, and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: ‘Assertion’

This property must be one of the following types:

*   `string`
*   `array`

### `id` (string, required)

URI that links to the certificate on the viewer.

### `uid` (string, required)

Unique identifier, in GUID format. V1.2 change: string pattern changed to guid

Additional restrictions:

*   Regex pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

### `issuedOn` (DateTime, required)

Date the certificate JSON was created. This uses the Open Badges DateTime type, defined as one of:

* ISO 8601 date format string yyyy-MM-dd'T'HH:mm:ss.SSS, where the time component is optional and time zone is optional
* 10-digit UNIX timestamp, epoch time

### `evidence` (string)

URL of the work that the recipient did to earn the achievement. This can be a page that links out to other pages if linking directly to the work is infeasible. V1.2 made this field optional, which is consistent with OBI spec.

### `expires` (DateTime)

If the achievement has some notion of expiry, this indicates a date when a badge should no longer be considered valid.

This uses the Open Badges DateTime type, defined as one of:

* ISO 8601 date format string yyyy-MM-dd'T'HH:mm:ss.SSS, where the time component is optional and time zone is optional
* 10-digit UNIX timestamp, epoch time

If the ISO 8601 format is used and no time zone is provided, the certificate verifiers will assume UTC.

### `image:signature` (object)

A single signature image, or array of objects with fields image and jobTitle. V1.2 change: support multiple signatures

Must be one of the following types:

* `string`
* `array`

If type is string, then value must be a Data URI; a base-64 encoded png image of the certificate’s image. https://en.wikipedia.org/wiki/Data_URI_scheme

If type is array, then array items are objects consisting of properties:

`jobTitle`: (string)

Title of the undersigned. http://schema.org/Person#jobTitle

`image`: (string)

Data URI; a base-64 encoded png image of the certificate’s image. https://en.wikipedia.org/wiki/Data_URI_scheme


Additional restrictions:

*   Image regex pattern: `data:image/png;base64,`
