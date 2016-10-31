The schema defines the following properties:

# `issuerKeys` (array, required)

list of issuer keys, listed in descending date order (most recent first). V1.2 change: renamed from issuer_key, added optional invalidated field.

The object is an array with all elements of the type `object`.

The array object has the following properties:

## `date` (string, required)

ISO-8601 formatted date time the key was activated.

## `key` (string, required)

Bitcoin address (compressed public key, usually 24 characters) that the issuer uses to issue the certificates.

## `invalidated` (string)

Optional ISO-8601 formatted date time the key was invalidated.

# `revocationKeys` (array, required)

list of revocation keys, listed in descending date order (most recent first). V1.2 changes: renamed from revocation_key, added optional invalidated field.

The object is an array with all elements of the type `object`.

The array object has the following properties:

## `date` (string, required)

ISO-8601 formatted date time the key was activated.

## `key` (string, required)

Bitcoin address (compressed public key, usually 24 characters) that the issuer uses to revoke the certificates.

## `invalidated` (string)

Optional ISO-8601 formatted date time the key was invalidated.

# `id` (string, required)

The URL of the issuer's website or homepage

# `name` (string, required)

Human-readable name of the issuing entity

# `email` (string, required)

Contact address for the individual or organization.

# `url` (string, required)

The URL where the issuer's certificates can be found

# `introductionURL` (string, required)

The URL hosting the issuer's introduction endpoint

# `image` (string, required)

Data URI; a base-64 encoded png image of the issuer's image. https://en.wikipedia.org/wiki/Data_URI_scheme

Additional restrictions:

* Regex pattern: `data:image/png;base64,`