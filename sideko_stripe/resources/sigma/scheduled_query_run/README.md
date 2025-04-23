
### list <a name="list"></a>
List all scheduled query runs

<p>Returns a list of scheduled query runs.</p>

**API Endpoint**: `GET /v1/sigma/scheduled_query_runs`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.sigma.scheduled_query_run.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.sigma.scheduled_query_run.list()
```

### get <a name="get"></a>
Retrieve a scheduled query run

<p>Retrieves the details of an scheduled query run.</p>

**API Endpoint**: `GET /v1/sigma/scheduled_query_runs/{scheduled_query_run}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.sigma.scheduled_query_run.get(scheduled_query_run="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.sigma.scheduled_query_run.get(scheduled_query_run="string")
```
