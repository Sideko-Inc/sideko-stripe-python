
### list <a name="list"></a>
List credit grants

<p>Retrieve a list of credit grants.</p>

**API Endpoint**: `GET /v1/billing/credit_grants`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.credit_grant.list()
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
res = await client.billing.credit_grant.list()
```

### get <a name="get"></a>
Retrieve a credit grant

<p>Retrieves a credit grant.</p>

**API Endpoint**: `GET /v1/billing/credit_grants/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.credit_grant.get(id="string")
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
res = await client.billing.credit_grant.get(id="string")
```

### create <a name="create"></a>
Create a credit grant

<p>Creates a credit grant.</p>

**API Endpoint**: `POST /v1/billing/credit_grants`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.credit_grant.create(
    amount={"type_": "monetary"},
    applicability_config={"scope": {}},
    category="paid",
    customer="string",
)
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
res = await client.billing.credit_grant.create(
    amount={"type_": "monetary"},
    applicability_config={"scope": {}},
    category="paid",
    customer="string",
)
```

### update <a name="update"></a>
Update a credit grant

<p>Updates a credit grant.</p>

**API Endpoint**: `POST /v1/billing/credit_grants/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.credit_grant.update(id="string")
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
res = await client.billing.credit_grant.update(id="string")
```

### expire <a name="expire"></a>
Expire a credit grant

<p>Expires a credit grant.</p>

**API Endpoint**: `POST /v1/billing/credit_grants/{id}/expire`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.credit_grant.expire(id="string")
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
res = await client.billing.credit_grant.expire(id="string")
```

### void <a name="void"></a>
Void a credit grant

<p>Voids a credit grant.</p>

**API Endpoint**: `POST /v1/billing/credit_grants/{id}/void`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.credit_grant.void(id="string")
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
res = await client.billing.credit_grant.void(id="string")
```
