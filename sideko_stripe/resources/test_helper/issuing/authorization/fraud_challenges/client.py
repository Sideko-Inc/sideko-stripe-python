import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class FraudChallengesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def respond(
        self,
        *,
        authorization: str,
        confirmed: bool,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Respond to fraud challenge

        <p>Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond

        Args:
            expand: Specifies which fields in the response should be expanded.
            authorization: str
            confirmed: Whether to simulate the user confirming that the transaction was legitimate (true) or telling Stripe that it was fraudulent (false).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.authorization.fraud_challenges.respond(
            authorization="string", confirmed=True
        )
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "confirmed": confirmed},
            dump_with=params._SerializerTestHelperIssuingAuthorizationFraudChallengesRespondBody,
            style={"confirmed": "form", "expand": "deepObject"},
            explode={"confirmed": True, "expand": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )


class AsyncFraudChallengesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def respond(
        self,
        *,
        authorization: str,
        confirmed: bool,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Respond to fraud challenge

        <p>Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond

        Args:
            expand: Specifies which fields in the response should be expanded.
            authorization: str
            confirmed: Whether to simulate the user confirming that the transaction was legitimate (true) or telling Stripe that it was fraudulent (false).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.authorization.fraud_challenges.respond(
            authorization="string", confirmed=True
        )
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "confirmed": confirmed},
            dump_with=params._SerializerTestHelperIssuingAuthorizationFraudChallengesRespondBody,
            style={"confirmed": "form", "expand": "deepObject"},
            explode={"confirmed": True, "expand": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )
