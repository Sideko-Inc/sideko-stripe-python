import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class DisputeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        charge: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Dispute:
        """
        <p>Retrieve a dispute for a specified charge.</p>

        GET /v1/charges/{charge}/dispute

        Args:
            expand: Specifies which fields in the response should be expanded.
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.dispute.get(charge="string")
        ```
        """
        models.Dispute.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(expand, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expand",
                to_encodable(item=expand, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v1/charges/{charge}/dispute",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Dispute,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeDisputeCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Dispute:
        """


        POST /v1/charges/{charge}/dispute

        Args:
            data: ChargeDisputeCreateBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.dispute.create(charge="string")
        ```
        """
        models.Dispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeDisputeCreateBody,
                style={
                    "evidence": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "submit": "form",
                },
                explode={
                    "evidence": True,
                    "expand": True,
                    "metadata": True,
                    "submit": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/dispute",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Dispute,
            request_options=request_options or default_request_options(),
        )

    def close(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeDisputeCloseBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Dispute:
        """


        POST /v1/charges/{charge}/dispute/close

        Args:
            data: ChargeDisputeCloseBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.dispute.close(charge="string")
        ```
        """
        models.Dispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeDisputeCloseBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/dispute/close",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Dispute,
            request_options=request_options or default_request_options(),
        )


class AsyncDisputeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        charge: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Dispute:
        """
        <p>Retrieve a dispute for a specified charge.</p>

        GET /v1/charges/{charge}/dispute

        Args:
            expand: Specifies which fields in the response should be expanded.
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.dispute.get(charge="string")
        ```
        """
        models.Dispute.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(expand, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expand",
                to_encodable(item=expand, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v1/charges/{charge}/dispute",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Dispute,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeDisputeCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Dispute:
        """


        POST /v1/charges/{charge}/dispute

        Args:
            data: ChargeDisputeCreateBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.dispute.create(charge="string")
        ```
        """
        models.Dispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeDisputeCreateBody,
                style={
                    "evidence": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "submit": "form",
                },
                explode={
                    "evidence": True,
                    "expand": True,
                    "metadata": True,
                    "submit": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/dispute",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Dispute,
            request_options=request_options or default_request_options(),
        )

    async def close(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeDisputeCloseBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Dispute:
        """


        POST /v1/charges/{charge}/dispute/close

        Args:
            data: ChargeDisputeCloseBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.dispute.close(charge="string")
        ```
        """
        models.Dispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeDisputeCloseBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/dispute/close",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Dispute,
            request_options=request_options or default_request_options(),
        )
