
### create <a name="create"></a>
Create a portal session

<p>Creates a session of the customer portal.</p>

**API Endpoint**: `POST /v1/billing_portal/sessions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing_portal.session.create(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing_portal.session.create(customer="string")
```
