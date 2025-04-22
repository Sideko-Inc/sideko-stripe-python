import pydantic
import pytest

from sideko_stripe import AsyncStripe, Stripe
from sideko_stripe.environment import Environment
from sideko_stripe.types import models


def test_reject_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject endpoint.

    Operation: reject
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingPersonalizationDesign

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
    response = client.test_helper.issuing.personalization_design.reject(
        personalization_design="string", rejection_reasons={}
    )
    try:
        pydantic.TypeAdapter(models.IssuingPersonalizationDesign).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_reject_200_success_default():
    """Tests a POST request to the /v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject endpoint.

    Operation: reject
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingPersonalizationDesign

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
    response = await client.test_helper.issuing.personalization_design.reject(
        personalization_design="string", rejection_reasons={}
    )
    try:
        pydantic.TypeAdapter(models.IssuingPersonalizationDesign).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_deactivate_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate endpoint.

    Operation: deactivate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingPersonalizationDesign

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
    response = client.test_helper.issuing.personalization_design.deactivate(
        personalization_design="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingPersonalizationDesign).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_deactivate_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate endpoint.

    Operation: deactivate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingPersonalizationDesign

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
    response = await client.test_helper.issuing.personalization_design.deactivate(
        personalization_design="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingPersonalizationDesign).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_activate_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate endpoint.

    Operation: activate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IssuingPersonalizationDesign

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
    response = client.test_helper.issuing.personalization_design.activate(
        personalization_design="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingPersonalizationDesign).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_activate_200_generated_success():
    """Tests a POST request to the /v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate endpoint.

    Operation: activate
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IssuingPersonalizationDesign

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
    response = await client.test_helper.issuing.personalization_design.activate(
        personalization_design="string"
    )
    try:
        pydantic.TypeAdapter(models.IssuingPersonalizationDesign).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
