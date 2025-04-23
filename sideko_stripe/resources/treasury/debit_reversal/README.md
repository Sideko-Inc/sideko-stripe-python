
### list <a name="list"></a>
List all DebitReversals

<p>Returns a list of DebitReversals.</p>

**API Endpoint**: `GET /v1/treasury/debit_reversals`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.debit_reversal.list(financial_account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.debit_reversal.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve a DebitReversal

<p>Retrieves a DebitReversal object.</p>

**API Endpoint**: `GET /v1/treasury/debit_reversals/{debit_reversal}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.debit_reversal.get(debit_reversal="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.debit_reversal.get(debit_reversal="string")
```

### create <a name="create"></a>
Create a DebitReversal

<p>Reverses a ReceivedDebit and creates a DebitReversal object.</p>

**API Endpoint**: `POST /v1/treasury/debit_reversals`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.debit_reversal.create(received_debit="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.debit_reversal.create(received_debit="string")
```
