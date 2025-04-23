
### list <a name="list"></a>
List VerificationReports

<p>List all verification reports.</p>

**API Endpoint**: `GET /v1/identity/verification_reports`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_report.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_report.list()
```

### get <a name="get"></a>
Retrieve a VerificationReport

<p>Retrieves an existing VerificationReport</p>

**API Endpoint**: `GET /v1/identity/verification_reports/{report}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_report.get(report="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_report.get(report="string")
```
