
### delete <a name="delete"></a>
Delete a customer source

<p>Delete a specified source for a given customer.</p>

**API Endpoint**: `DELETE /v1/customers/{customer}/sources/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.source.delete(customer="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.source.delete(customer="string", id="string")
```

### list <a name="list"></a>
GET /v1/customers/{customer}/sources

<p>List sources for a specified customer.</p>

**API Endpoint**: `GET /v1/customers/{customer}/sources`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.source.list(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.source.list(customer="string")
```

### get <a name="get"></a>
GET /v1/customers/{customer}/sources/{id}

<p>Retrieve a specified source for a given customer.</p>

**API Endpoint**: `GET /v1/customers/{customer}/sources/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.source.get(customer="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.source.get(customer="string", id="string")
```

### create <a name="create"></a>
Create a card

<p>When you create a new credit card, you must specify a customer or recipient on which to create it.</p>

<p>If the card’s owner has no default card, then the new card will become the default.
However, if the owner already has a default, then it will not change.
To change the default, you should <a href="/docs/api#update_customer">update the customer</a> to have a new <code>default_source</code>.</p>

**API Endpoint**: `POST /v1/customers/{customer}/sources`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.source.create(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.source.create(customer="string")
```

### update <a name="update"></a>
POST /v1/customers/{customer}/sources/{id}

<p>Update a specified source for a given customer.</p>

**API Endpoint**: `POST /v1/customers/{customer}/sources/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.source.update(customer="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.source.update(customer="string", id="string")
```

### verify <a name="verify"></a>
Verify a bank account

<p>Verify a specified bank account for a given customer.</p>

**API Endpoint**: `POST /v1/customers/{customer}/sources/{id}/verify`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.source.verify(customer="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.source.verify(customer="string", id="string")
```
