# Blockcerts Proposed Extensions to Open Badges V2

The [Open Badges specification](https://www.imsglobal.org/sites/default/files/Badges/OBv2p0/index.html) is maintained by [IMS Global](http://www.imsglobal.org/). While developing Blockcerts, we created 4 Open Badge v2-compliant extensions. 2 of these are specific to blockchain verification; the other 2 are extensions we found useful. All are being offered as official Open Badge extensions.

## Summary of extensions

- (Required for blockchain verification) blockchain verification type `MerkleProofVerification2017`, ideally as an enum added to the current verification options "hosted", "signed"
- (Required for blockchain verification) `signature` proof as an Open Badge extension; defined by:
    - [W3C LD Signature Specification](https://w3c-dvcg.github.io/ld-signatures/)
    - [Merkle Proof Signature Suite][https://w3c-dvcg.github.io/lds-merkleproof2017/]
- `recipientProfile` for identifying recipients
  - `RecipientProfile` extends the `Profile` type and adds `publicKey` for embedding a recipient's public key
- `signatureLines` as a image/signer array, intended for display in the certificate

## Example

Following is an example of a Blockcerts certificate. Note that this is fully OBv2 compliant. It uses the Open Badge `Extension` type to identify Open Badge extensions. These are marked in the example with `<` markers.

```
{
  "@context": ["https://w3id.org/openbadges/v2", "https://w3id.org/blockcerts/v2"],
  "type": "Assertion",
  "id": "urn:uuid:3bc1a96a-3501-46ed-8f75-49612bbac257",
  "issuedOn": "2017-07-20T09:33:47.490752+00:00",
  "recipient": {
    "hashed": false,
    "identity": "eularia@landroth.org",
    "type": "email"
  },
  "recipientProfile": {                           <<<<<<<<<<
    "type": ["RecipientProfile", "Extension"],
    "name": "Eularia Landroth",
    "publicKey": "ecdsa-koblitz-pubkey:mtr98kany9G1XYNU74pRnfBQmaCg2FZLmc"
  },
  "badge": {
    "type": "BadgeClass",
    "id": "urn:uuid:82a4c9f2-3588-457b-80ea-da695571b8fc",
    "name": "Certificate of Accomplishment",
    "image": "data:image/png;base64",
    "criteria": {
      "narrative": "Nibh iriure ei nam, modo ridens neglegentur mel eu. At his cibo mucius."
    },
    "issuer": {
      "type": "Profile",
      "id": "https://www.blockcerts.org/samples/2.0/issuer-testnet.json",
      "name": "University of Learning",
      "email": "contact@issuer.org",
      "image": "data:image/png;base64,...",
      "url": "https://www.issuer.org",
      "revocationList": "https://www.blockcerts.org/samples/2.0/revocation-list-testnet.json"
    },
    "signatureLines": [                          <<<<<<<<<<
      {
        "type": ["SignatureLine", "Extension"],
        "name": "Your signature",
        "image": "data:image/png;base64,...",
        "jobTitle": "University Issuer"
      }
    ],
    "description": "Lorem ipsum dolor sit amet, mei docendi concludaturque ad, cu nec partem graece. Est aperiam consetetur cu, expetenda moderatius neglegentur ei nam, suas dolor laudem eam an."
  },
  "verification": {                              <<<<<<<<<<
    "type": ["MerkleProofVerification2017", "Extension"],
    "publicKey": "ecdsa-koblitz-pubkey:msBCHdwaQ7N2ypBYupkp6uNxtr9Pg76imj"
  },
  "signature": {
    "type": ["MerkleProof2017", "Extension"],    <<<<<<<<<<
    "proof": [
      {
        "right": "51b4e22ed024ec7f38dc68b0bf78c87eda525ab0896b75d2064bdb9fc60b2698"
      },
      {
        "right": "61c56cca660b2e616d0bd62775e728f50275ae44adf12d1bfb9b9c507a14766b"
      }
    ],
    "merkleRoot": "3c9ee831b8705f2fbe09f8b3a92247eed88cdc90418c024924be668fdc92e781",
    "targetHash": "c65c6184e3d5a945ddb5437e93ea312411fd33aa1def22b0746d6ecd4aa30f20",
    "anchors": [
      {
        "sourceId": "582733d7cef8035d87cecc9ebbe13b3a2f6cc52583fbcd2b9709f20a6b8b56b3",
        "type": "BTCOpReturn"
      }
    ]
  }
}
```

## Considerations for adopting as official Open Badge extensions

- The current extension type/term names are not assumed to be final; it's expected that we will iterate on them during Open Badges review
- Signature lines are currently defined in the `badge` type instead of the  `assertion` type. I understand that this should likely move to `assertion` per OB extension best practices
- The prefix `ecdsa-koblitz-pubkey:` 
    - This is not final and is being Digital Verification subgroup of the W3C Credentials CG
    - The problem was that examples like this `ecdsa-koblitz-pubkey:msBCHdwaQ7N2ypBYupkp6uNxtr9Pg76imj` are not quite correct
        - The value right of the colon is a base58 encoded ecdsa koblitz public key hash
        - Currently the approach used by others in the community is to keep the `ecdsa-koblitz-pubkey:` and actually list the public key (not the hash)
        - The problem is readability (e.g. bitcoin addresses vs longer public keys)
        - Another option would be to invent a new prefix
    - Alternately, a more forward looking approach would be to use (or reserve) DIDs (Decentralized Identifiers) for this purpose. 
- Are there any special considerations in using the 2017 Merkle Proof Signature Suite from the W3C?
- How do we integrate Blockcerts verification into the OB verifier?
- How do we add the blockchain/blockcerts verification "type" (i.e. signed/hosted/...)

## Extension schemas and context

### Json-ld context

The Json-ld context is listed in the context array of a blockcert. It defines these extension terms. See [https://w3id.org/blockcerts/v2](https://w3id.org/blockcerts/v2)

### Json schemas

- MerkleProofVerification2017 is proposed as a new type enum to the current set of verification types
- [Merkle Proof Signature Schema](https://github.com/blockchain-certificates/cert-schema/blob/master/docs/merkleProofSignatureExtension_schema.md)
- [Recipient Profile Schema](https://github.com/blockchain-certificates/cert-schema/blob/master/docs/recipientProfileExtension_schema.md)
- [Signature Line Schema](https://github.com/blockchain-certificates/cert-schema/blob/master/docs/signatureLineExtension_schema.md)

