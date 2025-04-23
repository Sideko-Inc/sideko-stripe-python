
### list <a name="list"></a>
List all payment links

<p>Returns a list of your payment links.</p>

**API Endpoint**: `GET /v1/payment_links`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_link.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_link.list()
```

### get <a name="get"></a>
Retrieve payment link

<p>Retrieve a payment link.</p>

**API Endpoint**: `GET /v1/payment_links/{payment_link}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_link.get(payment_link="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_link.get(payment_link="string")
```

### create <a name="create"></a>
Create a payment link

<p>Creates a payment link.</p>

**API Endpoint**: `POST /v1/payment_links`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_link.create(line_items=[{"price": "string", "quantity": 123}])
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_link.create(
    line_items=[{"price": "string", "quantity": 123}]
)
```

### update <a name="update"></a>
Update a payment link

<p>Updates a payment link.</p>

**API Endpoint**: `POST /v1/payment_links/{payment_link}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_link.update(payment_link="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_link.update(payment_link="string")
```
