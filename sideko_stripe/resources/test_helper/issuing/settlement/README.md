
### create <a name="create"></a>
Create a test-mode settlement

<p>Allows the user to create an Issuing settlement.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/settlements`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.settlement.create(
    bin="string", clearing_date=123, currency="string", net_total_amount=123
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
res = await client.test_helper.issuing.settlement.create(
    bin="string", clearing_date=123, currency="string", net_total_amount=123
)
```

### complete <a name="complete"></a>
Complete a test-mode settlement

<p>Allows the user to mark an Issuing settlement as complete.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/settlements/{settlement}/complete`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.settlement.complete(settlement="string")
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
res = await client.test_helper.issuing.settlement.complete(settlement="string")
```
