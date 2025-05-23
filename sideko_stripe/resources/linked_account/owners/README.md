
### list <a name="list"></a>
List Account Owners

<p>Lists all owners for a given <code>Account</code></p>

**API Endpoint**: `GET /v1/linked_accounts/{account}/owners`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.linked_account.owners.list(account="string", ownership="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.linked_account.owners.list(account="string", ownership="string")
```
