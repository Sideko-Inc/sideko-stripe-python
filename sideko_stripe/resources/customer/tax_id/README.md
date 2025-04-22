
### delete <a name="delete"></a>
Delete a Customer tax ID

<p>Deletes an existing <code>tax_id</code> object.</p>

**API Endpoint**: `DELETE /v1/customers/{customer}/tax_ids/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.customer.tax_id.delete(customer="string", id="string")
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
res = await client.customer.tax_id.delete(customer="string", id="string")
```

### list <a name="list"></a>
List all Customer tax IDs

<p>Returns a list of tax IDs for a customer.</p>

**API Endpoint**: `GET /v1/customers/{customer}/tax_ids`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.customer.tax_id.list(customer="string")
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
res = await client.customer.tax_id.list(customer="string")
```

### get <a name="get"></a>
Retrieve a Customer tax ID

<p>Retrieves the <code>tax_id</code> object with the given identifier.</p>

**API Endpoint**: `GET /v1/customers/{customer}/tax_ids/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.customer.tax_id.get(customer="string", id="string")
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
res = await client.customer.tax_id.get(customer="string", id="string")
```

### create <a name="create"></a>
Create a Customer tax ID

<p>Creates a new <code>tax_id</code> object for a customer.</p>

**API Endpoint**: `POST /v1/customers/{customer}/tax_ids`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.customer.tax_id.create(customer="string", type_="ad_nrt", value="string")
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
res = await client.customer.tax_id.create(
    customer="string", type_="ad_nrt", value="string"
)
```
