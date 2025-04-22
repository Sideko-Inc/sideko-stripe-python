
### list <a name="list"></a>
List all SetupAttempts

<p>Returns a list of SetupAttempts that associate with a provided SetupIntent.</p>

**API Endpoint**: `GET /v1/setup_attempts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.setup_attempt.list(setup_intent="string")
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
res = await client.setup_attempt.list(setup_intent="string")
```
