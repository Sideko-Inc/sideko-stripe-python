
### get <a name="get"></a>
GET /v1/charges/{charge}/dispute

<p>Retrieve a dispute for a specified charge.</p>

**API Endpoint**: `GET /v1/charges/{charge}/dispute`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.charge.dispute.get(charge="string")
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
res = await client.charge.dispute.get(charge="string")
```

### create <a name="create"></a>
POST /v1/charges/{charge}/dispute



**API Endpoint**: `POST /v1/charges/{charge}/dispute`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.charge.dispute.create(charge="string")
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
res = await client.charge.dispute.create(charge="string")
```

### close <a name="close"></a>
POST /v1/charges/{charge}/dispute/close



**API Endpoint**: `POST /v1/charges/{charge}/dispute/close`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.charge.dispute.close(charge="string")
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
res = await client.charge.dispute.close(charge="string")
```
