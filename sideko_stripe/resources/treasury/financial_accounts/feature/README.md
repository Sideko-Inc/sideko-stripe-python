
### list <a name="list"></a>
Retrieve FinancialAccount Features

<p>Retrieves Features information associated with the FinancialAccount.</p>

**API Endpoint**: `GET /v1/treasury/financial_accounts/{financial_account}/features`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.financial_accounts.feature.list(financial_account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.financial_accounts.feature.list(financial_account="string")
```

### create <a name="create"></a>
Update FinancialAccount Features

<p>Updates the Features associated with a FinancialAccount.</p>

**API Endpoint**: `POST /v1/treasury/financial_accounts/{financial_account}/features`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.treasury.financial_accounts.feature.create(financial_account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.treasury.financial_accounts.feature.create(
    financial_account="string"
)
```
