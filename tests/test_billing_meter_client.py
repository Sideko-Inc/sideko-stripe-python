import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_reactivate_200_generated_success():
    """Tests a POST request to the /v1/billing/meters/{id}/reactivate endpoint.

    Operation: reactivate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.billing.meter.reactivate(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_reactivate_200_generated_success():
    """Tests a POST request to the /v1/billing/meters/{id}/reactivate endpoint.

    Operation: reactivate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.billing.meter.reactivate(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_deactivate_200_generated_success():
    """Tests a POST request to the /v1/billing/meters/{id}/deactivate endpoint.

    Operation: deactivate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.billing.meter.deactivate(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_deactivate_200_generated_success():
    """Tests a POST request to the /v1/billing/meters/{id}/deactivate endpoint.

    Operation: deactivate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.billing.meter.deactivate(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_generated_success():
    """Tests a POST request to the /v1/billing/meters/{id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.billing.meter.update(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/billing/meters/{id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.billing.meter.update(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_success_default():
    """Tests a POST request to the /v1/billing/meters endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.billing.meter.create(
        default_aggregation={"formula": "count"},
        display_name="string",
        event_name="string",
    )
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/billing/meters endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.billing.meter.create(
        default_aggregation={"formula": "count"},
        display_name="string",
        event_name="string",
    )
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/billing/meters/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.billing.meter.get(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/billing/meters/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BillingMeter

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.billing.meter.get(id="string")
    try:
        pydantic.TypeAdapter(models.BillingMeter).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/billing/meters endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BillingMeterListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.billing.meter.list()
    try:
        pydantic.TypeAdapter(models.BillingMeterListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/billing/meters endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BillingMeterListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.billing.meter.list()
    try:
        pydantic.TypeAdapter(models.BillingMeterListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
