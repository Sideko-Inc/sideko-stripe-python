
### list <a name="list"></a>
List all ReceivedDebits

<p>Returns a list of ReceivedDebits.</p>

**API Endpoint**: `GET /v1/treasury/received_debits`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.received_debit.list(financial_account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.received_debit.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve a ReceivedDebit

<p>Retrieves the details of an existing ReceivedDebit by passing the unique ReceivedDebit ID from the ReceivedDebit list</p>

**API Endpoint**: `GET /v1/treasury/received_debits/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.received_debit.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.received_debit.get(id="string")
```
