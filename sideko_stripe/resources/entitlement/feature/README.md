
### list <a name="list"></a>
List all features

<p>Retrieve a list of features</p>

**API Endpoint**: `GET /v1/entitlements/features`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.entitlement.feature.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.entitlement.feature.list()
```

### get <a name="get"></a>
Retrieve a feature

<p>Retrieves a feature</p>

**API Endpoint**: `GET /v1/entitlements/features/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.entitlement.feature.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.entitlement.feature.get(id="string")
```

### create <a name="create"></a>
Create a feature

<p>Creates a feature</p>

**API Endpoint**: `POST /v1/entitlements/features`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.entitlement.feature.create(lookup_key="string", name="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.entitlement.feature.create(lookup_key="string", name="string")
```

### update <a name="update"></a>
Updates a feature

<p>Update a feature’s metadata or permanently deactivate it.</p>

**API Endpoint**: `POST /v1/entitlements/features/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.entitlement.feature.update(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.entitlement.feature.update(id="string")
```
