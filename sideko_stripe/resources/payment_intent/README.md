
### list <a name="list"></a>
List all PaymentIntents

<p>Returns a list of PaymentIntents.</p>

**API Endpoint**: `GET /v1/payment_intents`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.list()
```

### search <a name="search"></a>
Search PaymentIntents

<p>Search for PaymentIntents you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.</p>

**API Endpoint**: `GET /v1/payment_intents/search`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.search(query="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.search(query="string")
```

### get <a name="get"></a>
Retrieve a PaymentIntent

<p>Retrieves the details of a PaymentIntent that has previously been created. </p>

<p>You can retrieve a PaymentIntent client-side using a publishable key when the <code>client_secret</code> is in the query string. </p>

<p>If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to the <a href="#payment_intent_object">payment intent</a> object reference for more details.</p>

**API Endpoint**: `GET /v1/payment_intents/{intent}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.get(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.get(intent="string")
```

### create <a name="create"></a>
Create a PaymentIntent

<p>Creates a PaymentIntent object.</p>

<p>After the PaymentIntent is created, attach a payment method and <a href="/docs/api/payment_intents/confirm">confirm</a>
to continue the payment. Learn more about <a href="/docs/payments/payment-intents">the available payment flows
with the Payment Intents API</a>.</p>

<p>When you use <code>confirm=true</code> during creation, it’s equivalent to creating
and confirming the PaymentIntent in the same call. You can use any parameters
available in the <a href="/docs/api/payment_intents/confirm">confirm API</a> when you supply
<code>confirm=true</code>.</p>

**API Endpoint**: `POST /v1/payment_intents`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.create(amount=123, currency="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.create(amount=123, currency="string")
```

### update <a name="update"></a>
Update a PaymentIntent

<p>Updates properties on a PaymentIntent object without confirming.</p>

<p>Depending on which properties you update, you might need to confirm the
PaymentIntent again. For example, updating the <code>payment_method</code>
always requires you to confirm the PaymentIntent again. If you prefer to
update and confirm at the same time, we recommend updating properties through
the <a href="/docs/api/payment_intents/confirm">confirm API</a> instead.</p>

**API Endpoint**: `POST /v1/payment_intents/{intent}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.update(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.update(intent="string")
```

### apply_customer_balance <a name="apply_customer_balance"></a>
Reconcile a customer_balance PaymentIntent

<p>Manually reconcile the remaining amount for a <code>customer_balance</code> PaymentIntent.</p>

**API Endpoint**: `POST /v1/payment_intents/{intent}/apply_customer_balance`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.apply_customer_balance(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.apply_customer_balance(intent="string")
```

### cancel <a name="cancel"></a>
Cancel a PaymentIntent

<p>You can cancel a PaymentIntent object when it’s in one of these statuses: <code>requires_payment_method</code>, <code>requires_capture</code>, <code>requires_confirmation</code>, <code>requires_action</code> or, <a href="/docs/payments/intents">in rare cases</a>, <code>processing</code>. </p>

<p>After it’s canceled, no additional charges are made by the PaymentIntent and any operations on the PaymentIntent fail with an error. For PaymentIntents with a <code>status</code> of <code>requires_capture</code>, the remaining <code>amount_capturable</code> is automatically refunded. </p>

<p>You can’t cancel the PaymentIntent for a Checkout Session. <a href="/docs/api/checkout/sessions/expire">Expire the Checkout Session</a> instead.</p>

**API Endpoint**: `POST /v1/payment_intents/{intent}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.cancel(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.cancel(intent="string")
```

### capture <a name="capture"></a>
Capture a PaymentIntent

<p>Capture the funds of an existing uncaptured PaymentIntent when its status is <code>requires_capture</code>.</p>

<p>Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.</p>

<p>Learn more about <a href="/docs/payments/capture-later">separate authorization and capture</a>.</p>

**API Endpoint**: `POST /v1/payment_intents/{intent}/capture`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.capture(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.capture(intent="string")
```

### confirm <a name="confirm"></a>
Confirm a PaymentIntent

<p>Confirm that your customer intends to pay with current or provided
payment method. Upon confirmation, the PaymentIntent will attempt to initiate
a payment.
If the selected payment method requires additional authentication steps, the
PaymentIntent will transition to the <code>requires_action</code> status and
suggest additional actions via <code>next_action</code>. If payment fails,
the PaymentIntent transitions to the <code>requires_payment_method</code> status or the
<code>canceled</code> status if the confirmation limit is reached. If
payment succeeds, the PaymentIntent will transition to the <code>succeeded</code>
status (or <code>requires_capture</code>, if <code>capture_method</code> is set to <code>manual</code>).
If the <code>confirmation_method</code> is <code>automatic</code>, payment may be attempted
using our <a href="/docs/stripe-js/reference#stripe-handle-card-payment">client SDKs</a>
and the PaymentIntent’s <a href="#payment_intent_object-client_secret">client_secret</a>.
After <code>next_action</code>s are handled by the client, no additional
confirmation is required to complete the payment.
If the <code>confirmation_method</code> is <code>manual</code>, all payment attempts must be
initiated using a secret key.
If any actions are required for the payment, the PaymentIntent will
return to the <code>requires_confirmation</code> state
after those actions are completed. Your server needs to then
explicitly re-confirm the PaymentIntent to initiate the next payment
attempt.
There is a variable upper limit on how many times a PaymentIntent can be confirmed.
After this limit is reached, any further calls to this endpoint will
transition the PaymentIntent to the <code>canceled</code> state.</p>

**API Endpoint**: `POST /v1/payment_intents/{intent}/confirm`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.confirm(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.confirm(intent="string")
```

### increment_authorization <a name="increment_authorization"></a>
Increment an authorization

<p>Perform an incremental authorization on an eligible
<a href="/docs/api/payment_intents/object">PaymentIntent</a>. To be eligible, the
PaymentIntent’s status must be <code>requires_capture</code> and
<a href="/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported">incremental_authorization_supported</a>
must be <code>true</code>.</p>

<p>Incremental authorizations attempt to increase the authorized amount on
your customer’s card to the new, higher <code>amount</code> provided. Similar to the
initial authorization, incremental authorizations can be declined. A
single PaymentIntent can call this endpoint multiple times to further
increase the authorized amount.</p>

<p>If the incremental authorization succeeds, the PaymentIntent object
returns with the updated
<a href="/docs/api/payment_intents/object#payment_intent_object-amount">amount</a>.
If the incremental authorization fails, a
<a href="/docs/error-codes#card-declined">card_declined</a> error returns, and no other
fields on the PaymentIntent or Charge update. The PaymentIntent
object remains capturable for the previously authorized amount.</p>

<p>Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines.
After it’s captured, a PaymentIntent can no longer be incremented.</p>

<p>Learn more about <a href="/docs/terminal/features/incremental-authorizations">incremental authorizations</a>.</p>

**API Endpoint**: `POST /v1/payment_intents/{intent}/increment_authorization`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.increment_authorization(amount=123, intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.increment_authorization(amount=123, intent="string")
```

### verify_microdeposits <a name="verify_microdeposits"></a>
Verify microdeposits on a PaymentIntent

<p>Verifies microdeposits on a PaymentIntent object.</p>

**API Endpoint**: `POST /v1/payment_intents/{intent}/verify_microdeposits`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_intent.verify_microdeposits(intent="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_intent.verify_microdeposits(intent="string")
```
