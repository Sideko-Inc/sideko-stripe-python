import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_verify_microdeposits_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/verify_microdeposits endpoint.

    Operation: verify_microdeposits
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.verify_microdeposits(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_verify_microdeposits_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/verify_microdeposits endpoint.

    Operation: verify_microdeposits
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.verify_microdeposits(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_increment_authorization_200_success_default():
    """Tests a POST request to the /v1/payment_intents/{intent}/increment_authorization endpoint.

    Operation: increment_authorization
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.increment_authorization(
        amount=123, intent="string"
    )
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_increment_authorization_200_success_default():
    """Tests a POST request to the /v1/payment_intents/{intent}/increment_authorization endpoint.

    Operation: increment_authorization
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.increment_authorization(
        amount=123, intent="string"
    )
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_confirm_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/confirm endpoint.

    Operation: confirm
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.confirm(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_confirm_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/confirm endpoint.

    Operation: confirm
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.confirm(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_capture_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/capture endpoint.

    Operation: capture
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.capture(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_capture_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/capture endpoint.

    Operation: capture
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.capture(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_cancel_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/cancel endpoint.

    Operation: cancel
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.cancel(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_cancel_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/cancel endpoint.

    Operation: cancel
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.cancel(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_apply_customer_balance_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/apply_customer_balance endpoint.

    Operation: apply_customer_balance
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.apply_customer_balance(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_apply_customer_balance_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent}/apply_customer_balance endpoint.

    Operation: apply_customer_balance
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.apply_customer_balance(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.update(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/payment_intents/{intent} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.update(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_success_default():
    """Tests a POST request to the /v1/payment_intents endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.create(amount=123, currency="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /v1/payment_intents endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.create(amount=123, currency="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/payment_intents/{intent} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.get(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/payment_intents/{intent} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntent

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.get(intent="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntent).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_search_200_generated_success():
    """Tests a GET request to the /v1/payment_intents/search endpoint.

    Operation: search
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntentSearchResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.search(query="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntentSearchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_search_200_generated_success():
    """Tests a GET request to the /v1/payment_intents/search endpoint.

    Operation: search
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntentSearchResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.search(query="string")
    try:
        pydantic.TypeAdapter(models.PaymentIntentSearchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/payment_intents endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaymentIntentListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.payment_intent.list()
    try:
        pydantic.TypeAdapter(models.PaymentIntentListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/payment_intents endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaymentIntentListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.payment_intent.list()
    try:
        pydantic.TypeAdapter(models.PaymentIntentListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
