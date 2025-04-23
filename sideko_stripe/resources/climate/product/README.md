
### list <a name="list"></a>
List products

<p>Lists all available Climate product objects.</p>

**API Endpoint**: `GET /v1/climate/products`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.product.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.product.list()
```

### get <a name="get"></a>
Retrieve a product

<p>Retrieves the details of a Climate product with the given ID.</p>

**API Endpoint**: `GET /v1/climate/products/{product}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.product.get(product="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.product.get(product="string")
```
