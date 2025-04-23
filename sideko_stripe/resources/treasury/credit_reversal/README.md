
### list <a name="list"></a>
List all CreditReversals

<p>Returns a list of CreditReversals.</p>

**API Endpoint**: `GET /v1/treasury/credit_reversals`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.credit_reversal.list(financial_account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.credit_reversal.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve a CreditReversal

<p>Retrieves the details of an existing CreditReversal by passing the unique CreditReversal ID from either the CreditReversal creation request or CreditReversal list</p>

**API Endpoint**: `GET /v1/treasury/credit_reversals/{credit_reversal}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.credit_reversal.get(credit_reversal="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.credit_reversal.get(credit_reversal="string")
```

### create <a name="create"></a>
Create a CreditReversal

<p>Reverses a ReceivedCredit and creates a CreditReversal object.</p>

**API Endpoint**: `POST /v1/treasury/credit_reversals`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.credit_reversal.create(received_credit="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.credit_reversal.create(received_credit="string")
```
