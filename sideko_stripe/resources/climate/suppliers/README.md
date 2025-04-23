
### get <a name="get"></a>
Retrieve a supplier

<p>Retrieves a Climate supplier object.</p>

**API Endpoint**: `GET /v1/climate/suppliers/{supplier}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.suppliers.get(supplier="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.suppliers.get(supplier="string")
```
