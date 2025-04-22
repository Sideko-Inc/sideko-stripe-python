
### create <a name="create"></a>
Create or retrieve funding instructions for a customer cash balance

<p>Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
funding instructions will be created. If funding instructions have already been created for a given customer, the same
funding instructions will be retrieved. In other words, we will return the same funding instructions each time.</p>

**API Endpoint**: `POST /v1/customers/{customer}/funding_instructions`

#### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    username=getenv("API_USERNAME"),
    password=getenv("API_PASSWORD"),
    token=getenv("API_TOKEN"),
)
res = client.customer.funding_instruction.create(
    bank_transfer={"type_": "eu_bank_transfer"},
    currency="string",
    customer="string",
    funding_type="bank_transfer",
)
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
res = await client.customer.funding_instruction.create(
    bank_transfer={"type_": "eu_bank_transfer"},
    currency="string",
    customer="string",
    funding_type="bank_transfer",
)
```
