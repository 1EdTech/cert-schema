verified on 2022/07/11

# Metadata property

You may define a `metadata` property as part of Blockcerts v3.

The object should stored as a stringified JSON as we let this property loosely defined,
and as such cannot anticipate its final shape, which in turn means that it will not be normalized by JSONLD for hashing
otherwise.

The object however still expects a shape to be respected:

## `schema`
 A JSON schema describing the metadata object.
When defining the groups that hold your properties, you will need to add a `properties` definition which lists the
 available keys. Each properties definition needs to reference a `title` (which will be used for display in 
 blockcerts-verifier and the wallet apps), and a `type` property.

If the type is `string`, you may add a `format` property to support links. In that case, the `format` property can be 
`uri`, `email`, or `phoneNumber`.

In all other cases the value will be represented as text.
 
## `displayOrder`
A array of strings under the shape of `group.property`.

## Groups
You may now define your various groups which hold the data you wish to add to your certificate.
The group and its properties need to be defined in the `displayOrder` array.

Each group needs to be defined in the `schema`.

## Example

```JSON
{
  "schema": {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
      "displayOrder": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "certificate": {
        "type": "object",
        "properties": {
          "issuingInstitution": {
            "title": "Issuing Institution",
            "type": "string"
          }
        }
      }
    }
  },
  "certificate": {
    "issuingInstitution": "Learning Machine Technologies, Inc."
  },
  "displayOrder": [
    "certificate.issuingInstitution"
  ]
}
```