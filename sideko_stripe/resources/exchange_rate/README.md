
### list <a name="list"></a>
List all exchange rates

<p>Returns a list of objects that contain the rates at which foreign currencies are converted to one another. Only shows the currencies for which Stripe supports.</p>

**API Endpoint**: `GET /v1/exchange_rates`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.exchange_rate.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.exchange_rate.list()
```

### get <a name="get"></a>
Retrieve an exchange rate

<p>Retrieves the exchange rates from the given currency to every supported currency.</p>

**API Endpoint**: `GET /v1/exchange_rates/{rate_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.exchange_rate.get(rate_id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.exchange_rate.get(rate_id="string")
```
