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


class CustomerSessionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        components: params.CustomerSessionCreateBodyComponents,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerSession:
        """
        Create a Customer Session

        <p>Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.</p>

        POST /v1/customer_sessions

        Args:
            expand: Specifies which fields in the response should be expanded.
            components: Configuration for each component. Exactly 1 component must be enabled.
            customer: The ID of an existing customer for which to create the Customer Session.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer_session.create(components={}, customer="string")
        ```
        """
        models.CustomerSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"expand": expand, "components": components, "customer": customer},
            dump_with=params._SerializerCustomerSessionCreateBody,
            style={
                "components": "deepObject",
                "customer": "form",
                "expand": "deepObject",
            },
            explode={"components": True, "customer": True, "expand": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/customer_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.CustomerSession,
            request_options=request_options or default_request_options(),
        )


class AsyncCustomerSessionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        components: params.CustomerSessionCreateBodyComponents,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerSession:
        """
        Create a Customer Session

        <p>Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.</p>

        POST /v1/customer_sessions

        Args:
            expand: Specifies which fields in the response should be expanded.
            components: Configuration for each component. Exactly 1 component must be enabled.
            customer: The ID of an existing customer for which to create the Customer Session.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer_session.create(components={}, customer="string")
        ```
        """
        models.CustomerSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"expand": expand, "components": components, "customer": customer},
            dump_with=params._SerializerCustomerSessionCreateBody,
            style={
                "components": "deepObject",
                "customer": "form",
                "expand": "deepObject",
            },
            explode={"components": True, "customer": True, "expand": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/customer_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.CustomerSession,
            request_options=request_options or default_request_options(),
        )
