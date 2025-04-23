import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_update_many_200_success_default():
    """Tests a POST request to the /v1/invoices/{invoice}/update_lines endpoint.

    Operation: update_many
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoice

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice.line.update_many(
        invoice="string", lines=[{"id": "string"}]
    )
    try:
        pydantic.TypeAdapter(models.Invoice).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_many_200_success_default():
    """Tests a POST request to the /v1/invoices/{invoice}/update_lines endpoint.

    Operation: update_many
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoice

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice.line.update_many(
        invoice="string", lines=[{"id": "string"}]
    )
    try:
        pydantic.TypeAdapter(models.Invoice).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_remove_many_200_success_default():
    """Tests a POST request to the /v1/invoices/{invoice}/remove_lines endpoint.

    Operation: remove_many
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoice

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice.line.remove_many(
        invoice="string", lines=[{"behavior": "delete", "id": "string"}]
    )
    try:
        pydantic.TypeAdapter(models.Invoice).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_remove_many_200_success_default():
    """Tests a POST request to the /v1/invoices/{invoice}/remove_lines endpoint.

    Operation: remove_many
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoice

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice.line.remove_many(
        invoice="string", lines=[{"behavior": "delete", "id": "string"}]
    )
    try:
        pydantic.TypeAdapter(models.Invoice).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_generated_success():
    """Tests a POST request to the /v1/invoices/{invoice}/lines/{line_item_id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.LineItem

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice.line.update(invoice="string", line_item_id="string")
    try:
        pydantic.TypeAdapter(models.LineItem).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/invoices/{invoice}/lines/{line_item_id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.LineItem

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice.line.update(invoice="string", line_item_id="string")
    try:
        pydantic.TypeAdapter(models.LineItem).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_many_200_success_default():
    """Tests a POST request to the /v1/invoices/{invoice}/add_lines endpoint.

    Operation: create_many
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoice

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice.line.create_many(invoice="string", lines=[{}])
    try:
        pydantic.TypeAdapter(models.Invoice).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_many_200_success_default():
    """Tests a POST request to the /v1/invoices/{invoice}/add_lines endpoint.

    Operation: create_many
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoice

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice.line.create_many(invoice="string", lines=[{}])
    try:
        pydantic.TypeAdapter(models.Invoice).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/invoices/{invoice}/lines endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.InvoiceLineListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice.line.list(invoice="string")
    try:
        pydantic.TypeAdapter(models.InvoiceLineListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/invoices/{invoice}/lines endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.InvoiceLineListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice.line.list(invoice="string")
    try:
        pydantic.TypeAdapter(models.InvoiceLineListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
