
### fail <a name="fail"></a>
Test mode: Fail an InboundTransfer

<p>Transitions a test mode created InboundTransfer to the <code>failed</code> status. The InboundTransfer must already be in the <code>processing</code> state.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/inbound_transfers/{id}/fail`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.treasury.inbound_transfers.fail(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.treasury.inbound_transfers.fail(id="string")
```

### returned <a name="returned"></a>
Test mode: Return an InboundTransfer

<p>Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the <code>succeeded</code> state.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/inbound_transfers/{id}/return`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.treasury.inbound_transfers.returned(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.treasury.inbound_transfers.returned(id="string")
```

### succeed <a name="succeed"></a>
Test mode: Succeed an InboundTransfer

<p>Transitions a test mode created InboundTransfer to the <code>succeeded</code> status. The InboundTransfer must already be in the <code>processing</code> state.</p>

**API Endpoint**: `POST /v1/test_helpers/treasury/inbound_transfers/{id}/succeed`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.treasury.inbound_transfers.succeed(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.treasury.inbound_transfers.succeed(id="string")
```
