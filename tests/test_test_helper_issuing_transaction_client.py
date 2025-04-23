import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_refund_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/transactions/{transaction}/refund endpoint.

    Operation: refund
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.transaction.refund(transaction="string")
    try:
        pydantic.TypeAdapter(models.IssuingTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_refund_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/transactions/{transaction}/refund endpoint.

    Operation: refund
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.transaction.refund(transaction="string")
    try:
        pydantic.TypeAdapter(models.IssuingTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_unlinked_refund_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/transactions/create_unlinked_refund endpoint.

    Operation: create_unlinked_refund
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.transaction.create_unlinked_refund(
        amount=123, card="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_unlinked_refund_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/transactions/create_unlinked_refund endpoint.

    Operation: create_unlinked_refund
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.transaction.create_unlinked_refund(
        amount=123, card="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_force_capture_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/transactions/create_force_capture endpoint.

    Operation: create_force_capture
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.transaction.create_force_capture(
        amount=123, card="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_force_capture_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/transactions/create_force_capture endpoint.

    Operation: create_force_capture
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingTransaction

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.transaction.create_force_capture(
        amount=123, card="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingTransaction).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
