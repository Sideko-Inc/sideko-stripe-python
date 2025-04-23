import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_list_200_generated_success():
    """Tests a GET request to the /v1/setup_attempts endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SetupAttemptListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.setup_attempt.list(setup_intent="string")
    try:
        pydantic.TypeAdapter(models.SetupAttemptListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/setup_attempts endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SetupAttemptListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.setup_attempt.list(setup_intent="string")
    try:
        pydantic.TypeAdapter(models.SetupAttemptListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
