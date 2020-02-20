# API Documentation
## To get products: GET request to '/products'
The response payload is as follows:

```
[
    {
        "sku": "abc",
        "attributes": {
            "size": "small",
            "grams": "100",
            "foo": "bar"
        }
    }
]
```

## To set products: POST request to '/products'

The payload for the POST request uses a difference model which means that only the changes need to be in the request body.
In this difference model omitted products or attributes are not deleted.

To delete products or attributes do the following:
- Attributes:
Specifing a ```null``` value for an attribute will delete that attribute from the product
e.g.:
```
[
    {
        "sku": "abc",
        "attributes": {
            "grams": null,
        }
    }
]
```

- Products:
Specifing a ```null``` value for a product's attributes will delete the product
e.g.:
```
[
    {
        "sku": "abc",
        "attributes": null
    }
]
```
Note: A product with no attributes is simply and empty object `{}`