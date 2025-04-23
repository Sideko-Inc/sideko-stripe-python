
### list <a name="list"></a>
List a Customer's PaymentMethods

<p>Returns a list of PaymentMethods for a given Customer</p>

**API Endpoint**: `GET /v1/customers/{customer}/payment_methods`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.payment_method.list(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.payment_method.list(customer="string")
```

### get <a name="get"></a>
Retrieve a Customer's PaymentMethod

<p>Retrieves a PaymentMethod object for a given Customer.</p>

**API Endpoint**: `GET /v1/customers/{customer}/payment_methods/{payment_method}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.payment_method.get(customer="string", payment_method="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.payment_method.get(
    customer="string", payment_method="string"
)
```
