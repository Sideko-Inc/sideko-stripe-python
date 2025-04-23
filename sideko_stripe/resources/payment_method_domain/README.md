
### list <a name="list"></a>
List payment method domains

<p>Lists the details of existing payment method domains.</p>

**API Endpoint**: `GET /v1/payment_method_domains`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method_domain.list()
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method_domain.list()
```

### get <a name="get"></a>
Retrieve a payment method domain

<p>Retrieves the details of an existing payment method domain.</p>

**API Endpoint**: `GET /v1/payment_method_domains/{payment_method_domain}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method_domain.get(payment_method_domain="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method_domain.get(payment_method_domain="string")
```

### create <a name="create"></a>
Create a payment method domain

<p>Creates a payment method domain.</p>

**API Endpoint**: `POST /v1/payment_method_domains`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method_domain.create(domain_name="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method_domain.create(domain_name="string")
```

### update <a name="update"></a>
Update a payment method domain

<p>Updates an existing payment method domain.</p>

**API Endpoint**: `POST /v1/payment_method_domains/{payment_method_domain}`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method_domain.update(payment_method_domain="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method_domain.update(payment_method_domain="string")
```

### validate <a name="validate"></a>
Validate an existing payment method domain

<p>Some payment methods might require additional steps to register a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain.
The payment method doesn’t appear in Elements or Embedded Checkout for this domain until it is active.</p>

<p>To activate a payment method on an existing payment method domain, complete the required registration steps specific to the payment method, and then validate the payment method domain with this endpoint.</p>

<p>Related guides: <a href="/docs/payments/payment-methods/pmd-registration">Payment method domains</a>.</p>

**API Endpoint**: `POST /v1/payment_method_domains/{payment_method_domain}/validate`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(token=getenv("API_TOKEN"))
res = client.payment_method_domain.validate(payment_method_domain="string")
```

#### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(token=getenv("API_TOKEN"))
res = await client.payment_method_domain.validate(payment_method_domain="string")
```
