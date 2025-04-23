
### list <a name="list"></a>
List all ForwardingRequests

<p>Lists all ForwardingRequest objects.</p>

**API Endpoint**: `GET /v1/forwarding/requests`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.forwarding.request.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.forwarding.request.list()
```

### get <a name="get"></a>
Retrieve a ForwardingRequest

<p>Retrieves a ForwardingRequest object.</p>

**API Endpoint**: `GET /v1/forwarding/requests/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.forwarding.request.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.forwarding.request.get(id="string")
```

### create <a name="create"></a>
Create a ForwardingRequest

<p>Creates a ForwardingRequest object.</p>

**API Endpoint**: `POST /v1/forwarding/requests`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.forwarding.request.create(
    payment_method="string", replacements=["card_cvc"], url="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.forwarding.request.create(
    payment_method="string", replacements=["card_cvc"], url="string"
)
```
