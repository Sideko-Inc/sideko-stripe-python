
### list <a name="list"></a>
List suppliers

<p>Lists all available Climate supplier objects.</p>

**API Endpoint**: `GET /v1/climate/suppliers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.v1.climate.suppliers.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.v1.climate.suppliers.list()
```
