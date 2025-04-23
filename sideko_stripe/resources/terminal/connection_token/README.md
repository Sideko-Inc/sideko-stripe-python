
### create <a name="create"></a>
Create a Connection Token

<p>To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.</p>

**API Endpoint**: `POST /v1/terminal/connection_tokens`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.terminal.connection_token.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.terminal.connection_token.create()
```
