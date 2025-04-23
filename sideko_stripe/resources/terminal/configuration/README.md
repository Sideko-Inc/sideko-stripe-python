
### delete <a name="delete"></a>
Delete a Configuration

<p>Deletes a <code>Configuration</code> object.</p>

**API Endpoint**: `DELETE /v1/terminal/configurations/{configuration}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.configuration.delete(configuration="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.configuration.delete(configuration="string")
```

### list <a name="list"></a>
List all Configurations

<p>Returns a list of <code>Configuration</code> objects.</p>

**API Endpoint**: `GET /v1/terminal/configurations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.configuration.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.configuration.list()
```

### get <a name="get"></a>
Retrieve a Configuration

<p>Retrieves a <code>Configuration</code> object.</p>

**API Endpoint**: `GET /v1/terminal/configurations/{configuration}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.configuration.get(configuration="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.configuration.get(configuration="string")
```

### create <a name="create"></a>
Create a Configuration

<p>Creates a new <code>Configuration</code> object.</p>

**API Endpoint**: `POST /v1/terminal/configurations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.configuration.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.configuration.create()
```

### update <a name="update"></a>
Update a Configuration

<p>Updates a new <code>Configuration</code> object.</p>

**API Endpoint**: `POST /v1/terminal/configurations/{configuration}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.configuration.update(configuration="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.configuration.update(configuration="string")
```
