## RecipientProfile schema

A Blockcerts extension allowing inclusion of additional recipient details, including recipient publicKey and name. Inclusion of the recipient publicKey allows the recipient to make a strong claim of ownership over the key, and hence the badge being awarded. In the future, publicKey will be deprecated in favor of a decentralized id (DID) in the `id` field.

The schema defines the following properties:

### `id` (string)

reserved for future use as DID

### `name` (string)

Name of recipient, [http://schema.org/name](http://schema.org/name)

### `publicKey` (string)

In Blockcerts `publicKey` IRIs are typically represented with a `<scheme>:` prefix. For Bitcoin transactions, this would be the recipient public Bitcoin address prefixed with `ecdsa-koblitz-pubkey:`; e.g. `ecdsa-koblitz-pubkey:14RZvYazz9H2DC2skBfpPVxax54g4yabxe`

Additional restrictions:

* Format: `uri`