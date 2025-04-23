
### delete <a name="delete"></a>
Cancel a subscription

<p>Cancels a customer’s subscription immediately. The customer won’t be charged again for the subscription. After it’s canceled, you can no longer update the subscription or its <a href="/metadata">metadata</a>.</p>

<p>Any pending invoice items that you’ve created are still charged at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations are also left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations are removed.</p>

<p>By default, upon subscription cancellation, Stripe stops automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

**API Endpoint**: `DELETE /v1/subscriptions/{subscription_exposed_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription.delete(subscription_exposed_id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription.delete(subscription_exposed_id="string")
```

### list <a name="list"></a>
List subscriptions

<p>By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify <code>status=canceled</code>.</p>

**API Endpoint**: `GET /v1/subscriptions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription.list()
```

### search <a name="search"></a>
Search subscriptions

<p>Search for subscriptions you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.</p>

**API Endpoint**: `GET /v1/subscriptions/search`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription.search(query="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription.search(query="string")
```

### get <a name="get"></a>
Retrieve a subscription

<p>Retrieves the subscription with the given ID.</p>

**API Endpoint**: `GET /v1/subscriptions/{subscription_exposed_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription.get(subscription_exposed_id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription.get(subscription_exposed_id="string")
```

### create <a name="create"></a>
Create a subscription

<p>Creates a new subscription on an existing customer. Each customer can have up to 500 active or scheduled subscriptions.</p>

<p>When you create a subscription with <code>collection_method=charge_automatically</code>, the first invoice is finalized as part of the request.
The <code>payment_behavior</code> parameter determines the exact behavior of the initial payment.</p>

<p>To start subscriptions where the first invoice always begins in a <code>draft</code> status, use <a href="/docs/billing/subscriptions/subscription-schedules#managing">subscription schedules</a> instead.
Schedules provide the flexibility to model more complex billing configurations that change over time.</p>

**API Endpoint**: `POST /v1/subscriptions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription.create(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription.create(customer="string")
```

### update <a name="update"></a>
Update a subscription

<p>Updates an existing subscription to match the specified parameters.
When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes.
To preview how the proration is calculated, use the <a href="/docs/api/invoices/create_preview">create preview</a> endpoint.</p>

<p>By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a <currency>100</currency> price, they’ll be billed <currency>100</currency> immediately. If on May 15 they switch to a <currency>200</currency> price, then on June 1 they’ll be billed <currency>250</currency> (<currency>200</currency> for a renewal of her subscription, plus a <currency>50</currency> prorating adjustment for half of the previous month’s <currency>100</currency> difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.</p>

<p>Switching prices does not normally change the billing date or generate an immediate charge unless:</p>

<ul>
<li>The billing interval is changed (for example, from monthly to yearly).</li>
<li>The subscription moves from free to paid.</li>
<li>A trial starts or ends.</li>
</ul>

<p>In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date. Learn about how <a href="/docs/billing/subscriptions/upgrade-downgrade#immediate-payment">Stripe immediately attempts payment for subscription changes</a>.</p>

<p>If you want to charge for an upgrade immediately, pass <code>proration_behavior</code> as <code>always_invoice</code> to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass <code>create_prorations</code>, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually <a href="/docs/api/invoices/create">invoice the customer</a>.</p>

<p>If you don’t want to prorate, set the <code>proration_behavior</code> option to <code>none</code>. With this option, the customer is billed <currency>100</currency> on May 1 and <currency>200</currency> on June 1. Similarly, if you set <code>proration_behavior</code> to <code>none</code> when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.</p>

<p>Updating the quantity on a subscription many times in an hour may result in <a href="/docs/rate-limits">rate limiting</a>. If you need to bill for a frequently changing quantity, consider integrating <a href="/docs/billing/subscriptions/usage-based">usage-based billing</a> instead.</p>

**API Endpoint**: `POST /v1/subscriptions/{subscription_exposed_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription.update(subscription_exposed_id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription.update(subscription_exposed_id="string")
```

### resume <a name="resume"></a>
Resume a subscription

<p>Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become <code>active</code>, and if payment fails the subscription will be <code>past_due</code>. The resumption invoice will void automatically if not paid by the expiration date.</p>

**API Endpoint**: `POST /v1/subscriptions/{subscription}/resume`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.subscription.resume(subscription="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.subscription.resume(subscription="string")
```
