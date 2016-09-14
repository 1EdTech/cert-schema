# Blockchain Certificates Receipt Schema, Version 1.2

Provides evidence of the certificate on the blockchain, using the chainpoint v2 standard

The schema defines the following properties:

## `type` (string, required)

type of hash. Currently the only supported hash type is SHA256, with chainpoint type ChainpointSHA256v2.

Additional restrictions:

* Regex pattern: `ChainpointSHA256v2`

## `targetHash` (string, required)

hash of item being verified. Currently the only supported hash type is SHA256, and the targetHash format is validated accordingly.

Additional restrictions:

* Regex pattern: `[A-Fa-f0-9]{64}`

## `merkleRoot` (string, required)

Merkle root value -- this is anchored to the blockchain. Currently the only supported hash type is SHA256, and merkleRoot format is validated accordingly.

Additional restrictions:

* Regex pattern: `[A-Fa-f0-9]{64}`

## `proof` (array, required)

how to walk the Merkle tree from the target item to the Merkle root

The object is an array with all elements of the type `object`.

The array object has the following properties:

### `left` (string)

value of left neighbor to combine into parent hash. Currently the only supported hash type is SHA256, and this value format is validated accordingly.

Additional restrictions:

* Regex pattern: `[A-Fa-f0-9]{64}`

### `right` (string)

value of right neighbor to combine into parent hash. Currently the only supported hash type is SHA256, and this value format is validated accordingly.

Additional restrictions:

* Regex pattern: `[A-Fa-f0-9]{64}`

## `anchors` (array, required)

how the proof is anchored to the blockchain

The object is an array with all elements of the type `object`.

The array object has the following properties:

### `type` (string, required)

type of anchor, e.g. BTCOpReturn. Currently the only supported value is BTCOpReturn.

Additional restrictions:

* Regex pattern: `BTCOpReturn`

### `sourceId` (string, required)

How to lookup the proof on the blockchain. Currently this is expected to be the (value of the) Bitcoin transaction id, and this value format is validated accordingly

Additional restrictions:

* Regex pattern: `[A-Fa-f0-9]{64}`

---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdType` 

A type or an array of types that the receipt object represents. The first or only item should be 'BlockchainReceipt', and any others should each be an IRI (usually a URL) corresponding to a definition of the type itself. In almost all cases, there will be only one type: 'BlockchainReceipt'

This property must be one of the following types:

* `string`
* `array`