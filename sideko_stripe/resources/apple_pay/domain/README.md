
### delete <a name="delete"></a>
DELETE /v1/apple_pay/domains/{domain}

<p>Delete an apple pay domain.</p>

**API Endpoint**: `DELETE /v1/apple_pay/domains/{domain}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apple_pay.domain.delete(domain="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apple_pay.domain.delete(domain="string")
```

### list <a name="list"></a>
GET /v1/apple_pay/domains

<p>List apple pay domains.</p>

**API Endpoint**: `GET /v1/apple_pay/domains`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apple_pay.domain.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apple_pay.domain.list()
```

### get <a name="get"></a>
GET /v1/apple_pay/domains/{domain}

<p>Retrieve an apple pay domain.</p>

**API Endpoint**: `GET /v1/apple_pay/domains/{domain}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apple_pay.domain.get(domain="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apple_pay.domain.get(domain="string")
```

### create <a name="create"></a>
POST /v1/apple_pay/domains

<p>Create an apple pay domain.</p>

**API Endpoint**: `POST /v1/apple_pay/domains`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apple_pay.domain.create(domain_name="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apple_pay.domain.create(domain_name="string")
```
