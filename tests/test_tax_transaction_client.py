import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_create_reversal_200_success_default():
    """Tests a POST request to the /v1/tax/transactions/create_reversal endpoint.

    Operation: create_reversal
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.tax.transaction.create_reversal(
        mode="full", original_transaction="string", reference="string"
    )
    try:
        pydantic.TypeAdapter(models.TaxTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_reversal_200_success_default():
    """Tests a POST request to the /v1/tax/transactions/create_reversal endpoint.

    Operation: create_reversal
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.tax.transaction.create_reversal(
        mode="full", original_transaction="string", reference="string"
    )
    try:
        pydantic.TypeAdapter(models.TaxTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_from_calculation_200_success_default():
    """Tests a POST request to the /v1/tax/transactions/create_from_calculation endpoint.

    Operation: create_from_calculation
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.tax.transaction.create_from_calculation(
        calculation="string", reference="string"
    )
    try:
        pydantic.TypeAdapter(models.TaxTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_from_calculation_200_success_default():
    """Tests a POST request to the /v1/tax/transactions/create_from_calculation endpoint.

    Operation: create_from_calculation
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.tax.transaction.create_from_calculation(
        calculation="string", reference="string"
    )
    try:
        pydantic.TypeAdapter(models.TaxTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/tax/transactions/{transaction} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.tax.transaction.get(transaction="string")
    try:
        pydantic.TypeAdapter(models.TaxTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/tax/transactions/{transaction} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.tax.transaction.get(transaction="string")
    try:
        pydantic.TypeAdapter(models.TaxTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
