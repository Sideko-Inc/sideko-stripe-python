
### expire <a name="expire"></a>
Expire a pending refund.

<p>Expire a refund with a status of <code>requires_action</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/refunds/{refund}/expire`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.refund.expire(refund="string")
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
res = await client.test_helper.refund.expire(refund="string")
```
