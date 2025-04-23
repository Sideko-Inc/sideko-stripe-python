
### list <a name="list"></a>
Retrieve an invoice's line items

<p>When retrieving an invoice, you’ll get a <strong>lines</strong> property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

**API Endpoint**: `GET /v1/invoices/{invoice}/lines`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.invoice.line.list(invoice="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.invoice.line.list(invoice="string")
```

### create_many <a name="create_many"></a>
Bulk add invoice line items

<p>Adds multiple line items to an invoice. This is only possible when an invoice is still a draft.</p>

**API Endpoint**: `POST /v1/invoices/{invoice}/add_lines`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.invoice.line.create_many(invoice="string", lines=[{}])
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.invoice.line.create_many(invoice="string", lines=[{}])
```

### update <a name="update"></a>
Update an invoice's line item

<p>Updates an invoice’s line item. Some fields, such as <code>tax_amounts</code>, only live on the invoice line item,
so they can only be updated through this endpoint. Other fields, such as <code>amount</code>, live on both the invoice
item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well.
Updating an invoice’s line item is only possible before the invoice is finalized.</p>

**API Endpoint**: `POST /v1/invoices/{invoice}/lines/{line_item_id}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.invoice.line.update(invoice="string", line_item_id="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.invoice.line.update(invoice="string", line_item_id="string")
```

### remove_many <a name="remove_many"></a>
Bulk remove invoice line items

<p>Removes multiple line items from an invoice. This is only possible when an invoice is still a draft.</p>

**API Endpoint**: `POST /v1/invoices/{invoice}/remove_lines`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.invoice.line.remove_many(
    invoice="string", lines=[{"behavior": "delete", "id": "string"}]
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.invoice.line.remove_many(
    invoice="string", lines=[{"behavior": "delete", "id": "string"}]
)
```

### update_many <a name="update_many"></a>
Bulk update invoice line items

<p>Updates multiple line items on an invoice. This is only possible when an invoice is still a draft.</p>

**API Endpoint**: `POST /v1/invoices/{invoice}/update_lines`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.invoice.line.update_many(invoice="string", lines=[{"id": "string"}])
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.invoice.line.update_many(invoice="string", lines=[{"id": "string"}])
```
