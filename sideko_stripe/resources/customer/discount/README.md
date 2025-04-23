
### delete <a name="delete"></a>
Delete a customer discount

<p>Removes the currently applied discount on a customer.</p>

**API Endpoint**: `DELETE /v1/customers/{customer}/discount`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.discount.delete(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.discount.delete(customer="string")
```

### list <a name="list"></a>
GET /v1/customers/{customer}/discount



**API Endpoint**: `GET /v1/customers/{customer}/discount`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.discount.list(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.discount.list(customer="string")
```
