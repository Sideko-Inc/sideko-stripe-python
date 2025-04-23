import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_unarchive_200_generated_success():
    """Tests a POST request to the /v1/invoice_rendering_templates/{template}/unarchive endpoint.

    Operation: unarchive
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.InvoiceRenderingTemplate

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice_rendering_template.unarchive(template="string")
    try:
        pydantic.TypeAdapter(models.InvoiceRenderingTemplate).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_unarchive_200_generated_success():
    """Tests a POST request to the /v1/invoice_rendering_templates/{template}/unarchive endpoint.

    Operation: unarchive
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.InvoiceRenderingTemplate

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice_rendering_template.unarchive(template="string")
    try:
        pydantic.TypeAdapter(models.InvoiceRenderingTemplate).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_archive_200_generated_success():
    """Tests a POST request to the /v1/invoice_rendering_templates/{template}/archive endpoint.

    Operation: archive
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.InvoiceRenderingTemplate

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice_rendering_template.archive(template="string")
    try:
        pydantic.TypeAdapter(models.InvoiceRenderingTemplate).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_archive_200_generated_success():
    """Tests a POST request to the /v1/invoice_rendering_templates/{template}/archive endpoint.

    Operation: archive
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.InvoiceRenderingTemplate

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice_rendering_template.archive(template="string")
    try:
        pydantic.TypeAdapter(models.InvoiceRenderingTemplate).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/invoice_rendering_templates/{template} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.InvoiceRenderingTemplate

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice_rendering_template.get(template="string")
    try:
        pydantic.TypeAdapter(models.InvoiceRenderingTemplate).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/invoice_rendering_templates/{template} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.InvoiceRenderingTemplate

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice_rendering_template.get(template="string")
    try:
        pydantic.TypeAdapter(models.InvoiceRenderingTemplate).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/invoice_rendering_templates endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.InvoiceRenderingTemplateListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.invoice_rendering_template.list()
    try:
        pydantic.TypeAdapter(
            models.InvoiceRenderingTemplateListResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/invoice_rendering_templates endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.InvoiceRenderingTemplateListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.invoice_rendering_template.list()
    try:
        pydantic.TypeAdapter(
            models.InvoiceRenderingTemplateListResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
