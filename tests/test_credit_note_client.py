import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_void_200_generated_success():
    """Tests a POST request to the /v1/credit_notes/{id}/void endpoint.

    Operation: void
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.void(id="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_void_200_generated_success():
    """Tests a POST request to the /v1/credit_notes/{id}/void endpoint.

    Operation: void
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.void(id="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_generated_success():
    """Tests a POST request to the /v1/credit_notes/{id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.update(id="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/credit_notes/{id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.update(id="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_success_default():
    """Tests a POST request to the /v1/credit_notes endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.create(invoice="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/credit_notes endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.create(invoice="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.get(id="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.get(id="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_lines_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/{credit_note}/lines endpoint.

    Operation: lines
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNoteLinesResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.lines(credit_note="string")
    try:
        pydantic.TypeAdapter(models.CreditNoteLinesResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_lines_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/{credit_note}/lines endpoint.

    Operation: lines
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNoteLinesResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.lines(credit_note="string")
    try:
        pydantic.TypeAdapter(models.CreditNoteLinesResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_preview_lines_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/preview/lines endpoint.

    Operation: preview_lines
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNotePreviewLinesResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.preview_lines(invoice="string")
    try:
        pydantic.TypeAdapter(models.CreditNotePreviewLinesResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_preview_lines_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/preview/lines endpoint.

    Operation: preview_lines
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNotePreviewLinesResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.preview_lines(invoice="string")
    try:
        pydantic.TypeAdapter(models.CreditNotePreviewLinesResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_preview_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/preview endpoint.

    Operation: preview
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.preview(invoice="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_preview_200_generated_success():
    """Tests a GET request to the /v1/credit_notes/preview endpoint.

    Operation: preview
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNote

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.preview(invoice="string")
    try:
        pydantic.TypeAdapter(models.CreditNote).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/credit_notes endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CreditNoteListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = client.credit_note.list()
    try:
        pydantic.TypeAdapter(models.CreditNoteListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/credit_notes endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CreditNoteListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(
        username="API_USERNAME",
        password="API_PASSWORD",
        token="API_TOKEN",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.credit_note.list()
    try:
        pydantic.TypeAdapter(models.CreditNoteListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
