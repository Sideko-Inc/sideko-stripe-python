
### get <a name="get"></a>
Retrieve a cash balance

<p>Retrieves a customer’s cash balance.</p>

**API Endpoint**: `GET /v1/customers/{customer}/cash_balance`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.customer.cash_balance.get(customer="string")
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
res = await client.customer.cash_balance.get(customer="string")
```

### modify <a name="modify"></a>
Update a cash balance's settings

<p>Changes the settings on a customer’s cash balance.</p>

**API Endpoint**: `POST /v1/customers/{customer}/cash_balance`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.customer.cash_balance.modify(customer="string")
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
res = await client.customer.cash_balance.modify(customer="string")
```
