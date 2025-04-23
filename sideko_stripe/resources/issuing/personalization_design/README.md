
### list <a name="list"></a>
List all personalization designs

<p>Returns a list of personalization design objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

**API Endpoint**: `GET /v1/issuing/personalization_designs`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.personalization_design.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.personalization_design.list()
```

### get <a name="get"></a>
Retrieve a personalization design

<p>Retrieves a personalization design object.</p>

**API Endpoint**: `GET /v1/issuing/personalization_designs/{personalization_design}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.personalization_design.get(personalization_design="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.personalization_design.get(personalization_design="string")
```

### create <a name="create"></a>
Create a personalization design

<p>Creates a personalization design object.</p>

**API Endpoint**: `POST /v1/issuing/personalization_designs`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.personalization_design.create(physical_bundle="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.personalization_design.create(physical_bundle="string")
```

### update <a name="update"></a>
Update a personalization design

<p>Updates a card personalization object.</p>

**API Endpoint**: `POST /v1/issuing/personalization_designs/{personalization_design}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.issuing.personalization_design.update(personalization_design="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.issuing.personalization_design.update(
    personalization_design="string"
)
```
