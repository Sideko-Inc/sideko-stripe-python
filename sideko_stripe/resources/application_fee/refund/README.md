
### get <a name="get"></a>
Retrieve an application fee refund

<p>By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.</p>

**API Endpoint**: `GET /v1/application_fees/{fee}/refunds/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.application_fee.refund.get(fee="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.application_fee.refund.get(fee="string", id="string")
```

### list <a name="list"></a>
List all application fee refunds

<p>You can see a list of the refunds belonging to a specific application fee. Note that the 10 most recent refunds are always available by default on the application fee object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional refunds.</p>

**API Endpoint**: `GET /v1/application_fees/{id}/refunds`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.application_fee.refund.list(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.application_fee.refund.list(id="string")
```

### update <a name="update"></a>
Update an application fee refund

<p>Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<p>This request only accepts metadata as an argument.</p>

**API Endpoint**: `POST /v1/application_fees/{fee}/refunds/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.application_fee.refund.update(fee="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.application_fee.refund.update(fee="string", id="string")
```

### create <a name="create"></a>
POST /v1/application_fees/{id}/refund



**API Endpoint**: `POST /v1/application_fees/{id}/refund`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.application_fee.refund.create(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.application_fee.refund.create(id="string")
```

### create_many <a name="create_many"></a>
Create an application fee refund

<p>Refunds an application fee that has previously been collected but not yet refunded.
Funds will be refunded to the Stripe account from which the fee was originally collected.</p>

<p>You can optionally refund only part of an application fee.
You can do so multiple times, until the entire fee has been refunded.</p>

<p>Once entirely refunded, an application fee can’t be refunded again.
This method will raise an error when called on an already-refunded application fee,
or when trying to refund more money than is left on an application fee.</p>

**API Endpoint**: `POST /v1/application_fees/{id}/refunds`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.application_fee.refund.create_many(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.application_fee.refund.create_many(id="string")
```
