
### delete <a name="delete"></a>
Delete a Reader

<p>Deletes a <code>Reader</code> object.</p>

**API Endpoint**: `DELETE /v1/terminal/readers/{reader}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.delete(reader="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.delete(reader="string")
```

### list <a name="list"></a>
List all Readers

<p>Returns a list of <code>Reader</code> objects.</p>

**API Endpoint**: `GET /v1/terminal/readers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.list()
```

### get <a name="get"></a>
Retrieve a Reader

<p>Retrieves a <code>Reader</code> object.</p>

**API Endpoint**: `GET /v1/terminal/readers/{reader}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.get(reader="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.get(reader="string")
```

### create <a name="create"></a>
Create a Reader

<p>Creates a new <code>Reader</code> object.</p>

**API Endpoint**: `POST /v1/terminal/readers`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.create(registration_code="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.create(registration_code="string")
```

### update <a name="update"></a>
Update a Reader

<p>Updates a <code>Reader</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

**API Endpoint**: `POST /v1/terminal/readers/{reader}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.update(reader="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.update(reader="string")
```

### cancel_action <a name="cancel_action"></a>
Cancel the current reader action

<p>Cancels the current reader action.</p>

**API Endpoint**: `POST /v1/terminal/readers/{reader}/cancel_action`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.cancel_action(reader="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.cancel_action(reader="string")
```

### process_payment_intent <a name="process_payment_intent"></a>
Hand-off a PaymentIntent to a Reader

<p>Initiates a payment flow on a Reader.</p>

**API Endpoint**: `POST /v1/terminal/readers/{reader}/process_payment_intent`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.process_payment_intent(
    payment_intent="string", reader="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.process_payment_intent(
    payment_intent="string", reader="string"
)
```

### process_setup_intent <a name="process_setup_intent"></a>
Hand-off a SetupIntent to a Reader

<p>Initiates a setup intent flow on a Reader.</p>

**API Endpoint**: `POST /v1/terminal/readers/{reader}/process_setup_intent`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.process_setup_intent(
    allow_redisplay="always", reader="string", setup_intent="string"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.process_setup_intent(
    allow_redisplay="always", reader="string", setup_intent="string"
)
```

### refund_payment <a name="refund_payment"></a>
Refund a Charge or a PaymentIntent in-person

<p>Initiates a refund on a Reader</p>

**API Endpoint**: `POST /v1/terminal/readers/{reader}/refund_payment`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.refund_payment(reader="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.refund_payment(reader="string")
```

### set_reader_display <a name="set_reader_display"></a>
Set reader display

<p>Sets reader display to show cart details.</p>

**API Endpoint**: `POST /v1/terminal/readers/{reader}/set_reader_display`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.terminal.reader.set_reader_display(reader="string", type_="cart")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = await client.terminal.reader.set_reader_display(reader="string", type_="cart")
```
