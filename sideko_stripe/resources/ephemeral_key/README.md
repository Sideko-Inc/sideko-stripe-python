
### delete <a name="delete"></a>
Immediately invalidate an ephemeral key

<p>Invalidates a short-lived API key for a given resource.</p>

**API Endpoint**: `DELETE /v1/ephemeral_keys/{key}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.ephemeral_key.delete(key="string")
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
res = await client.ephemeral_key.delete(key="string")
```

### create <a name="create"></a>
Create an ephemeral key

<p>Creates a short-lived API key for a given resource.</p>

**API Endpoint**: `POST /v1/ephemeral_keys`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.ephemeral_key.create()
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
res = await client.ephemeral_key.create()
```
