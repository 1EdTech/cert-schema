
# Certificate Schema V1

The schema defines the following properties:

## `certificate` (object, required)

Properties of the `certificate` object:

### `id` (string, required)

URI link to a JSON that describes the type of certificate. Default format is https://[domain]/criteria/[year]/[month]/[certificate_title].json.

### `image` (string, required)

A base-64 encoded png image of the certificate's image.

Additional restrictions:

* Regex pattern: `data:image/png;base64,`

### `language` (string, required)

Represents the ieft language and ieft country codes. Format is [ieft_language]-[IEFT_COUNTRY].

Additional restrictions:

* Regex pattern: `[a-z]{2}-[A-Z]{2}`

### `subtitle` (object, required)

Subtitle of the certificate.

Properties of the `subtitle` object:

#### `content` (string, required)

Content of the subtitle.

#### `display` (boolean, required)

Flag that indicates whether to show or hide the subtitle in the viewer.

### `title` (string, required)

Title of the certificate.

### `issuer` (object, required)

Details about the issuer of the certificate.

Properties of the `issuer` object:

#### `image` (string, required)

A base-64 encoded png image of the issuer's logo.

Additional restrictions:

* Regex pattern: `data:image/png;base64,`

#### `id` (string, required)

Link to a JSON that details the issuer's issuing and recovation keys. Default is https://[domain]/issuer/[org_abbr]-issuer.json. Included for (near) backward compatibility with open badges specification 1.1

#### `url` (string, required)

URI of the issuer's homepage

#### `name` (string, required)

Name of the issuer.

#### `email` (string, required)

Email address of the issuer.

### `description` (string, required)

Description of what the certificate represents. Usually one - three sentences long.

## `assertion` (object, required)

Properties of the `assertion` object:

### `evidence` (string, required)

Text, uri, etc. that shows evidence of the recipient's learning that the certificate represents. Can be left as an empty string if not used.

### `uid` (string, required)

Unique identifier. By default it is created using the string of a BSON ObjectId(), yielding an identifier 24 characters long.

### `issuedOn` (string, required)

Date the the certificate JSON was created.

### `id` (string, required)

URI that links to the certificate on the viewer. Default is https://[domain]/[uid]

### `image:signature` (string, required)

A base-64 encoded png image of the issuer's signature.

Additional restrictions:

* Regex pattern: `data:image/png;base64,`

## `verify` (object, required)

Properties of the `verify` object:

### `attribute-signed` (string, required)

Name of the attribute in the json that is signed by the issuer's private key. Default is 'uid', referring to the uid attribute.

### `type` (string, required)

Name of the signing method. Default is 'ECDSA(secp256k1)', referring to the Bitcoin method of signing messages with the issuer's private key.

### `signer` (string, required)

URI where issuer's public key is presented. Default is https://[domain]/keys/[org-abbr]-certs-public-key.asc. Compatible with open badges specification v1.1. Ideally, we would change this to point to a JSON instead, so we could retire keys (similar to the way we handle the issuer ID), but for now we're sticking with the OBS 1.1.

## `recipient` (object, required)

Properties of the `recipient` object:

### `familyName` (string, required)

Family name of the recipient.

### `identity` (string, required)

String that represents a recipient's identity. By default, it is an email address.

### `type` (string, required)

Type of value in the identity field. Default is 'email'.

### `hashed` (boolean, required)

Describes if the value in the identity field is hashed or not. Default is false, indicating that the identity is not hashed.

### `pubkey` (string, required)

Bitcoin address (compressed public key, usually 24 characters) of the recipient.

### `givenName` (string, required)

Given name of the recipient

## `signature` (string)

String of signature created when the Bitcoin private key signs the value in the attribute-signed field.

## `extension` (object)

Extension object that includes extra fields not in the standard.

Properties of the `extension` object:

### `assertion` (object)

Properties of the `assertion` object:

### `verify` (object)

Properties of the `verify` object:

### `certificate` (object)

Properties of the `certificate` object:

### `recipient` (object)

Properties of the `recipient` object:
