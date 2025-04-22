
### activate <a name="activate"></a>
Activate a testmode personalization design

<p>Updates the <code>status</code> of the specified testmode personalization design object to <code>active</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.personalization_design.activate(
    personalization_design="string"
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
res = await client.test_helper.issuing.personalization_design.activate(
    personalization_design="string"
)
```

### deactivate <a name="deactivate"></a>
Deactivate a testmode personalization design

<p>Updates the <code>status</code> of the specified testmode personalization design object to <code>inactive</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.personalization_design.deactivate(
    personalization_design="string"
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
res = await client.test_helper.issuing.personalization_design.deactivate(
    personalization_design="string"
)
```

### reject <a name="reject"></a>
Reject a testmode personalization design

<p>Updates the <code>status</code> of the specified testmode personalization design object to <code>rejected</code>.</p>

**API Endpoint**: `POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.test_helper.issuing.personalization_design.reject(
    personalization_design="string", rejection_reasons={}
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
res = await client.test_helper.issuing.personalization_design.reject(
    personalization_design="string", rejection_reasons={}
)
```
