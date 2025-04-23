
### list <a name="list"></a>
List credit balance transactions

<p>Retrieve a list of credit balance transactions.</p>

**API Endpoint**: `GET /v1/billing/credit_balance_transactions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.credit_balance_transaction.list(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.credit_balance_transaction.list(customer="string")
```

### get <a name="get"></a>
Retrieve a credit balance transaction

<p>Retrieves a credit balance transaction.</p>

**API Endpoint**: `GET /v1/billing/credit_balance_transactions/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.credit_balance_transaction.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.credit_balance_transaction.get(id="string")
```
