
### create <a name="create"></a>
Create a test Confirmation Token

<p>Creates a test mode Confirmation Token server side for your integration tests.</p>

**API Endpoint**: `POST /v1/test_helpers/confirmation_tokens`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.confirmation_token.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.confirmation_token.create()
```
