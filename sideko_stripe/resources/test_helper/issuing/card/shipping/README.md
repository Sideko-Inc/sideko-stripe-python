
### deliver <a name="deliver"></a>
Deliver a testmode card

<p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>delivered</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/cards/{card}/shipping/deliver`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.card.shipping.deliver(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.card.shipping.deliver(card="string")
```

### fail <a name="fail"></a>
Fail a testmode card

<p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>failure</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/cards/{card}/shipping/fail`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.card.shipping.fail(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.card.shipping.fail(card="string")
```

### returned <a name="returned"></a>
Return a testmode card

<p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>returned</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/cards/{card}/shipping/return`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.card.shipping.returned(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.card.shipping.returned(card="string")
```

### ship <a name="ship"></a>
Ship a testmode card

<p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>shipped</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/cards/{card}/shipping/ship`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.card.shipping.ship(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.card.shipping.ship(card="string")
```

### submit <a name="submit"></a>
Submit a testmode card

<p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>submitted</code>. This method requires Stripe Version ‘2024-09-30.acacia’ or later.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/cards/{card}/shipping/submit`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.card.shipping.submit(card="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.card.shipping.submit(card="string")
```
