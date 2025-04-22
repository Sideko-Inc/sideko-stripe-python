
### list <a name="list"></a>
List Accounts

<p>Returns a list of Financial Connections <code>Account</code> objects.</p>

**API Endpoint**: `GET /v1/linked_accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.linked_account.list()
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
res = await client.linked_account.list()
```

### get <a name="get"></a>
Retrieve an Account

<p>Retrieves the details of an Financial Connections <code>Account</code>.</p>

**API Endpoint**: `GET /v1/linked_accounts/{account}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.linked_account.get(account="string")
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
res = await client.linked_account.get(account="string")
```

### disconnect <a name="disconnect"></a>
Disconnect an Account

<p>Disables your access to a Financial Connections <code>Account</code>. You will no longer be able to access data associated with the account (e.g. balances, transactions).</p>

**API Endpoint**: `POST /v1/linked_accounts/{account}/disconnect`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.linked_account.disconnect(account="string")
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
res = await client.linked_account.disconnect(account="string")
```

### refresh <a name="refresh"></a>
Refresh Account data

<p>Refreshes the data associated with a Financial Connections <code>Account</code>.</p>

**API Endpoint**: `POST /v1/linked_accounts/{account}/refresh`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.linked_account.refresh(account="string", features=["balance"])
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
res = await client.linked_account.refresh(account="string", features=["balance"])
```
