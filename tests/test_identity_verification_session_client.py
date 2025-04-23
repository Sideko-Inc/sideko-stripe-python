import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_redact_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions/{session}/redact endpoint.

    Operation: redact
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.identity.verification_session.redact(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_redact_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions/{session}/redact endpoint.

    Operation: redact
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.identity.verification_session.redact(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_cancel_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions/{session}/cancel endpoint.

    Operation: cancel
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.identity.verification_session.cancel(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_cancel_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions/{session}/cancel endpoint.

    Operation: cancel
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.identity.verification_session.cancel(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_update_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions/{session} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.identity.verification_session.update(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions/{session} endpoint.

    Operation: update
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.identity.verification_session.update(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.identity.verification_session.create()
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_generated_success():
    """Tests a POST request to the /v1/identity/verification_sessions endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.identity.verification_session.create()
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v1/identity/verification_sessions/{session} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.identity.verification_session.get(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v1/identity/verification_sessions/{session} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityVerificationSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.identity.verification_session.get(session="string")
    try:
        pydantic.TypeAdapter(models.IdentityVerificationSession).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v1/identity/verification_sessions endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityVerificationSessionListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Stripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.identity.verification_session.list()
    try:
        pydantic.TypeAdapter(
            models.IdentityVerificationSessionListResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v1/identity/verification_sessions endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityVerificationSessionListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncStripe(token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.identity.verification_session.list()
    try:
        pydantic.TypeAdapter(
            models.IdentityVerificationSessionListResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
