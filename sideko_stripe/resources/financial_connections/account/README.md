
### list <a name="list"></a>
List Accounts

<p>Returns a list of Financial Connections <code>Account</code> objects.</p>

**API Endpoint**: `GET /v1/financial_connections/accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.financial_connections.account.list()
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
res = await client.financial_connections.account.list()
```

### get <a name="get"></a>
Retrieve an Account

<p>Retrieves the details of an Financial Connections <code>Account</code>.</p>

**API Endpoint**: `GET /v1/financial_connections/accounts/{account}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.financial_connections.account.get(account="string")
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
res = await client.financial_connections.account.get(account="string")
```

### disconnect <a name="disconnect"></a>
Disconnect an Account

<p>Disables your access to a Financial Connections <code>Account</code>. You will no longer be able to access data associated with the account (e.g. balances, transactions).</p>

**API Endpoint**: `POST /v1/financial_connections/accounts/{account}/disconnect`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.financial_connections.account.disconnect(account="string")
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
res = await client.financial_connections.account.disconnect(account="string")
```

### refresh <a name="refresh"></a>
Refresh Account data

<p>Refreshes the data associated with a Financial Connections <code>Account</code>.</p>

**API Endpoint**: `POST /v1/financial_connections/accounts/{account}/refresh`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.financial_connections.account.refresh(
    account="string", features=["balance"]
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
res = await client.financial_connections.account.refresh(
    account="string", features=["balance"]
)
```

### subscribe <a name="subscribe"></a>
Subscribe to data refreshes for an Account

<p>Subscribes to periodic refreshes of data associated with a Financial Connections <code>Account</code>.</p>

**API Endpoint**: `POST /v1/financial_connections/accounts/{account}/subscribe`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.financial_connections.account.subscribe(
    account="string", features=["transactions"]
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
res = await client.financial_connections.account.subscribe(
    account="string", features=["transactions"]
)
```

### unsubscribe <a name="unsubscribe"></a>
Unsubscribe from data refreshes for an Account

<p>Unsubscribes from periodic refreshes of data associated with a Financial Connections <code>Account</code>.</p>

**API Endpoint**: `POST /v1/financial_connections/accounts/{account}/unsubscribe`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.financial_connections.account.unsubscribe(
    account="string", features=["transactions"]
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
res = await client.financial_connections.account.unsubscribe(
    account="string", features=["transactions"]
)
```
