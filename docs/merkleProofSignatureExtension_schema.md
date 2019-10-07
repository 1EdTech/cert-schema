## MerkleProof2017 schema

An extension that allows an issuer to issue an Open Badge on the blockchain and provide proof of inclusion in a blockchain transaction. This uses [Merkle Proof Signature Suite 2017](https://w3c-dvcg.github.io/lds-merkleproof2017/)

This signature scheme is used along with the OBI verification extension type `MerkleProofVerification2017`.

The schema defines the following properties:

### `type` (JsonLdType, required)

### `merkleRoot` (string, required)

### `targetHash` (string, required)

### `proof` (array, required)

The object is an array with all elements of the type `object`.

The array object has the following properties:

#### `right` (string)

#### `left` (string)

### `anchors` (array, required)

The object is an array with all elements of the type `object`.

The array object has the following properties:

#### `sourceId` (string)

#### `type` (string)

#### `chain` (string)

Chain is an optional field introduced by Blockcerts to help during verification. Current supported values are:

- bitcoinMainnet
- bitcoinTestnet
- bitcoinRegtest
- ethereumMainnet
- ethereumRopsten
- mockchain


---

# Sub Schemas

The schema defines the following additional types:

## `JsonLdType`

A type or an array of types defined in a JSON-LD context file.

This property must be one of the following types:

* `string`
* `array`
