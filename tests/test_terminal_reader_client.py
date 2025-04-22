import pydantic
import pytest
import typing

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_set_reader_display_200_success_default():
    """Tests a POST request to the /v1/terminal/readers/{reader}/set_reader_display endpoint.

    Operation: set_reader_display
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReader

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
    response = client.terminal.reader.set_reader_display(reader="string", type_="cart")
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_set_reader_display_200_success_default():
    """Tests a POST request to the /v1/terminal/readers/{reader}/set_reader_display endpoint.

    Operation: set_reader_display
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReader

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
    response = await client.terminal.reader.set_reader_display(
        reader="string", type_="cart"
    )
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_refund_payment_200_generated_success():
    """Tests a POST request to the /v1/terminal/readers/{reader}/refund_payment endpoint.

    Operation: refund_payment
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReader

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
    response = client.terminal.reader.refund_payment(reader="string")
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_refund_payment_200_generated_success():
    """Tests a POST request to the /v1/terminal/readers/{reader}/refund_payment endpoint.

    Operation: refund_payment
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReader

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
    response = await client.terminal.reader.refund_payment(reader="string")
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_process_setup_intent_200_success_default():
    """Tests a POST request to the /v1/terminal/readers/{reader}/process_setup_intent endpoint.

    Operation: process_setup_intent
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReader

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
    response = client.terminal.reader.process_setup_intent(
        allow_redisplay="always", reader="string", setup_intent="string"
    )
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_process_setup_intent_200_success_default():
    """Tests a POST request to the /v1/terminal/readers/{reader}/process_setup_intent endpoint.

    Operation: process_setup_intent
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReader

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
    response = await client.terminal.reader.process_setup_intent(
        allow_redisplay="always", reader="string", setup_intent="string"
    )
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_process_payment_intent_200_success_default():
    """Tests a POST request to the /v1/terminal/readers/{reader}/process_payment_intent endpoint.

    Operation: process_payment_intent
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReader

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
    response = client.terminal.reader.process_payment_intent(
        payment_intent="string", reader="string"
    )
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_process_payment_intent_200_success_default():
    """Tests a POST request to the /v1/terminal/readers/{reader}/process_payment_intent endpoint.

    Operation: process_payment_intent
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReader

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
    response = await client.terminal.reader.process_payment_intent(
        payment_intent="string", reader="string"
    )
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_cancel_action_200_generated_success():
    """Tests a POST request to the /v1/terminal/readers/{reader}/cancel_action endpoint.

    Operation: cancel_action
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReader

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
    response = client.terminal.reader.cancel_action(reader="string")
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_cancel_action_200_generated_success():
    """Tests a POST request to the /v1/terminal/readers/{reader}/cancel_action endpoint.

    Operation: cancel_action
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReader

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
    response = await client.terminal.reader.cancel_action(reader="string")
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_generated_success():
    """Tests a POST request to the /v1/terminal/readers/{reader} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.TerminalReader, models.DeletedTerminalReader]

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
    response = client.terminal.reader.update(reader="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.TerminalReader, models.DeletedTerminalReader]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/terminal/readers/{reader} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.TerminalReader, models.DeletedTerminalReader]

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
    response = await client.terminal.reader.update(reader="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.TerminalReader, models.DeletedTerminalReader]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_success_default():
    """Tests a POST request to the /v1/terminal/readers endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReader

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
    response = client.terminal.reader.create(registration_code="string")
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/terminal/readers endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReader

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
    response = await client.terminal.reader.create(registration_code="string")
    try:
        pydantic.TypeAdapter(models.TerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/terminal/readers/{reader} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.TerminalReader, models.DeletedTerminalReader]

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
    response = client.terminal.reader.get(reader="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.TerminalReader, models.DeletedTerminalReader]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/terminal/readers/{reader} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.TerminalReader, models.DeletedTerminalReader]

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
    response = await client.terminal.reader.get(reader="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.TerminalReader, models.DeletedTerminalReader]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/terminal/readers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalReaderListResponse

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
    response = client.terminal.reader.list()
    try:
        pydantic.TypeAdapter(models.TerminalReaderListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/terminal/readers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalReaderListResponse

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
    response = await client.terminal.reader.list()
    try:
        pydantic.TypeAdapter(models.TerminalReaderListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v1/terminal/readers/{reader} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DeletedTerminalReader

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
    response = client.terminal.reader.delete(reader="string")
    try:
        pydantic.TypeAdapter(models.DeletedTerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v1/terminal/readers/{reader} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DeletedTerminalReader

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
    response = await client.terminal.reader.delete(reader="string")
    try:
        pydantic.TypeAdapter(models.DeletedTerminalReader).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
