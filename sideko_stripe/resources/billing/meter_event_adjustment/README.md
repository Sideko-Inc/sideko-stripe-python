
### create <a name="create"></a>
Create a billing meter event adjustment

<p>Creates a billing meter event adjustment.</p>

**API Endpoint**: `POST /v1/billing/meter_event_adjustments`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.billing.meter_event_adjustment.create(event_name="string", type_="cancel")
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
res = await client.billing.meter_event_adjustment.create(
    event_name="string", type_="cancel"
)
```
