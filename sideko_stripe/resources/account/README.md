
### delete <a name="delete"></a>
Delete an account

<p>With <a href="/connect">Connect</a>, you can delete accounts you manage.</p>

<p>Test-mode accounts can be deleted at any time.</p>

<p>Live-mode accounts where Stripe is responsible for negative account balances cannot be deleted, which includes Standard accounts. Live-mode accounts where your platform is liable for negative account balances, which includes Custom and Express accounts, can be deleted when all <a href="/api/balance/balance_object">balances</a> are zero.</p>

<p>If you want to delete your own account, use the <a href="https://dashboard.stripe.com/settings/account">account information tab in your account settings</a> instead.</p>

**API Endpoint**: `DELETE /v1/accounts/{account}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.delete(account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.delete(account="string")
```

### details <a name="details"></a>
Retrieve account

<p>Retrieves the details of an account.</p>

**API Endpoint**: `GET /v1/account`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.details()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.details()
```

### list <a name="list"></a>
List all connected accounts

<p>Returns a list of accounts connected to your platform via <a href="/docs/connect">Connect</a>. If you’re not a platform, the list is empty.</p>

**API Endpoint**: `GET /v1/accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.list()
```

### get <a name="get"></a>
Retrieve account

<p>Retrieves the details of an account.</p>

**API Endpoint**: `GET /v1/accounts/{account}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.get(account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.get(account="string")
```

### create <a name="create"></a>
POST /v1/accounts

<p>With <a href="/docs/connect">Connect</a>, you can create Stripe accounts for your users.
To do this, you’ll first need to <a href="https://dashboard.stripe.com/account/applications/settings">register your platform</a>.</p>

<p>If you’ve already collected information for your connected accounts, you <a href="/docs/connect/best-practices#onboarding">can prefill that information</a> when
creating the account. Connect Onboarding won’t ask for the prefilled information during account onboarding.
You can prefill any information on the account.</p>

**API Endpoint**: `POST /v1/accounts`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.create()
```

### update <a name="update"></a>
Update an account

<p>Updates a <a href="/connect/accounts">connected account</a> by setting the values of the parameters passed. Any parameters not provided are
left unchanged.</p>

<p>For accounts where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a>
is <code>application</code>, which includes Custom accounts, you can update any information on the account.</p>

<p>For accounts where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a>
is <code>stripe</code>, which includes Standard and Express accounts, you can update all information until you create
an <a href="/api/account_links">Account Link</a> or <a href="/api/account_sessions">Account Session</a> to start Connect onboarding,
after which some properties can no longer be updated.</p>

<p>To update your own account, use the <a href="https://dashboard.stripe.com/settings/account">Dashboard</a>. Refer to our
<a href="/docs/connect/updating-accounts">Connect</a> documentation to learn more about updating accounts.</p>

**API Endpoint**: `POST /v1/accounts/{account}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.update(account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.update(account="string")
```

### create_login_link <a name="create_login_link"></a>
Create a login link

<p>Creates a login link for a connected account to access the Express Dashboard.</p>

<p><strong>You can only create login links for accounts that use the <a href="/connect/express-dashboard">Express Dashboard</a> and are connected to your platform</strong>.</p>

**API Endpoint**: `POST /v1/accounts/{account}/login_links`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.create_login_link(account="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.create_login_link(account="string")
```

### reject <a name="reject"></a>
Reject an account

<p>With <a href="/connect">Connect</a>, you can reject accounts that you have flagged as suspicious.</p>

<p>Only accounts where your platform is liable for negative account balances, which includes Custom and Express accounts, can be rejected. Test-mode accounts can be rejected at any time. Live-mode accounts can only be rejected after all balances are zero.</p>

**API Endpoint**: `POST /v1/accounts/{account}/reject`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.account.reject(account="string", reason="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.account.reject(account="string", reason="string")
```
