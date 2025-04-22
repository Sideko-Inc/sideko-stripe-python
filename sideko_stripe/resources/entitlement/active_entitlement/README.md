
### list <a name="list"></a>
List all active entitlements

<p>Retrieve a list of active entitlements for a customer</p>

**API Endpoint**: `GET /v1/entitlements/active_entitlements`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.entitlement.active_entitlement.list(customer="string")
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
res = await client.entitlement.active_entitlement.list(customer="string")
```

### get <a name="get"></a>
Retrieve an active entitlement

<p>Retrieve an active entitlement</p>

**API Endpoint**: `GET /v1/entitlements/active_entitlements/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.entitlement.active_entitlement.get(id="string")
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
res = await client.entitlement.active_entitlement.get(id="string")
```
