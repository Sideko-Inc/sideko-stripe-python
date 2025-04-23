
### create <a name="create"></a>
Test mode: Create a ReceivedDebit

<p>Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/received_debits`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.treasury.received_debit.create(
    amount=123, currency="string", financial_account="string", network="ach"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.treasury.received_debit.create(
    amount=123, currency="string", financial_account="string", network="ach"
)
```
