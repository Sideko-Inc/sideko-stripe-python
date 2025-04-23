
### list <a name="list"></a>
List secrets

<p>List all secrets stored on the given scope.</p>

**API Endpoint**: `GET /v1/apps/secrets`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apps.secret.list(scope={"type_": "account"})
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apps.secret.list(scope={"type_": "account"})
```

### find <a name="find"></a>
Find a Secret

<p>Finds a secret in the secret store by name and scope.</p>

**API Endpoint**: `GET /v1/apps/secrets/find`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apps.secret.find(name="string", scope={"type_": "account"})
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apps.secret.find(name="string", scope={"type_": "account"})
```

### create <a name="create"></a>
Set a Secret

<p>Create or replace a secret in the secret store.</p>

**API Endpoint**: `POST /v1/apps/secrets`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apps.secret.create(
    name="string", payload="string", scope={"type_": "account"}
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apps.secret.create(
    name="string", payload="string", scope={"type_": "account"}
)
```

### delete <a name="delete"></a>
Delete a Secret

<p>Deletes a secret from the secret store by name and scope.</p>

**API Endpoint**: `POST /v1/apps/secrets/delete`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.apps.secret.delete(name="string", scope={"type_": "account"})
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.apps.secret.delete(name="string", scope={"type_": "account"})
```
