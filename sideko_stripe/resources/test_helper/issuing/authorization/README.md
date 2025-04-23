
### create <a name="create"></a>
Create a test-mode authorization

<p>Create a test-mode authorization.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/authorizations`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.authorization.create(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.authorization.create(card="string")
```

### capture <a name="capture"></a>
Capture a test-mode authorization

<p>Capture a test-mode authorization.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/authorizations/{authorization}/capture`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.authorization.capture(authorization="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.authorization.capture(authorization="string")
```

### expire <a name="expire"></a>
Expire a test-mode authorization

<p>Expire a test-mode Authorization.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/authorizations/{authorization}/expire`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.authorization.expire(authorization="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.authorization.expire(authorization="string")
```

### finalize_amount <a name="finalize_amount"></a>
Finalize a test-mode authorization's amount

<p>Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.authorization.finalize_amount(
    authorization="string", final_amount=123
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.authorization.finalize_amount(
    authorization="string", final_amount=123
)
```

### increment <a name="increment"></a>
Increment a test-mode authorization

<p>Increment a test-mode Authorization.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/authorizations/{authorization}/increment`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.authorization.increment(
    authorization="string", increment_amount=123
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.authorization.increment(
    authorization="string", increment_amount=123
)
```

### reverse <a name="reverse"></a>
Reverse a test-mode authorization

<p>Reverse a test-mode Authorization.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/authorizations/{authorization}/reverse`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.authorization.reverse(authorization="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.authorization.reverse(authorization="string")
```
