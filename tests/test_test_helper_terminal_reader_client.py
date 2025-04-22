import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_present_payment_method_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/terminal/readers/{reader}/present_payment_method endpoint.

    Operation: present_payment_method
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReader

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.test_helper.terminal.reader.present_payment_method(
        reader="string"
    )
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_present_payment_method_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/terminal/readers/{reader}/present_payment_method endpoint.

    Operation: present_payment_method
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReader

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.test_helper.terminal.reader.present_payment_method(
        reader="string"
    )
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
