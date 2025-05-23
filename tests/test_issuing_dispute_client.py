import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_submit_200_generated_success():
    """Tests a POST request to the /v1/issuing/disputes/{dispute}/submit endpoint.

    Operation: submit
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.issuing.dispute.submit(dispute="string")
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_submit_200_generated_success():
    """Tests a POST request to the /v1/issuing/disputes/{dispute}/submit endpoint.

    Operation: submit
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.issuing.dispute.submit(dispute="string")
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_generated_success():
    """Tests a POST request to the /v1/issuing/disputes/{dispute} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.issuing.dispute.update(dispute="string")
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/issuing/disputes/{dispute} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.issuing.dispute.update(dispute="string")
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_generated_success():
    """Tests a POST request to the /v1/issuing/disputes endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.issuing.dispute.create()
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_generated_success():
    """Tests a POST request to the /v1/issuing/disputes endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.issuing.dispute.create()
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/issuing/disputes/{dispute} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.issuing.dispute.get(dispute="string")
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/issuing/disputes/{dispute} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingDispute

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.issuing.dispute.get(dispute="string")
    try:
        pydantic.TypeAdapter(models.IssuingDispute).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/issuing/disputes endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingDisputeListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.issuing.dispute.list()
    try:
        pydantic.TypeAdapter(models.IssuingDisputeListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/issuing/disputes endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingDisputeListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.issuing.dispute.list()
    try:
        pydantic.TypeAdapter(models.IssuingDisputeListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
