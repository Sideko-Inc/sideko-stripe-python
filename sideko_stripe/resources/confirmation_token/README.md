
### get <a name="get"></a>
Retrieve a ConfirmationToken

<p>Retrieves an existing ConfirmationToken object</p>

**API Endpoint**: `GET /v1/confirmation_tokens/{confirmation_token}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.confirmation_token.get(confirmation_token="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.confirmation_token.get(confirmation_token="string")
```
