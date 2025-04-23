
### list <a name="list"></a>
List all quotes

<p>Returns a list of your quotes.</p>

**API Endpoint**: `GET /v1/quotes`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.list()
```

### get <a name="get"></a>
Retrieve a quote

<p>Retrieves the quote with the given ID.</p>

**API Endpoint**: `GET /v1/quotes/{quote}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.get(quote="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.get(quote="string")
```

### computed_upfront_line_items <a name="computed_upfront_line_items"></a>
Retrieve a quote's upfront line items

<p>When retrieving a quote, there is an includable <a href="https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items"><strong>computed.upfront.line_items</strong></a> property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.</p>

**API Endpoint**: `GET /v1/quotes/{quote}/computed_upfront_line_items`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.computed_upfront_line_items(quote="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.computed_upfront_line_items(quote="string")
```

### pdf <a name="pdf"></a>
Download quote PDF

<p>Download the PDF for a finalized quote. Explanation for special handling can be found <a href="https://docs.stripe.com/quotes/overview#quote_pdf">here</a></p>

**API Endpoint**: `GET /v1/quotes/{quote}/pdf`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.pdf(quote="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.pdf(quote="string")
```

### create <a name="create"></a>
Create a quote

<p>A quote models prices and services for a customer. Default options for <code>header</code>, <code>description</code>, <code>footer</code>, and <code>expires_at</code> can be set in the dashboard via the <a href="https://dashboard.stripe.com/settings/billing/quote">quote template</a>.</p>

**API Endpoint**: `POST /v1/quotes`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.create()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.create()
```

### update <a name="update"></a>
Update a quote

<p>A quote models prices and services for a customer.</p>

**API Endpoint**: `POST /v1/quotes/{quote}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.update(quote="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.update(quote="string")
```

### accept <a name="accept"></a>
Accept a quote

<p>Accepts the specified quote.</p>

**API Endpoint**: `POST /v1/quotes/{quote}/accept`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.accept(quote="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.accept(quote="string")
```

### cancel <a name="cancel"></a>
Cancel a quote

<p>Cancels the quote.</p>

**API Endpoint**: `POST /v1/quotes/{quote}/cancel`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.cancel(quote="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.cancel(quote="string")
```

### finalize <a name="finalize"></a>
Finalize a quote

<p>Finalizes the quote.</p>

**API Endpoint**: `POST /v1/quotes/{quote}/finalize`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.quote.finalize(quote="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.quote.finalize(quote="string")
```
