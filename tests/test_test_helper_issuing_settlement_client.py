import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_complete_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/settlements/{settlement}/complete endpoint.

    Operation: complete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingSettlement

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.settlement.complete(settlement="string")
    try:
        pydantic.TypeAdapter(models.IssuingSettlement).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_complete_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/settlements/{settlement}/complete endpoint.

    Operation: complete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingSettlement

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.settlement.complete(settlement="string")
    try:
        pydantic.TypeAdapter(models.IssuingSettlement).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/settlements endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingSettlement

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.settlement.create(
        bin="string", clearing_date=123, currency="string", net_total_amount=123
    )
    try:
        pydantic.TypeAdapter(models.IssuingSettlement).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/settlements endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingSettlement

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.settlement.create(
        bin="string", clearing_date=123, currency="string", net_total_amount=123
    )
    try:
        pydantic.TypeAdapter(models.IssuingSettlement).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
