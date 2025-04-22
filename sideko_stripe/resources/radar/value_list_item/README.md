
### delete <a name="delete"></a>
Delete a value list item

<p>Deletes a <code>ValueListItem</code> object, removing it from its parent value list.</p>

**API Endpoint**: `DELETE /v1/radar/value_list_items/{item}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.radar.value_list_item.delete(item="string")
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
res = await client.radar.value_list_item.delete(item="string")
```

### list <a name="list"></a>
List all value list items

<p>Returns a list of <code>ValueListItem</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

**API Endpoint**: `GET /v1/radar/value_list_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.radar.value_list_item.list(value_list="string")
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
res = await client.radar.value_list_item.list(value_list="string")
```

### get <a name="get"></a>
Retrieve a value list item

<p>Retrieves a <code>ValueListItem</code> object.</p>

**API Endpoint**: `GET /v1/radar/value_list_items/{item}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.radar.value_list_item.get(item="string")
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
res = await client.radar.value_list_item.get(item="string")
```

### create <a name="create"></a>
Create a value list item

<p>Creates a new <code>ValueListItem</code> object, which is added to the specified parent value list.</p>

**API Endpoint**: `POST /v1/radar/value_list_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.radar.value_list_item.create(value="string", value_list="string")
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
res = await client.radar.value_list_item.create(value="string", value_list="string")
```
