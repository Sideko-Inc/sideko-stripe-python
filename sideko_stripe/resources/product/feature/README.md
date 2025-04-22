
### delete <a name="delete"></a>
Remove a feature from a product

<p>Deletes the feature attachment to a product</p>

**API Endpoint**: `DELETE /v1/products/{product}/features/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.product.feature.delete(id="string", product="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.product.feature.delete(id="string", product="string")
```

### list <a name="list"></a>
List all features attached to a product

<p>Retrieve a list of features for a product</p>

**API Endpoint**: `GET /v1/products/{product}/features`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.product.feature.list(product="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.product.feature.list(product="string")
```

### get <a name="get"></a>
Retrieve a product_feature

<p>Retrieves a product_feature, which represents a feature attachment to a product</p>

**API Endpoint**: `GET /v1/products/{product}/features/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.product.feature.get(id="string", product="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.product.feature.get(id="string", product="string")
```

### create <a name="create"></a>
Attach a feature to a product

<p>Creates a product_feature, which represents a feature attachment to a product</p>

**API Endpoint**: `POST /v1/products/{product}/features`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.product.feature.create(entitlement_feature="string", product="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.product.feature.create(
    entitlement_feature="string", product="string"
)
```
