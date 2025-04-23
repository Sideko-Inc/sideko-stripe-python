
### list <a name="list"></a>
List all cards

<p>Returns a list of Issuing <code>Card</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

**API Endpoint**: `GET /v1/issuing/cards`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.card.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.card.list()
```

### get <a name="get"></a>
Retrieve a card

<p>Retrieves an Issuing <code>Card</code> object.</p>

**API Endpoint**: `GET /v1/issuing/cards/{card}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.card.get(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.card.get(card="string")
```

### create <a name="create"></a>
Create a card

<p>Creates an Issuing <code>Card</code> object.</p>

**API Endpoint**: `POST /v1/issuing/cards`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.card.create(currency="string", type_="physical")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.card.create(currency="string", type_="physical")
```

### update <a name="update"></a>
Update a card

<p>Updates the specified Issuing <code>Card</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

**API Endpoint**: `POST /v1/issuing/cards/{card}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.card.update(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.card.update(card="string")
```
