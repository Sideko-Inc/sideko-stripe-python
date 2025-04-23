
### delete <a name="delete"></a>
Cancel a subscription

<p>Cancels a customer’s subscription. If you set the <code>at_period_end</code> parameter to <code>true</code>, the subscription will remain active until the end of the period, at which point it will be canceled and not renewed. Otherwise, with the default <code>false</code> value, the subscription is terminated immediately. In either case, the customer will not be charged again for the subscription.</p>

<p>Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.</p>

<p>By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

**API Endpoint**: `DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.subscription.delete(
    customer="string", subscription_exposed_id="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.subscription.delete(
    customer="string", subscription_exposed_id="string"
)
```

### list <a name="list"></a>
List active subscriptions

<p>You can see a list of the customer’s active subscriptions. Note that the 10 most recent active subscriptions are always available by default on the customer object. If you need more than those 10, you can use the limit and starting_after parameters to page through additional subscriptions.</p>

**API Endpoint**: `GET /v1/customers/{customer}/subscriptions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.subscription.list(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.subscription.list(customer="string")
```

### get <a name="get"></a>
Retrieve a subscription

<p>Retrieves the subscription with the given ID.</p>

**API Endpoint**: `GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.subscription.get(
    customer="string", subscription_exposed_id="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.subscription.get(
    customer="string", subscription_exposed_id="string"
)
```

### create <a name="create"></a>
Create a subscription

<p>Creates a new subscription on an existing customer.</p>

**API Endpoint**: `POST /v1/customers/{customer}/subscriptions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.subscription.create(customer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.subscription.create(customer="string")
```

### modify <a name="modify"></a>
Update a subscription on a customer

<p>Updates an existing subscription on a customer to match the specified parameters. When changing plans or quantities, we will optionally prorate the price we charge next month to make up for any price changes. To preview how the proration will be calculated, use the <a href="#upcoming_invoice">upcoming invoice</a> endpoint.</p>

**API Endpoint**: `POST /v1/customers/{customer}/subscriptions/{subscription_exposed_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.customer.subscription.modify(
    customer="string", subscription_exposed_id="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.customer.subscription.modify(
    customer="string", subscription_exposed_id="string"
)
```
