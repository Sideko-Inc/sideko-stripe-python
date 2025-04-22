
### list <a name="list"></a>
List all FinancialAccounts

<p>Returns a list of FinancialAccounts.</p>

**API Endpoint**: `GET /v1/treasury/financial_accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.financial_account.list()
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
res = await client.treasury.financial_account.list()
```

### get <a name="get"></a>
Retrieve a FinancialAccount

<p>Retrieves the details of a FinancialAccount.</p>

**API Endpoint**: `GET /v1/treasury/financial_accounts/{financial_account}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.financial_account.get(financial_account="string")
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
res = await client.treasury.financial_account.get(financial_account="string")
```

### create <a name="create"></a>
Create a FinancialAccount

<p>Creates a new FinancialAccount. Each connected account can have up to three FinancialAccounts by default.</p>

**API Endpoint**: `POST /v1/treasury/financial_accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.financial_account.create(supported_currencies=["string"])
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
res = await client.treasury.financial_account.create(supported_currencies=["string"])
```

### update <a name="update"></a>
Update a FinancialAccount

<p>Updates the details of a FinancialAccount.</p>

**API Endpoint**: `POST /v1/treasury/financial_accounts/{financial_account}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.financial_account.update(financial_account="string")
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
res = await client.treasury.financial_account.update(financial_account="string")
```

### close <a name="close"></a>
Close a FinancialAccount

<p>Closes a FinancialAccount. A FinancialAccount can only be closed if it has a zero balance, has no pending InboundTransfers, and has canceled all attached Issuing cards.</p>

**API Endpoint**: `POST /v1/treasury/financial_accounts/{financial_account}/close`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.financial_account.close(financial_account="string")
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
res = await client.treasury.financial_account.close(financial_account="string")
```
