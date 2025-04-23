
### list <a name="list"></a>
List all Transactions

<p>Retrieves a list of Transaction objects.</p>

**API Endpoint**: `GET /v1/treasury/transactions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.transaction.list(financial_account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.transaction.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve a Transaction

<p>Retrieves the details of an existing Transaction.</p>

**API Endpoint**: `GET /v1/treasury/transactions/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.transaction.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.transaction.get(id="string")
```
