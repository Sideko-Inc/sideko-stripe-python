
### list <a name="list"></a>
List all account capabilities

<p>Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.</p>

**API Endpoint**: `GET /v1/accounts/{account}/capabilities`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.account.capability.list(account="string")
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
res = await client.account.capability.list(account="string")
```

### get <a name="get"></a>
Retrieve an Account Capability

<p>Retrieves information about the specified Account Capability.</p>

**API Endpoint**: `GET /v1/accounts/{account}/capabilities/{capability}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.account.capability.get(account="string", capability="string")
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
res = await client.account.capability.get(account="string", capability="string")
```

### create <a name="create"></a>
Update an Account Capability

<p>Updates an existing Account Capability. Request or remove a capability by updating its <code>requested</code> parameter.</p>

**API Endpoint**: `POST /v1/accounts/{account}/capabilities/{capability}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.account.capability.create(account="string", capability="string")
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
res = await client.account.capability.create(account="string", capability="string")
```
