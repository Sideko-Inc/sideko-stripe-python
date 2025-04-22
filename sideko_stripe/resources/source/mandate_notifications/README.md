
### get <a name="get"></a>
Retrieve a Source MandateNotification

<p>Retrieves a new Source MandateNotification.</p>

**API Endpoint**: `GET /v1/sources/{source}/mandate_notifications/{mandate_notification}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.source.mandate_notifications.get(
    mandate_notification="string", source="string"
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
res = await client.source.mandate_notifications.get(
    mandate_notification="string", source="string"
)
```
