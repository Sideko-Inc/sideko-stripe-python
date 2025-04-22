
### delete <a name="delete"></a>
Delete a test clock

<p>Deletes a test clock.</p>

**API Endpoint**: `DELETE /v1/test_helpers/test_clocks/{test_clock}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.test_clock.delete(test_clock="string")
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
res = await client.test_helper.test_clock.delete(test_clock="string")
```

### list <a name="list"></a>
List all test clocks

<p>Returns a list of your test clocks.</p>

**API Endpoint**: `GET /v1/test_helpers/test_clocks`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.test_clock.list()
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
res = await client.test_helper.test_clock.list()
```

### get <a name="get"></a>
Retrieve a test clock

<p>Retrieves a test clock.</p>

**API Endpoint**: `GET /v1/test_helpers/test_clocks/{test_clock}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.test_clock.get(test_clock="string")
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
res = await client.test_helper.test_clock.get(test_clock="string")
```

### create <a name="create"></a>
Create a test clock

<p>Creates a new test clock that can be attached to new customers and quotes.</p>

**API Endpoint**: `POST /v1/test_helpers/test_clocks`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.test_clock.create(frozen_time=123)
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
res = await client.test_helper.test_clock.create(frozen_time=123)
```

### advance <a name="advance"></a>
Advance a test clock

<p>Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to <code>Ready</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/test_clocks/{test_clock}/advance`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.test_clock.advance(frozen_time=123, test_clock="string")
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
res = await client.test_helper.test_clock.advance(frozen_time=123, test_clock="string")
```
