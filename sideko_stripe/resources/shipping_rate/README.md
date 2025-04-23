
### list <a name="list"></a>
List all shipping rates

<p>Returns a list of your shipping rates.</p>

**API Endpoint**: `GET /v1/shipping_rates`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.shipping_rate.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.shipping_rate.list()
```

### get <a name="get"></a>
Retrieve a shipping rate

<p>Returns the shipping rate object with the given ID.</p>

**API Endpoint**: `GET /v1/shipping_rates/{shipping_rate_token}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.shipping_rate.get(shipping_rate_token="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.shipping_rate.get(shipping_rate_token="string")
```

### create <a name="create"></a>
Create a shipping rate

<p>Creates a new shipping rate object.</p>

**API Endpoint**: `POST /v1/shipping_rates`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.shipping_rate.create(display_name="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.shipping_rate.create(display_name="string")
```

### update <a name="update"></a>
Update a shipping rate

<p>Updates an existing shipping rate object.</p>

**API Endpoint**: `POST /v1/shipping_rates/{shipping_rate_token}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.shipping_rate.update(shipping_rate_token="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.shipping_rate.update(shipping_rate_token="string")
```
