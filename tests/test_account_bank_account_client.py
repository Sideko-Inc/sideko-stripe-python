import pydantic
import pytest
import typing

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_update_200_generated_success():
    """Tests a POST request to the /v1/accounts/{account}/bank_accounts/{id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.BankAccount, models.Card]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.account.bank_account.update(account="string", id="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.BankAccount, models.Card]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/accounts/{account}/bank_accounts/{id} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.BankAccount, models.Card]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.account.bank_account.update(account="string", id="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.BankAccount, models.Card]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_generated_success():
    """Tests a POST request to the /v1/accounts/{account}/bank_accounts endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.BankAccount, models.Card]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.account.bank_account.create(account="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.BankAccount, models.Card]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_generated_success():
    """Tests a POST request to the /v1/accounts/{account}/bank_accounts endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.BankAccount, models.Card]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.account.bank_account.create(account="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.BankAccount, models.Card]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/accounts/{account}/bank_accounts/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.BankAccount, models.Card]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.account.bank_account.get(account="string", id="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.BankAccount, models.Card]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/accounts/{account}/bank_accounts/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.BankAccount, models.Card]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.account.bank_account.get(account="string", id="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.BankAccount, models.Card]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v1/accounts/{account}/bank_accounts/{id} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.DeletedBankAccount, models.DeletedCard]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.account.bank_account.delete(account="string", id="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.DeletedBankAccount, models.DeletedCard]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v1/accounts/{account}/bank_accounts/{id} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.DeletedBankAccount, models.DeletedCard]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.account.bank_account.delete(account="string", id="string")
    try:
        pydantic.TypeAdapter(
            typing.Union[models.DeletedBankAccount, models.DeletedCard]
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
