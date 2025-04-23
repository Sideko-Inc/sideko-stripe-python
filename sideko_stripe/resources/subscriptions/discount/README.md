
### delete <a name="delete"></a>
Delete a subscription discount

<p>Removes the currently applied discount on a subscription.</p>

**API Endpoint**: `DELETE /v1/subscriptions/{subscription_exposed_id}/discount`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscriptions.discount.delete(subscription_exposed_id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscriptions.discount.delete(subscription_exposed_id="string")
```
