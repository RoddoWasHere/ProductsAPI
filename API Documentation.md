# API Documentation
## To get products: GET request to '/products'
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
Specifing a ```null``` value for an product's attributes will delete the product
e.g.:
```
[
    {
        "sku": "abc",
        "attributes": null
    }
]
```