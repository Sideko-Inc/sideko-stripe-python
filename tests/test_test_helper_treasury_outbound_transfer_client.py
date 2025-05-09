import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_returned_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return endpoint.

    Operation: returned
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.treasury.outbound_transfer.returned(
        outbound_transfer="string"
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_returned_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return endpoint.

    Operation: returned
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.treasury.outbound_transfer.returned(
        outbound_transfer="string"
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_post_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post endpoint.

    Operation: post
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.treasury.outbound_transfer.post(
        outbound_transfer="string"
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_post_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post endpoint.

    Operation: post
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.treasury.outbound_transfer.post(
        outbound_transfer="string"
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_fail_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail endpoint.

    Operation: fail
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.treasury.outbound_transfer.fail(
        outbound_transfer="string"
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_fail_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail endpoint.

    Operation: fail
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.treasury.outbound_transfer.fail(
        outbound_transfer="string"
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_success_default():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.treasury.outbound_transfer.update(
        outbound_transfer="string", tracking_details={"type_": "ach"}
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_default():
    """Tests a POST request to the /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TreasuryOutboundTransfer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.treasury.outbound_transfer.update(
        outbound_transfer="string", tracking_details={"type_": "ach"}
    )
    try:
        pydantic.TypeAdapter(models.TreasuryOutboundTransfer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
