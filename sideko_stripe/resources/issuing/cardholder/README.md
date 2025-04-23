
### list <a name="list"></a>
List all cardholders

<p>Returns a list of Issuing <code>Cardholder</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

**API Endpoint**: `GET /v1/issuing/cardholders`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.cardholder.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.cardholder.list()
```

### get <a name="get"></a>
Retrieve a cardholder

<p>Retrieves an Issuing <code>Cardholder</code> object.</p>

**API Endpoint**: `GET /v1/issuing/cardholders/{cardholder}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.cardholder.get(cardholder="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.cardholder.get(cardholder="string")
```

### create <a name="create"></a>
Create a cardholder

<p>Creates a new Issuing <code>Cardholder</code> object that can be issued cards.</p>

**API Endpoint**: `POST /v1/issuing/cardholders`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.cardholder.create(
    billing={
        "address": {
            "city": "string",
            "country": "string",
            "line1": "string",
            "postal_code": "string",
        }
    },
    name="string",
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.cardholder.create(
    billing={
        "address": {
            "city": "string",
            "country": "string",
            "line1": "string",
            "postal_code": "string",
        }
    },
    name="string",
)
```

### update <a name="update"></a>
Update a cardholder

<p>Updates the specified Issuing <code>Cardholder</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

**API Endpoint**: `POST /v1/issuing/cardholders/{cardholder}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.cardholder.update(cardholder="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.cardholder.update(cardholder="string")
```
