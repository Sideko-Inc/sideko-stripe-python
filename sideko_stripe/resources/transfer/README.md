
### list <a name="list"></a>
List all transfers

<p>Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.</p>

**API Endpoint**: `GET /v1/transfers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfer.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfer.list()
```

### get <a name="get"></a>
Retrieve a transfer

<p>Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.</p>

**API Endpoint**: `GET /v1/transfers/{transfer}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfer.get(transfer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfer.get(transfer="string")
```

### create <a name="create"></a>
Create a transfer

<p>To send funds from your Stripe account to a connected account, you create a new transfer object. Your <a href="#balance">Stripe balance</a> must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.</p>

**API Endpoint**: `POST /v1/transfers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfer.create(currency="string", destination="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfer.create(currency="string", destination="string")
```

### update <a name="update"></a>
Update a transfer

<p>Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

<p>This request accepts only metadata as an argument.</p>

**API Endpoint**: `POST /v1/transfers/{transfer}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.transfer.update(transfer="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.transfer.update(transfer="string")
```
