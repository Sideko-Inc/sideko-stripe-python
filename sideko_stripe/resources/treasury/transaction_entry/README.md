
### list <a name="list"></a>
List all TransactionEntries

<p>Retrieves a list of TransactionEntry objects.</p>

**API Endpoint**: `GET /v1/treasury/transaction_entries`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.transaction_entry.list(financial_account="string")
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
res = await client.treasury.transaction_entry.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve a TransactionEntry

<p>Retrieves a TransactionEntry object.</p>

**API Endpoint**: `GET /v1/treasury/transaction_entries/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.transaction_entry.get(id="string")
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
res = await client.treasury.transaction_entry.get(id="string")
```
