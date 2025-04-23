
### list <a name="list"></a>
Retrieve settings

<p>Retrieves Tax <code>Settings</code> for a merchant.</p>

**API Endpoint**: `GET /v1/tax/settings`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.setting.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.setting.list()
```

### update <a name="update"></a>
Update settings

<p>Updates Tax <code>Settings</code> parameters used in tax calculations. All parameters are editable but none can be removed once set.</p>

**API Endpoint**: `POST /v1/tax/settings`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.tax.setting.update()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.tax.setting.update()
```
