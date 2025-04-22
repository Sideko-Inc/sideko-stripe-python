
### list <a name="list"></a>
List all credit notes

<p>Returns a list of credit notes.</p>

**API Endpoint**: `GET /v1/credit_notes`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.list()
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
res = await client.credit_note.list()
```

### preview <a name="preview"></a>
Preview a credit note

<p>Get a preview of a credit note without creating it.</p>

**API Endpoint**: `GET /v1/credit_notes/preview`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.preview(invoice="string")
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
res = await client.credit_note.preview(invoice="string")
```

### preview_lines <a name="preview_lines"></a>
Retrieve a credit note preview's line items

<p>When retrieving a credit note preview, you’ll get a <strong>lines</strong> property containing the first handful of those items. This URL you can retrieve the full (paginated) list of line items.</p>

**API Endpoint**: `GET /v1/credit_notes/preview/lines`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.preview_lines(invoice="string")
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
res = await client.credit_note.preview_lines(invoice="string")
```

### lines <a name="lines"></a>
Retrieve a credit note's line items

<p>When retrieving a credit note, you’ll get a <strong>lines</strong> property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

**API Endpoint**: `GET /v1/credit_notes/{credit_note}/lines`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.lines(credit_note="string")
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
res = await client.credit_note.lines(credit_note="string")
```

### get <a name="get"></a>
Retrieve a credit note

<p>Retrieves the credit note object with the given identifier.</p>

**API Endpoint**: `GET /v1/credit_notes/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.get(id="string")
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
res = await client.credit_note.get(id="string")
```

### create <a name="create"></a>
Create a credit note

<p>Issue a credit note to adjust the amount of a finalized invoice. For a <code>status=open</code> invoice, a credit note reduces
its <code>amount_due</code>. For a <code>status=paid</code> invoice, a credit note does not affect its <code>amount_due</code>. Instead, it can result
in any combination of the following:</p>

<ul>
<li>Refund: create a new refund (using <code>refund_amount</code>) or link an existing refund (using <code>refund</code>).</li>
<li>Customer balance credit: credit the customer’s balance (using <code>credit_amount</code>) which will be automatically applied to their next invoice when it’s finalized.</li>
<li>Outside of Stripe credit: record the amount that is or will be credited outside of Stripe (using <code>out_of_band_amount</code>).</li>
</ul>

<p>For post-payment credit notes the sum of the refund, credit and outside of Stripe amounts must equal the credit note total.</p>

<p>You may issue multiple credit notes for an invoice. Each credit note will increment the invoice’s <code>pre_payment_credit_notes_amount</code>
or <code>post_payment_credit_notes_amount</code> depending on its <code>status</code> at the time of credit note creation.</p>

**API Endpoint**: `POST /v1/credit_notes`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.create(invoice="string")
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
res = await client.credit_note.create(invoice="string")
```

### update <a name="update"></a>
Update a credit note

<p>Updates an existing credit note.</p>

**API Endpoint**: `POST /v1/credit_notes/{id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.update(id="string")
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
res = await client.credit_note.update(id="string")
```

### void <a name="void"></a>
Void a credit note

<p>Marks a credit note as void. Learn more about <a href="/docs/billing/invoices/credit-notes#voiding">voiding credit notes</a>.</p>

**API Endpoint**: `POST /v1/credit_notes/{id}/void`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.credit_note.void(id="string")
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
res = await client.credit_note.void(id="string")
```
