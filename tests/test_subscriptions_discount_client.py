import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v1/subscriptions/{subscription_exposed_id}/discount endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DeletedDiscount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.subscriptions.discount.delete(subscription_exposed_id="string")
    try:
        pydantic.TypeAdapter(models.DeletedDiscount).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v1/subscriptions/{subscription_exposed_id}/discount endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DeletedDiscount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.subscriptions.discount.delete(
        subscription_exposed_id="string"
    )
    try:
        pydantic.TypeAdapter(models.DeletedDiscount).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
