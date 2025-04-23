
### list <a name="list"></a>
List all payments for an invoice

<p>When retrieving an invoice, there is an includable payments property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of payments.</p>

**API Endpoint**: `GET /v1/invoice_payments`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.invoice_payment.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.invoice_payment.list()
```

### get <a name="get"></a>
Retrieve an InvoicePayment

<p>Retrieves the invoice payment with the given ID.</p>

**API Endpoint**: `GET /v1/invoice_payments/{invoice_payment}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.invoice_payment.get(invoice_payment="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.invoice_payment.get(invoice_payment="string")
```
