
### list <a name="list"></a>
List VerificationSessions

<p>Returns a list of VerificationSessions</p>

**API Endpoint**: `GET /v1/identity/verification_sessions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_session.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_session.list()
```

### get <a name="get"></a>
Retrieve a VerificationSession

<p>Retrieves the details of a VerificationSession that was previously created.</p>

<p>When the session status is <code>requires_input</code>, you can use this method to retrieve a valid
<code>client_secret</code> or <code>url</code> to allow re-submission.</p>

**API Endpoint**: `GET /v1/identity/verification_sessions/{session}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_session.get(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_session.get(session="string")
```

### create <a name="create"></a>
Create a VerificationSession

<p>Creates a VerificationSession object.</p>

<p>After the VerificationSession is created, display a verification modal using the session <code>client_secret</code> or send your users to the session’s <code>url</code>.</p>

<p>If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.</p>

<p>Related guide: <a href="/docs/identity/verify-identity-documents">Verify your users’ identity documents</a></p>

**API Endpoint**: `POST /v1/identity/verification_sessions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_session.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_session.create()
```

### update <a name="update"></a>
Update a VerificationSession

<p>Updates a VerificationSession object.</p>

<p>When the session status is <code>requires_input</code>, you can use this method to update the
verification check and options.</p>

**API Endpoint**: `POST /v1/identity/verification_sessions/{session}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_session.update(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_session.update(session="string")
```

### cancel <a name="cancel"></a>
Cancel a VerificationSession

<p>A VerificationSession object can be canceled when it is in <code>requires_input</code> <a href="/docs/identity/how-sessions-work">status</a>.</p>

<p>Once canceled, future submission attempts are disabled. This cannot be undone. <a href="/docs/identity/verification-sessions#cancel">Learn more</a>.</p>

**API Endpoint**: `POST /v1/identity/verification_sessions/{session}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_session.cancel(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_session.cancel(session="string")
```

### redact <a name="redact"></a>
Redact a VerificationSession

<p>Redact a VerificationSession to remove all collected information from Stripe. This will redact
the VerificationSession and all objects related to it, including VerificationReports, Events,
request logs, etc.</p>

<p>A VerificationSession object can be redacted when it is in <code>requires_input</code> or <code>verified</code>
<a href="/docs/identity/how-sessions-work">status</a>. Redacting a VerificationSession in <code>requires_action</code>
state will automatically cancel it.</p>

<p>The redaction process may take up to four days. When the redaction process is in progress, the
VerificationSession’s <code>redaction.status</code> field will be set to <code>processing</code>; when the process is
finished, it will change to <code>redacted</code> and an <code>identity.verification_session.redacted</code> event
will be emitted.</p>

<p>Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
fields that contain personal data will be replaced by the string <code>[redacted]</code> or a similar
placeholder. The <code>metadata</code> field will also be erased. Redacted objects cannot be updated or
used for any purpose.</p>

<p><a href="/docs/identity/verification-sessions#redact">Learn more</a>.</p>

**API Endpoint**: `POST /v1/identity/verification_sessions/{session}/redact`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.identity.verification_session.redact(session="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.identity.verification_session.redact(session="string")
```
