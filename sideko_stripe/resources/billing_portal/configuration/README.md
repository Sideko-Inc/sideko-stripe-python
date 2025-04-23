
### list <a name="list"></a>
List portal configurations

<p>Returns a list of configurations that describe the functionality of the customer portal.</p>

**API Endpoint**: `GET /v1/billing_portal/configurations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing_portal.configuration.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing_portal.configuration.list()
```

### get <a name="get"></a>
Retrieve a portal configuration

<p>Retrieves a configuration that describes the functionality of the customer portal.</p>

**API Endpoint**: `GET /v1/billing_portal/configurations/{configuration}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing_portal.configuration.get(configuration="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing_portal.configuration.get(configuration="string")
```

### create <a name="create"></a>
Create a portal configuration

<p>Creates a configuration that describes the functionality and behavior of a PortalSession</p>

**API Endpoint**: `POST /v1/billing_portal/configurations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing_portal.configuration.create(features={})
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing_portal.configuration.create(features={})
```

### update <a name="update"></a>
Update a portal configuration

<p>Updates a configuration that describes the functionality of the customer portal.</p>

**API Endpoint**: `POST /v1/billing_portal/configurations/{configuration}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.billing_portal.configuration.update(configuration="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.billing_portal.configuration.update(configuration="string")
```
