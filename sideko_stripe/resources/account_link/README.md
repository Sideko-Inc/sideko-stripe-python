
### create <a name="create"></a>
Create an account link

<p>Creates an AccountLink object that includes a single-use Stripe URL that the platform can redirect their user to in order to take them through the Connect Onboarding flow.</p>

**API Endpoint**: `POST /v1/account_links`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account_link.create(account="string", type_="account_onboarding")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account_link.create(account="string", type_="account_onboarding")
```
