
### delete <a name="delete"></a>
Delete a subscription item

<p>Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.</p>

**API Endpoint**: `DELETE /v1/subscription_items/{item}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription_item.delete(item="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription_item.delete(item="string")
```

### list <a name="list"></a>
List all subscription items

<p>Returns a list of your subscription items for a given subscription.</p>

**API Endpoint**: `GET /v1/subscription_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription_item.list(subscription="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription_item.list(subscription="string")
```

### get <a name="get"></a>
Retrieve a subscription item

<p>Retrieves the subscription item with the given ID.</p>

**API Endpoint**: `GET /v1/subscription_items/{item}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription_item.get(item="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription_item.get(item="string")
```

### create <a name="create"></a>
Create a subscription item

<p>Adds a new item to an existing subscription. No existing items will be changed or replaced.</p>

**API Endpoint**: `POST /v1/subscription_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription_item.create(subscription="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription_item.create(subscription="string")
```

### update <a name="update"></a>
Update a subscription item

<p>Updates the plan or quantity of an item on a current subscription.</p>

**API Endpoint**: `POST /v1/subscription_items/{item}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription_item.update(item="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription_item.update(item="string")
```
