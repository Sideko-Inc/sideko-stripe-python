
### list <a name="list"></a>
Retrieve a Checkout Session's line items

<p>When retrieving a Checkout Session, there is an includable <strong>line_items</strong> property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

**API Endpoint**: `GET /v1/checkout/sessions/{session}/line_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.checkout.session.line_items.list(session="string")
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
res = await client.checkout.session.line_items.list(session="string")
```
