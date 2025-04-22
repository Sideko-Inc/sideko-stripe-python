
### create_force_capture <a name="create_force_capture"></a>
Create a test-mode force capture

<p>Allows the user to capture an arbitrary amount, also known as a forced capture.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/transactions/create_force_capture`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.transaction.create_force_capture(
    amount=123, card="string"
)
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
res = await client.test_helper.issuing.transaction.create_force_capture(
    amount=123, card="string"
)
```

### create_unlinked_refund <a name="create_unlinked_refund"></a>
Create a test-mode unlinked refund

<p>Allows the user to refund an arbitrary amount, also known as a unlinked refund.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/transactions/create_unlinked_refund`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.transaction.create_unlinked_refund(
    amount=123, card="string"
)
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
res = await client.test_helper.issuing.transaction.create_unlinked_refund(
    amount=123, card="string"
)
```

### refund <a name="refund"></a>
Refund a test-mode transaction

<p>Refund a test-mode Transaction.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/transactions/{transaction}/refund`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.transaction.refund(transaction="string")
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
res = await client.test_helper.issuing.transaction.refund(transaction="string")
```
