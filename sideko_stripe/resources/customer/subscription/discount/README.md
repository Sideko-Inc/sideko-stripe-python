
### delete <a name="delete"></a>
Delete a customer discount

<p>Removes the currently applied discount on a customer.</p>

**API Endpoint**: `DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.subscription.discount.delete(
    customer="string", subscription_exposed_id="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.subscription.discount.delete(
    customer="string", subscription_exposed_id="string"
)
```

### list <a name="list"></a>
GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount



**API Endpoint**: `GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.subscription.discount.list(
    customer="string", subscription_exposed_id="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.subscription.discount.list(
    customer="string", subscription_exposed_id="string"
)
```
