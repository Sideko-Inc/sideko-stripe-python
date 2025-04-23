
### create <a name="create"></a>
Create an Account Session

<p>Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.</p>

**API Endpoint**: `POST /v1/account_sessions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account_sessions.create(account="string", components={})
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account_sessions.create(account="string", components={})
```
