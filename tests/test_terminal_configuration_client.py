import pydantic
import pytest
import typing

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_update_200_generated_success():
    """Tests a POST request to the /v1/terminal/configurations/{configuration} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.TerminalConfiguration, models.DeletedTerminalConfiguration]

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
    response = client.terminal.configuration.update(configuration="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/terminal/configurations/{configuration} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.TerminalConfiguration, models.DeletedTerminalConfiguration]

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
    response = await client.terminal.configuration.update(configuration="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_generated_success():
    """Tests a POST request to the /v1/terminal/configurations endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalConfiguration

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
    response = client.terminal.configuration.create()
    try:
        pydantic.TypeAdapter(models.TerminalConfiguration).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_generated_success():
    """Tests a POST request to the /v1/terminal/configurations endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalConfiguration

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
    response = await client.terminal.configuration.create()
    try:
        pydantic.TypeAdapter(models.TerminalConfiguration).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/terminal/configurations/{configuration} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.TerminalConfiguration, models.DeletedTerminalConfiguration]

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
    response = client.terminal.configuration.get(configuration="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/terminal/configurations/{configuration} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.TerminalConfiguration, models.DeletedTerminalConfiguration]

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
    response = await client.terminal.configuration.get(configuration="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/terminal/configurations endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TerminalConfigurationListResponse

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
    response = client.terminal.configuration.list()
    try:
        pydantic.TypeAdapter(models.TerminalConfigurationListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/terminal/configurations endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TerminalConfigurationListResponse

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
    response = await client.terminal.configuration.list()
    try:
        pydantic.TypeAdapter(models.TerminalConfigurationListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v1/terminal/configurations/{configuration} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DeletedTerminalConfiguration

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
    response = client.terminal.configuration.delete(configuration="string")
    try:
        pydantic.TypeAdapter(models.DeletedTerminalConfiguration).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v1/terminal/configurations/{configuration} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DeletedTerminalConfiguration

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
    response = await client.terminal.configuration.delete(configuration="string")
    try:
        pydantic.TypeAdapter(models.DeletedTerminalConfiguration).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
