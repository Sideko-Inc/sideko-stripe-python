
### get <a name="get"></a>
Retrieve a Session

<p>Retrieves the details of a Financial Connections <code>Session</code></p>

**API Endpoint**: `GET /v1/link_account_sessions/{session}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.link_account_session.get(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.link_account_session.get(session="string")
```

### create <a name="create"></a>
Create a Session

<p>To launch the Financial Connections authorization flow, create a <code>Session</code>. The session’s <code>client_secret</code> can be used to launch the flow using Stripe.js.</p>

**API Endpoint**: `POST /v1/link_account_sessions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.link_account_session.create(
    account_holder={"type_": "account"}, permissions=["balances"]
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.link_account_session.create(
    account_holder={"type_": "account"}, permissions=["balances"]
)
```
