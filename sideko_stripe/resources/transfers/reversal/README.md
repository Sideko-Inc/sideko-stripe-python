
### list <a name="list"></a>
List all reversals

<p>You can see a list of the reversals belonging to a specific transfer. Note that the 10 most recent reversals are always available by default on the transfer object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional reversals.</p>

**API Endpoint**: `GET /v1/transfers/{id}/reversals`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfers.reversal.list(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfers.reversal.list(id="string")
```

### get <a name="get"></a>
Retrieve a reversal

<p>By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.</p>

**API Endpoint**: `GET /v1/transfers/{transfer}/reversals/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfers.reversal.get(id="string", transfer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfers.reversal.get(id="string", transfer="string")
```

### create <a name="create"></a>
Create a transfer reversal

<p>When you create a new reversal, you must specify a transfer to create it on.</p>

<p>When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.</p>

<p>Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.</p>

**API Endpoint**: `POST /v1/transfers/{id}/reversals`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfers.reversal.create(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfers.reversal.create(id="string")
```

### update <a name="update"></a>
Update a reversal

<p>Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<p>This request only accepts metadata and description as arguments.</p>

**API Endpoint**: `POST /v1/transfers/{transfer}/reversals/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfers.reversal.update(id="string", transfer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfers.reversal.update(id="string", transfer="string")
```
