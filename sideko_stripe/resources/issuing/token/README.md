
### list <a name="list"></a>
List all issuing tokens for card

<p>Lists all Issuing <code>Token</code> objects for a given card.</p>

**API Endpoint**: `GET /v1/issuing/tokens`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.token.list(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.token.list(card="string")
```

### get <a name="get"></a>
Retrieve an issuing token

<p>Retrieves an Issuing <code>Token</code> object.</p>

**API Endpoint**: `GET /v1/issuing/tokens/{token}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.token.get(token="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.token.get(token="string")
```

### update <a name="update"></a>
Update a token status

<p>Attempts to update the specified Issuing <code>Token</code> object to the status specified.</p>

**API Endpoint**: `POST /v1/issuing/tokens/{token}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.token.update(status="active", token="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.token.update(status="active", token="string")
```
