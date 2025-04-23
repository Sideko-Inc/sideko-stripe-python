
### list <a name="list"></a>
List all Checkout Sessions

<p>Returns a list of Checkout Sessions.</p>

**API Endpoint**: `GET /v1/checkout/sessions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.checkout.session.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.checkout.session.list()
```

### get <a name="get"></a>
Retrieve a Checkout Session

<p>Retrieves a Checkout Session object.</p>

**API Endpoint**: `GET /v1/checkout/sessions/{session}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.checkout.session.get(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.checkout.session.get(session="string")
```

### create <a name="create"></a>
Create a Checkout Session

<p>Creates a Checkout Session object.</p>

**API Endpoint**: `POST /v1/checkout/sessions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.checkout.session.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.checkout.session.create()
```

### update <a name="update"></a>
Update a Checkout Session

<p>Updates a Checkout Session object.</p>

**API Endpoint**: `POST /v1/checkout/sessions/{session}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.checkout.session.update(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.checkout.session.update(session="string")
```

### expire <a name="expire"></a>
Expire a Checkout Session

<p>A Checkout Session can be expired when it is in one of these statuses: <code>open</code> </p>

<p>After it expires, a customer can’t complete a Checkout Session and customers loading the Checkout Session see a message saying the Checkout Session is expired.</p>

**API Endpoint**: `POST /v1/checkout/sessions/{session}/expire`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.checkout.session.expire(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.checkout.session.expire(session="string")
```
