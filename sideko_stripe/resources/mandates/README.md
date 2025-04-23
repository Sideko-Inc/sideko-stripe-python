
### get <a name="get"></a>
Retrieve a Mandate

<p>Retrieves a Mandate object.</p>

**API Endpoint**: `GET /v1/mandates/{mandate}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.mandates.get(mandate="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.mandates.get(mandate="string")
```
