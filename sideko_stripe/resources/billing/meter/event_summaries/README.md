
### list <a name="list"></a>
List billing meter event summaries

<p>Retrieve a list of billing meter event summaries.</p>

**API Endpoint**: `GET /v1/billing/meters/{id}/event_summaries`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.meter.event_summaries.list(
    customer="string", end_time=123, id="string", start_time=123
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.meter.event_summaries.list(
    customer="string", end_time=123, id="string", start_time=123
)
```
