
### list <a name="list"></a>
List orders

<p>Lists all Climate order objects. The orders are returned sorted by creation date, with the
most recently created orders appearing first.</p>

**API Endpoint**: `GET /v1/climate/orders`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.order.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.order.list()
```

### get <a name="get"></a>
Retrieve an order

<p>Retrieves the details of a Climate order object with the given ID.</p>

**API Endpoint**: `GET /v1/climate/orders/{order}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.order.get(order="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.order.get(order="string")
```

### create <a name="create"></a>
Create an order

<p>Creates a Climate order object for a given Climate product. The order will be processed immediately
after creation and payment will be deducted your Stripe balance.</p>

**API Endpoint**: `POST /v1/climate/orders`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.order.create(product="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.order.create(product="string")
```

### update <a name="update"></a>
Update an order

<p>Updates the specified order by setting the values of the parameters passed.</p>

**API Endpoint**: `POST /v1/climate/orders/{order}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.order.update(order="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.order.update(order="string")
```

### cancel <a name="cancel"></a>
Cancel an order

<p>Cancels a Climate order. You can cancel an order within 24 hours of creation. Stripe refunds the
reservation <code>amount_subtotal</code>, but not the <code>amount_fees</code> for user-triggered cancellations. Frontier
might cancel reservations if suppliers fail to deliver. If Frontier cancels the reservation, Stripe
provides 90 days advance notice and refunds the <code>amount_total</code>.</p>

**API Endpoint**: `POST /v1/climate/orders/{order}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.climate.order.cancel(order="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.climate.order.cancel(order="string")
```
