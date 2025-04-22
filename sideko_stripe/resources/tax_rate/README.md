
### list <a name="list"></a>
List all tax rates

<p>Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.</p>

**API Endpoint**: `GET /v1/tax_rates`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.tax_rate.list()
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
res = await client.tax_rate.list()
```

### get <a name="get"></a>
Retrieve a tax rate

<p>Retrieves a tax rate with the given ID</p>

**API Endpoint**: `GET /v1/tax_rates/{tax_rate}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.tax_rate.get(tax_rate="string")
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
res = await client.tax_rate.get(tax_rate="string")
```

### create <a name="create"></a>
Create a tax rate

<p>Creates a new tax rate.</p>

**API Endpoint**: `POST /v1/tax_rates`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.tax_rate.create(display_name="string", inclusive=True, percentage=123.45)
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
res = await client.tax_rate.create(
    display_name="string", inclusive=True, percentage=123.45
)
```

### update <a name="update"></a>
Update a tax rate

<p>Updates an existing tax rate.</p>

**API Endpoint**: `POST /v1/tax_rates/{tax_rate}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.tax_rate.update(tax_rate="string")
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
res = await client.tax_rate.update(tax_rate="string")
```
