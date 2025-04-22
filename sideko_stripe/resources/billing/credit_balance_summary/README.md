
### get <a name="get"></a>
Retrieve the credit balance summary for a customer

<p>Retrieves the credit balance summary for a customer.</p>

**API Endpoint**: `GET /v1/billing/credit_balance_summary`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.credit_balance_summary.get(
    customer="string", filter={"type_": "applicability_scope"}
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
res = await client.billing.credit_balance_summary.get(
    customer="string", filter={"type_": "applicability_scope"}
)
```
