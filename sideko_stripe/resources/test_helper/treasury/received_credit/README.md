
### create <a name="create"></a>
Test mode: Create a ReceivedCredit

<p>Use this endpoint to simulate a test mode ReceivedCredit initiated by a third party. In live mode, you can’t directly create ReceivedCredits initiated by third parties.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/received_credits`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.treasury.received_credit.create(
    amount=123, currency="string", financial_account="string", network="ach"
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
res = await client.test_helper.treasury.received_credit.create(
    amount=123, currency="string", financial_account="string", network="ach"
)
```
