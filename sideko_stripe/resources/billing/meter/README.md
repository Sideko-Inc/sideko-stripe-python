
### list <a name="list"></a>
List billing meters

<p>Retrieve a list of billing meters.</p>

**API Endpoint**: `GET /v1/billing/meters`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.meter.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.meter.list()
```

### get <a name="get"></a>
Retrieve a billing meter

<p>Retrieves a billing meter given an ID.</p>

**API Endpoint**: `GET /v1/billing/meters/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.meter.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.meter.get(id="string")
```

### create <a name="create"></a>
Create a billing meter

<p>Creates a billing meter.</p>

**API Endpoint**: `POST /v1/billing/meters`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.meter.create(
    default_aggregation={"formula": "count"}, display_name="string", event_name="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.meter.create(
    default_aggregation={"formula": "count"}, display_name="string", event_name="string"
)
```

### update <a name="update"></a>
Update a billing meter

<p>Updates a billing meter.</p>

**API Endpoint**: `POST /v1/billing/meters/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.meter.update(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.meter.update(id="string")
```

### deactivate <a name="deactivate"></a>
Deactivate a billing meter

<p>When a meter is deactivated, no more meter events will be accepted for this meter. You can’t attach a deactivated meter to a price.</p>

**API Endpoint**: `POST /v1/billing/meters/{id}/deactivate`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.meter.deactivate(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.meter.deactivate(id="string")
```

### reactivate <a name="reactivate"></a>
Reactivate a billing meter

<p>When a meter is reactivated, events for this meter can be accepted and you can attach the meter to a price.</p>

**API Endpoint**: `POST /v1/billing/meters/{id}/reactivate`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing.meter.reactivate(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing.meter.reactivate(id="string")
```
