
### list <a name="list"></a>
List all OutboundTransfers

<p>Returns a list of OutboundTransfers sent from the specified FinancialAccount.</p>

**API Endpoint**: `GET /v1/treasury/outbound_transfers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_transfer.list(financial_account="string")
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
res = await client.treasury.outbound_transfer.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve an OutboundTransfer

<p>Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.</p>

**API Endpoint**: `GET /v1/treasury/outbound_transfers/{outbound_transfer}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_transfer.get(outbound_transfer="string")
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
res = await client.treasury.outbound_transfer.get(outbound_transfer="string")
```

### create <a name="create"></a>
Create an OutboundTransfer

<p>Creates an OutboundTransfer.</p>

**API Endpoint**: `POST /v1/treasury/outbound_transfers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_transfer.create(
    amount=123, currency="string", financial_account="string"
)
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
res = await client.treasury.outbound_transfer.create(
    amount=123, currency="string", financial_account="string"
)
```

### cancel <a name="cancel"></a>
Cancel an OutboundTransfer

<p>An OutboundTransfer can be canceled if the funds have not yet been paid out.</p>

**API Endpoint**: `POST /v1/treasury/outbound_transfers/{outbound_transfer}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_transfer.cancel(outbound_transfer="string")
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
res = await client.treasury.outbound_transfer.cancel(outbound_transfer="string")
```
