
### list <a name="list"></a>
List all charges

<p>Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.</p>

**API Endpoint**: `GET /v1/charges`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.charge.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.charge.list()
```

### search <a name="search"></a>
Search charges

<p>Search for charges you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
to an hour behind during outages. Search functionality is not available to merchants in India.</p>

**API Endpoint**: `GET /v1/charges/search`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.charge.search(query="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.charge.search(query="string")
```

### get <a name="get"></a>
Retrieve a charge

<p>Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.</p>

**API Endpoint**: `GET /v1/charges/{charge}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.charge.get(charge="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.charge.get(charge="string")
```

### create <a name="create"></a>
POST /v1/charges

<p>This method is no longer recommended—use the <a href="/docs/api/payment_intents">Payment Intents API</a>
to initiate a new payment instead. Confirmation of the PaymentIntent creates the <code>Charge</code>
object used to request payment.</p>

**API Endpoint**: `POST /v1/charges`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.charge.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.charge.create()
```

### update <a name="update"></a>
Update a charge

<p>Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

**API Endpoint**: `POST /v1/charges/{charge}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.charge.update(charge="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.charge.update(charge="string")
```

### capture <a name="capture"></a>
Capture a payment

<p>Capture the payment of an existing, uncaptured charge that was created with the <code>capture</code> option set to false.</p>

<p>Uncaptured payments expire a set number of days after they are created (<a href="/docs/charges/placing-a-hold">7 by default</a>), after which they are marked as refunded and capture attempts will fail.</p>

<p>Don’t use this method to capture a PaymentIntent-initiated charge. Use <a href="/docs/api/payment_intents/capture">Capture a PaymentIntent</a>.</p>

**API Endpoint**: `POST /v1/charges/{charge}/capture`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.charge.capture(charge="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.charge.capture(charge="string")
```
