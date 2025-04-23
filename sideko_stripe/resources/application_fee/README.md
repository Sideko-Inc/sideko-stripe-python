
### list <a name="list"></a>
List all application fees

<p>Returns a list of application fees you’ve previously collected. The application fees are returned in sorted order, with the most recent fees appearing first.</p>

**API Endpoint**: `GET /v1/application_fees`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.application_fee.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.application_fee.list()
```

### get <a name="get"></a>
Retrieve an application fee

<p>Retrieves the details of an application fee that your account has collected. The same information is returned when refunding the application fee.</p>

**API Endpoint**: `GET /v1/application_fees/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.application_fee.get(id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.application_fee.get(id="string")
```
