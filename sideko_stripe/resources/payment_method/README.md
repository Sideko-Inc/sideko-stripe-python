
### list <a name="list"></a>
List PaymentMethods

<p>Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the <a href="/docs/api/payment_methods/customer_list">List a Customer’s PaymentMethods</a> API instead.</p>

**API Endpoint**: `GET /v1/payment_methods`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method.list()
```

### get <a name="get"></a>
Retrieve a PaymentMethod

<p>Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use <a href="/docs/api/payment_methods/customer">Retrieve a Customer’s PaymentMethods</a></p>

**API Endpoint**: `GET /v1/payment_methods/{payment_method}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method.get(payment_method="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method.get(payment_method="string")
```

### create <a name="create"></a>
Shares a PaymentMethod

<p>Creates a PaymentMethod object. Read the <a href="/docs/stripe-js/reference#stripe-create-payment-method">Stripe.js reference</a> to learn how to create PaymentMethods via Stripe.js.</p>

<p>Instead of creating a PaymentMethod directly, we recommend using the <a href="/docs/payments/accept-a-payment">PaymentIntents</a> API to accept a payment immediately or the <a href="/docs/payments/save-and-reuse">SetupIntent</a> API to collect payment method details ahead of a future payment.</p>

**API Endpoint**: `POST /v1/payment_methods`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method.create()
```

### update <a name="update"></a>
Update a PaymentMethod

<p>Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.</p>

**API Endpoint**: `POST /v1/payment_methods/{payment_method}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method.update(payment_method="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method.update(payment_method="string")
```

### attach <a name="attach"></a>
Attach a PaymentMethod to a Customer

<p>Attaches a PaymentMethod object to a Customer.</p>

<p>To attach a new PaymentMethod to a customer for future payments, we recommend you use a <a href="/docs/api/setup_intents">SetupIntent</a>
or a PaymentIntent with <a href="/docs/api/payment_intents/create#create_payment_intent-setup_future_usage">setup_future_usage</a>.
These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the <code>/v1/payment_methods/:id/attach</code>
endpoint without first using a SetupIntent or PaymentIntent with <code>setup_future_usage</code> does not optimize the PaymentMethod for
future use, which makes later declines and payment friction more likely.
See <a href="/docs/payments/payment-intents#future-usage">Optimizing cards for future payments</a> for more information about setting up
future payments.</p>

<p>To use this PaymentMethod as the default for invoice or subscription payments,
set <a href="/docs/api/customers/update#update_customer-invoice_settings-default_payment_method"><code>invoice_settings.default_payment_method</code></a>,
on the Customer to the PaymentMethod’s ID.</p>

**API Endpoint**: `POST /v1/payment_methods/{payment_method}/attach`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method.attach(customer="string", payment_method="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method.attach(customer="string", payment_method="string")
```

### detach <a name="detach"></a>
Detach a PaymentMethod from a Customer

<p>Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.</p>

**API Endpoint**: `POST /v1/payment_methods/{payment_method}/detach`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method.detach(payment_method="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method.detach(payment_method="string")
```
