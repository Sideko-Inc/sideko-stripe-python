import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_fund_cash_balance_200_success_default():
    """Tests a POST request to the /v1/test_helpers/customers/{customer}/fund_cash_balance endpoint.

    Operation: fund_cash_balance
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CustomerCashBalanceTransaction

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
    response = client.test_helper.customer.fund_cash_balance(
        amount=123, currency="string", customer="string"
    )
    try:
        pydantic.TypeAdapter(models.CustomerCashBalanceTransaction).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_fund_cash_balance_200_success_default():
    """Tests a POST request to the /v1/test_helpers/customers/{customer}/fund_cash_balance endpoint.

    Operation: fund_cash_balance
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CustomerCashBalanceTransaction

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
    response = await client.test_helper.customer.fund_cash_balance(
        amount=123, currency="string", customer="string"
    )
    try:
        pydantic.TypeAdapter(models.CustomerCashBalanceTransaction).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
