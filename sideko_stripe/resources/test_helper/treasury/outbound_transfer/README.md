
### update <a name="update"></a>
Test mode: Update an OutboundTransfer

<p>Updates a test mode created OutboundTransfer with tracking details. The OutboundTransfer must not be cancelable, and cannot be in the <code>canceled</code> or <code>failed</code> states.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.treasury.outbound_transfer.update(
    outbound_transfer="string", tracking_details={"type_": "ach"}
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
res = await client.test_helper.treasury.outbound_transfer.update(
    outbound_transfer="string", tracking_details={"type_": "ach"}
)
```

### fail <a name="fail"></a>
Test mode: Fail an OutboundTransfer

<p>Transitions a test mode created OutboundTransfer to the <code>failed</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.treasury.outbound_transfer.fail(outbound_transfer="string")
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
res = await client.test_helper.treasury.outbound_transfer.fail(
    outbound_transfer="string"
)
```

### post <a name="post"></a>
Test mode: Post an OutboundTransfer

<p>Transitions a test mode created OutboundTransfer to the <code>posted</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.treasury.outbound_transfer.post(outbound_transfer="string")
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
res = await client.test_helper.treasury.outbound_transfer.post(
    outbound_transfer="string"
)
```

### returned <a name="returned"></a>
Test mode: Return an OutboundTransfer

<p>Transitions a test mode created OutboundTransfer to the <code>returned</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.treasury.outbound_transfer.returned(outbound_transfer="string")
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
res = await client.test_helper.treasury.outbound_transfer.returned(
    outbound_transfer="string"
)
```
