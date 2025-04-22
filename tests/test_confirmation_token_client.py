import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_get_200_generated_success():
    """Tests a GET request to the /v1/confirmation_tokens/{confirmation_token} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ConfirmationToken

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
    response = client.confirmation_token.get(confirmation_token="string")
    try:
        pydantic.TypeAdapter(models.ConfirmationToken).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/confirmation_tokens/{confirmation_token} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ConfirmationToken

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
    response = await client.confirmation_token.get(confirmation_token="string")
    try:
        pydantic.TypeAdapter(models.ConfirmationToken).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
