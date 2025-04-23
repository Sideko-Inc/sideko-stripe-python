
### get <a name="get"></a>
Retrieve a transaction

<p>Retrieves a Tax <code>Transaction</code> object.</p>

**API Endpoint**: `GET /v1/tax/transactions/{transaction}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.transaction.get(transaction="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.transaction.get(transaction="string")
```

### create_from_calculation <a name="create_from_calculation"></a>
Create a transaction from a calculation

<p>Creates a Tax Transaction from a calculation, if that calculation hasn’t expired. Calculations expire after 90 days.</p>

**API Endpoint**: `POST /v1/tax/transactions/create_from_calculation`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.transaction.create_from_calculation(
    calculation="string", reference="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.transaction.create_from_calculation(
    calculation="string", reference="string"
)
```

### create_reversal <a name="create_reversal"></a>
Create a reversal transaction

<p>Partially or fully reverses a previously created <code>Transaction</code>.</p>

**API Endpoint**: `POST /v1/tax/transactions/create_reversal`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.transaction.create_reversal(
    mode="full", original_transaction="string", reference="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.transaction.create_reversal(
    mode="full", original_transaction="string", reference="string"
)
```
