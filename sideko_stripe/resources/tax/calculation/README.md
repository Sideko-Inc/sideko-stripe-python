
### get <a name="get"></a>
Retrieve a Tax Calculation

<p>Retrieves a Tax <code>Calculation</code> object, if the calculation hasn’t expired.</p>

**API Endpoint**: `GET /v1/tax/calculations/{calculation}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.calculation.get(calculation="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.calculation.get(calculation="string")
```

### create <a name="create"></a>
Create a Tax Calculation

<p>Calculates tax based on the input and returns a Tax <code>Calculation</code> object.</p>

**API Endpoint**: `POST /v1/tax/calculations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.calculation.create(currency="string", line_items=[{"amount": 123}])
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.calculation.create(
    currency="string", line_items=[{"amount": 123}]
)
```
