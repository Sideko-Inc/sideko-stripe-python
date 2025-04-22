
### list <a name="list"></a>
List all OutboundPayments

<p>Returns a list of OutboundPayments sent from the specified FinancialAccount.</p>

**API Endpoint**: `GET /v1/treasury/outbound_payments`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_payment.list(financial_account="string")
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
res = await client.treasury.outbound_payment.list(financial_account="string")
```

### get <a name="get"></a>
Retrieve an OutboundPayment

<p>Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.</p>

**API Endpoint**: `GET /v1/treasury/outbound_payments/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_payment.get(id="string")
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
res = await client.treasury.outbound_payment.get(id="string")
```

### create <a name="create"></a>
Create an OutboundPayment

<p>Creates an OutboundPayment.</p>

**API Endpoint**: `POST /v1/treasury/outbound_payments`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_payment.create(
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
res = await client.treasury.outbound_payment.create(
    amount=123, currency="string", financial_account="string"
)
```

### cancel <a name="cancel"></a>
Cancel an OutboundPayment

<p>Cancel an OutboundPayment.</p>

**API Endpoint**: `POST /v1/treasury/outbound_payments/{id}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.treasury.outbound_payment.cancel(id="string")
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
res = await client.treasury.outbound_payment.cancel(id="string")
```
