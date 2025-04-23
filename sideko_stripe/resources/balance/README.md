
### list <a name="list"></a>
Retrieve balance

<p>Retrieves the current account balance, based on the authentication that was used to make the request.
 For a sample request, see <a href="/docs/connect/account-balances#accounting-for-negative-balances">Accounting for negative balances</a>.</p>

**API Endpoint**: `GET /v1/balance`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.balance.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.balance.list()
```
