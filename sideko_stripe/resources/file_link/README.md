
### list <a name="list"></a>
List all file links

<p>Returns a list of file links.</p>

**API Endpoint**: `GET /v1/file_links`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.file_link.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.file_link.list()
```

### get <a name="get"></a>
Retrieve a file link

<p>Retrieves the file link with the given ID.</p>

**API Endpoint**: `GET /v1/file_links/{link}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.file_link.get(link="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.file_link.get(link="string")
```

### create <a name="create"></a>
Create a file link

<p>Creates a new file link object.</p>

**API Endpoint**: `POST /v1/file_links`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.file_link.create(file="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.file_link.create(file="string")
```

### update <a name="update"></a>
Update a file link

<p>Updates an existing file link object. Expired links can no longer be updated.</p>

**API Endpoint**: `POST /v1/file_links/{link}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.file_link.update(link="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.file_link.update(link="string")
```
