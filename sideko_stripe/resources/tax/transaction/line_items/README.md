
### list <a name="list"></a>
Retrieve a transaction's line items

<p>Retrieves the line items of a committed standalone transaction as a collection.</p>

**API Endpoint**: `GET /v1/tax/transactions/{transaction}/line_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.transaction.line_items.list(transaction="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.transaction.line_items.list(transaction="string")
```
