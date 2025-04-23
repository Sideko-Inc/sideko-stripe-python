
### delete <a name="delete"></a>
Delete a Location

<p>Deletes a <code>Location</code> object.</p>

**API Endpoint**: `DELETE /v1/terminal/locations/{location}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.location.delete(location="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.location.delete(location="string")
```

### list <a name="list"></a>
List all Locations

<p>Returns a list of <code>Location</code> objects.</p>

**API Endpoint**: `GET /v1/terminal/locations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.location.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.location.list()
```

### get <a name="get"></a>
Retrieve a Location

<p>Retrieves a <code>Location</code> object.</p>

**API Endpoint**: `GET /v1/terminal/locations/{location}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.location.get(location="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.location.get(location="string")
```

### create <a name="create"></a>
Create a Location

<p>Creates a new <code>Location</code> object.
For further details, including which address fields are required in each country, see the <a href="/docs/terminal/fleet/locations">Manage locations</a> guide.</p>

**API Endpoint**: `POST /v1/terminal/locations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.location.create(
    address={"country": "string"}, display_name="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.location.create(
    address={"country": "string"}, display_name="string"
)
```

### update <a name="update"></a>
Update a Location

<p>Updates a <code>Location</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

**API Endpoint**: `POST /v1/terminal/locations/{location}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.location.update(location="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.location.update(location="string")
```
