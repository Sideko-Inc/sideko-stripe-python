
### list <a name="list"></a>
List all early fraud warnings

<p>Returns a list of early fraud warnings.</p>

**API Endpoint**: `GET /v1/radar/early_fraud_warnings`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.radar.early_fraud_warning.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.radar.early_fraud_warning.list()
```

### get <a name="get"></a>
Retrieve an early fraud warning

<p>Retrieves the details of an early fraud warning that has previously been created. </p>

<p>Please refer to the <a href="#early_fraud_warning_object">early fraud warning</a> object reference for more details.</p>

**API Endpoint**: `GET /v1/radar/early_fraud_warnings/{early_fraud_warning}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.radar.early_fraud_warning.get(early_fraud_warning="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.radar.early_fraud_warning.get(early_fraud_warning="string")
```
