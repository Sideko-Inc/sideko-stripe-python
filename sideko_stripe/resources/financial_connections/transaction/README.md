
### list <a name="list"></a>
List Transactions

<p>Returns a list of Financial Connections <code>Transaction</code> objects.</p>

**API Endpoint**: `GET /v1/financial_connections/transactions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.financial_connections.transaction.list(account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.financial_connections.transaction.list(account="string")
```

### get <a name="get"></a>
Retrieve a Transaction

<p>Retrieves the details of a Financial Connections <code>Transaction</code></p>

**API Endpoint**: `GET /v1/financial_connections/transactions/{transaction}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.financial_connections.transaction.get(transaction="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.financial_connections.transaction.get(transaction="string")
```
