
### respond <a name="respond"></a>
Respond to fraud challenge

<p>Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.test_helper.issuing.authorization.fraud_challenges.respond(
    authorization="string", confirmed=True
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.test_helper.issuing.authorization.fraud_challenges.respond(
    authorization="string", confirmed=True
)
```
