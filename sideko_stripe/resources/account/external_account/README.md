
### delete <a name="delete"></a>
Delete an external account

<p>Delete a specified external account for a given account.</p>

**API Endpoint**: `DELETE /v1/accounts/{account}/external_accounts/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.external_account.delete(account="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.external_account.delete(account="string", id="string")
```

### list <a name="list"></a>
List all external accounts

<p>List external accounts for an account.</p>

**API Endpoint**: `GET /v1/accounts/{account}/external_accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.external_account.list(account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.external_account.list(account="string")
```

### get <a name="get"></a>
Retrieve an external account

<p>Retrieve a specified external account for a given account.</p>

**API Endpoint**: `GET /v1/accounts/{account}/external_accounts/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.external_account.get(account="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.external_account.get(account="string", id="string")
```

### create <a name="create"></a>
Create an external account

<p>Create an external account for a given account.</p>

**API Endpoint**: `POST /v1/accounts/{account}/external_accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.external_account.create(account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.external_account.create(account="string")
```

### update <a name="update"></a>
POST /v1/accounts/{account}/external_accounts/{id}

<p>Updates the metadata, account holder name, account holder type of a bank account belonging to
a connected account and optionally sets it as the default for its currency. Other bank account
details are not editable by design.</p>

<p>You can only update bank accounts when <a href="/api/accounts/object#account_object-controller-requirement_collection">account.controller.requirement_collection</a> is <code>application</code>, which includes <a href="/connect/custom-accounts">Custom accounts</a>.</p>

<p>You can re-enable a disabled bank account by performing an update call without providing any
arguments or changes.</p>

**API Endpoint**: `POST /v1/accounts/{account}/external_accounts/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.external_account.update(account="string", id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.external_account.update(account="string", id="string")
```
