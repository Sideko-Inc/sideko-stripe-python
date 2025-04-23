
### fund_cash_balance <a name="fund_cash_balance"></a>
Fund a test mode cash balance

<p>Create an incoming testmode bank transfer</p>

**API Endpoint**: `POST /v1/test_helpers/customers/{customer}/fund_cash_balance`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.customer.fund_cash_balance(
    amount=123, currency="string", customer="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.customer.fund_cash_balance(
    amount=123, currency="string", customer="string"
)
```
