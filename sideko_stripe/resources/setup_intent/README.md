
### list <a name="list"></a>
List all SetupIntents

<p>Returns a list of SetupIntents.</p>

**API Endpoint**: `GET /v1/setup_intents`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.setup_intent.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.setup_intent.list()
```

### get <a name="get"></a>
Retrieve a SetupIntent

<p>Retrieves the details of a SetupIntent that has previously been created. </p>

<p>Client-side retrieval using a publishable key is allowed when the <code>client_secret</code> is provided in the query string. </p>

<p>When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the <a href="#setup_intent_object">SetupIntent</a> object reference for more details.</p>

**API Endpoint**: `GET /v1/setup_intents/{intent}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.setup_intent.get(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.setup_intent.get(intent="string")
```

### create <a name="create"></a>
Create a SetupIntent

<p>Creates a SetupIntent object.</p>

<p>After you create the SetupIntent, attach a payment method and <a href="/docs/api/setup_intents/confirm">confirm</a>
it to collect any required permissions to charge the payment method later.</p>

**API Endpoint**: `POST /v1/setup_intents`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.setup_intent.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.setup_intent.create()
```

### update <a name="update"></a>
Update a SetupIntent

<p>Updates a SetupIntent object.</p>

**API Endpoint**: `POST /v1/setup_intents/{intent}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.setup_intent.update(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.setup_intent.update(intent="string")
```

### cancel <a name="cancel"></a>
Cancel a SetupIntent

<p>You can cancel a SetupIntent object when it’s in one of these statuses: <code>requires_payment_method</code>, <code>requires_confirmation</code>, or <code>requires_action</code>. </p>

<p>After you cancel it, setup is abandoned and any operations on the SetupIntent fail with an error. You can’t cancel the SetupIntent for a Checkout Session. <a href="/docs/api/checkout/sessions/expire">Expire the Checkout Session</a> instead.</p>

**API Endpoint**: `POST /v1/setup_intents/{intent}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.setup_intent.cancel(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.setup_intent.cancel(intent="string")
```

### confirm <a name="confirm"></a>
Confirm a SetupIntent

<p>Confirm that your customer intends to set up the current or
provided payment method. For example, you would confirm a SetupIntent
when a customer hits the “Save” button on a payment method management
page on your website.</p>

<p>If the selected payment method does not require any additional
steps from the customer, the SetupIntent will transition to the
<code>succeeded</code> status.</p>

<p>Otherwise, it will transition to the <code>requires_action</code> status and
suggest additional actions via <code>next_action</code>. If setup fails,
the SetupIntent will transition to the
<code>requires_payment_method</code> status or the <code>canceled</code> status if the
confirmation limit is reached.</p>

**API Endpoint**: `POST /v1/setup_intents/{intent}/confirm`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.setup_intent.confirm(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.setup_intent.confirm(intent="string")
```

### verify_microdeposits <a name="verify_microdeposits"></a>
Verify microdeposits on a SetupIntent

<p>Verifies microdeposits on a SetupIntent object.</p>

**API Endpoint**: `POST /v1/setup_intents/{intent}/verify_microdeposits`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.setup_intent.verify_microdeposits(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.setup_intent.verify_microdeposits(intent="string")
```
