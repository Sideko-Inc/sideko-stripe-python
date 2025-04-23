
### list <a name="list"></a>
List all InboundTransfers

<p>Returns a list of InboundTransfers sent from the specified FinancialAccount.</p>

**API Endpoint**: `GET /v1/treasury/inbound_transfers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.inbound_transfer.list(financial_account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.inbound_transfer.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve an InboundTransfer

<p>Retrieves the details of an existing InboundTransfer.</p>

**API Endpoint**: `GET /v1/treasury/inbound_transfers/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.inbound_transfer.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.inbound_transfer.get(id="string")
```

### create <a name="create"></a>
Create an InboundTransfer

<p>Creates an InboundTransfer.</p>

**API Endpoint**: `POST /v1/treasury/inbound_transfers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.inbound_transfer.create(
    amount=123,
    currency="string",
    financial_account="string",
    origin_payment_method="string",
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.inbound_transfer.create(
    amount=123,
    currency="string",
    financial_account="string",
    origin_payment_method="string",
)
```

### cance <a name="cance"></a>
Cancel an InboundTransfer

<p>Cancels an InboundTransfer.</p>

**API Endpoint**: `POST /v1/treasury/inbound_transfers/{inbound_transfer}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.inbound_transfer.cance(inbound_transfer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.inbound_transfer.cance(inbound_transfer="string")
```
