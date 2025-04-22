
### list <a name="list"></a>
Retrieve a calculation's line items

<p>Retrieves the line items of a tax calculation as a collection, if the calculation hasn’t expired.</p>

**API Endpoint**: `GET /v1/tax/calculations/{calculation}/line_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.tax.calculations.line_item.list(calculation="string")
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
res = await client.tax.calculations.line_item.list(calculation="string")
```
