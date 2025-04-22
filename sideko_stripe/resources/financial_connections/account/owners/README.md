
### list <a name="list"></a>
List Account Owners

<p>Lists all owners for a given <code>Account</code></p>

**API Endpoint**: `GET /v1/financial_connections/accounts/{account}/owners`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.financial_connections.account.owners.list(
    account="string", ownership="string"
)
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
res = await client.financial_connections.account.owners.list(
    account="string", ownership="string"
)
```
