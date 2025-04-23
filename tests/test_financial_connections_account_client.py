import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_unsubscribe_200_success_default():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/unsubscribe endpoint.

    Operation: unsubscribe
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.financial_connections.account.unsubscribe(
        account="string", features=["transactions"]
    )
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_unsubscribe_200_success_default():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/unsubscribe endpoint.

    Operation: unsubscribe
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.financial_connections.account.unsubscribe(
        account="string", features=["transactions"]
    )
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_subscribe_200_success_default():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/subscribe endpoint.

    Operation: subscribe
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.financial_connections.account.subscribe(
        account="string", features=["transactions"]
    )
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_subscribe_200_success_default():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/subscribe endpoint.

    Operation: subscribe
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.financial_connections.account.subscribe(
        account="string", features=["transactions"]
    )
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_refresh_200_success_default():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/refresh endpoint.

    Operation: refresh
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.financial_connections.account.refresh(
        account="string", features=["balance"]
    )
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_refresh_200_success_default():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/refresh endpoint.

    Operation: refresh
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.financial_connections.account.refresh(
        account="string", features=["balance"]
    )
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_disconnect_200_generated_success():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/disconnect endpoint.

    Operation: disconnect
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.financial_connections.account.disconnect(account="string")
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_disconnect_200_generated_success():
    """Tests a POST request to the /v1/financial_connections/accounts/{account}/disconnect endpoint.

    Operation: disconnect
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.financial_connections.account.disconnect(account="string")
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/financial_connections/accounts/{account} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.financial_connections.account.get(account="string")
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/financial_connections/accounts/{account} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.FinancialConnectionsAccount

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.financial_connections.account.get(account="string")
    try:
        pydantic.TypeAdapter(models.FinancialConnectionsAccount).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/financial_connections/accounts endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.FinancialConnectionsAccountListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.financial_connections.account.list()
    try:
        pydantic.TypeAdapter(
            models.FinancialConnectionsAccountListResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/financial_connections/accounts endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.FinancialConnectionsAccountListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.financial_connections.account.list()
    try:
        pydantic.TypeAdapter(
            models.FinancialConnectionsAccountListResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
