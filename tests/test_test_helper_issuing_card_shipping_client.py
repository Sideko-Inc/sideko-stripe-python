import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_submit_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/submit endpoint.

    Operation: submit
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.card.shipping.submit(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_submit_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/submit endpoint.

    Operation: submit
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.card.shipping.submit(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_ship_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/ship endpoint.

    Operation: ship
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.card.shipping.ship(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_ship_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/ship endpoint.

    Operation: ship
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.card.shipping.ship(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_returned_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/return endpoint.

    Operation: returned
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.card.shipping.returned(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_returned_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/return endpoint.

    Operation: returned
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.card.shipping.returned(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_fail_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/fail endpoint.

    Operation: fail
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.card.shipping.fail(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_fail_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/fail endpoint.

    Operation: fail
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.card.shipping.fail(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_deliver_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/deliver endpoint.

    Operation: deliver
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.test_helper.issuing.card.shipping.deliver(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_deliver_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/cards/{card}/shipping/deliver endpoint.

    Operation: deliver
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingCard

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.test_helper.issuing.card.shipping.deliver(card="string")
    try:
        pydantic.TypeAdapter(models.IssuingCard).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
