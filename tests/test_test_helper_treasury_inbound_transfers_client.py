import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_succeed_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/inbound_transfers/{id}/succeed endpoint.

    Operation: succeed
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TreasuryInboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.treasury.inbound_transfers.succeed(id="string")
    try:
        pydantic.TypeAdapter(models.TreasuryInboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_succeed_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/inbound_transfers/{id}/succeed endpoint.

    Operation: succeed
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TreasuryInboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.treasury.inbound_transfers.succeed(id="string")
    try:
        pydantic.TypeAdapter(models.TreasuryInboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_returned_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/inbound_transfers/{id}/return endpoint.

    Operation: returned
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TreasuryInboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.treasury.inbound_transfers.returned(id="string")
    try:
        pydantic.TypeAdapter(models.TreasuryInboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_returned_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/inbound_transfers/{id}/return endpoint.

    Operation: returned
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TreasuryInboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.treasury.inbound_transfers.returned(id="string")
    try:
        pydantic.TypeAdapter(models.TreasuryInboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_fail_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/inbound_transfers/{id}/fail endpoint.

    Operation: fail
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TreasuryInboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.treasury.inbound_transfers.fail(id="string")
    try:
        pydantic.TypeAdapter(models.TreasuryInboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_fail_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/inbound_transfers/{id}/fail endpoint.

    Operation: fail
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TreasuryInboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.treasury.inbound_transfers.fail(id="string")
    try:
        pydantic.TypeAdapter(models.TreasuryInboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
