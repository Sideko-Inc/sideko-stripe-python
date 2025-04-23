import pydantic
import pytest
import typing

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_update_200_generated_success():
    """Tests a POST request to the /v1/customers/{customer} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Customer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.customer.update(customer="string")
    try:
        pydantic.TypeAdapter(models.Customer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/customers/{customer} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Customer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.customer.update(customer="string")
    try:
        pydantic.TypeAdapter(models.Customer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_generated_success():
    """Tests a POST request to the /v1/customers endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Customer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.customer.create()
    try:
        pydantic.TypeAdapter(models.Customer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_generated_success():
    """Tests a POST request to the /v1/customers endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Customer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.customer.create()
    try:
        pydantic.TypeAdapter(models.Customer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/customers/{customer} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.Customer, models.DeletedCustomer]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.customer.get(customer="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.Customer, models.DeletedCustomer]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/customers/{customer} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.Customer, models.DeletedCustomer]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.customer.get(customer="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.Customer, models.DeletedCustomer]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_search_200_generated_success():
    """Tests a GET request to the /v1/customers/search endpoint.

    Operation: search
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CustomerSearchResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.customer.search(query="string")
    try:
        pydantic.TypeAdapter(models.CustomerSearchResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_search_200_generated_success():
    """Tests a GET request to the /v1/customers/search endpoint.

    Operation: search
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CustomerSearchResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.customer.search(query="string")
    try:
        pydantic.TypeAdapter(models.CustomerSearchResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/customers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CustomerListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.customer.list()
    try:
        pydantic.TypeAdapter(models.CustomerListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/customers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CustomerListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.customer.list()
    try:
        pydantic.TypeAdapter(models.CustomerListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v1/customers/{customer} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DeletedCustomer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.customer.delete(customer="string")
    try:
        pydantic.TypeAdapter(models.DeletedCustomer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v1/customers/{customer} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DeletedCustomer

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.customer.delete(customer="string")
    try:
        pydantic.TypeAdapter(models.DeletedCustomer).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
