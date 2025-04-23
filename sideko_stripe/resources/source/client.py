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
from sideko_stripe.resources.source.mandate_notifications import (
    AsyncMandateNotificationsClient,
    MandateNotificationsClient,
)
from sideko_stripe.resources.source.source_transactions import (
    AsyncSourceTransactionsClient,
    SourceTransactionsClient,
)
from sideko_stripe.types import models, params


class SourceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.mandate_notifications = MandateNotificationsClient(
            base_client=self._base_client
        )
        self.source_transactions = SourceTransactionsClient(
            base_client=self._base_client
        )

    def get(
        self,
        *,
        source: str,
        client_secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        Retrieve a source

        <p>Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.</p>

        GET /v1/sources/{source}

        Args:
            client_secret: The client secret of the source. Required if a publishable key is used to retrieve the source.
            expand: Specifies which fields in the response should be expanded.
            source: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.source.get(source="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(client_secret, type_utils.NotGiven):
            encode_query_param(
                _query,
                "client_secret",
                to_encodable(item=client_secret, dump_with=str),
                style="form",
                explode=True,
            )
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
            path=f"/v1/sources/{source}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.SourceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        Shares a source

        <p>Creates a new source object.</p>

        POST /v1/sources

        Args:
            data: SourceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.source.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSourceCreateBody,
                style={
                    "amount": "form",
                    "currency": "form",
                    "customer": "form",
                    "expand": "deepObject",
                    "flow": "form",
                    "mandate": "deepObject",
                    "metadata": "deepObject",
                    "original_source": "form",
                    "owner": "deepObject",
                    "receiver": "deepObject",
                    "redirect": "deepObject",
                    "source_order": "deepObject",
                    "statement_descriptor": "form",
                    "token": "form",
                    "type": "form",
                    "usage": "form",
                },
                explode={
                    "amount": True,
                    "currency": True,
                    "customer": True,
                    "expand": True,
                    "flow": True,
                    "mandate": True,
                    "metadata": True,
                    "original_source": True,
                    "owner": True,
                    "receiver": True,
                    "redirect": True,
                    "source_order": True,
                    "statement_descriptor": True,
                    "token": True,
                    "type": True,
                    "usage": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/sources",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        source: str,
        data: typing.Union[
            typing.Optional[params.SourceUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        Update a source

        <p>Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request accepts the <code>metadata</code> and <code>owner</code> as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our <a href="/docs/sources">payment method guides</a> for more detail.</p>

        POST /v1/sources/{source}

        Args:
            data: SourceUpdateBody
            source: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.source.update(source="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSourceUpdateBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "mandate": "deepObject",
                    "metadata": "deepObject",
                    "owner": "deepObject",
                    "source_order": "deepObject",
                },
                explode={
                    "amount": True,
                    "expand": True,
                    "mandate": True,
                    "metadata": True,
                    "owner": True,
                    "source_order": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/sources/{source}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )

    def verify(
        self,
        *,
        source: str,
        values: typing.List[str],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        <p>Verify a given source.</p>

        POST /v1/sources/{source}/verify

        Args:
            expand: Specifies which fields in the response should be expanded.
            source: str
            values: The values needed to verify the source.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.source.verify(source="string", values=["string"])
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "values": values},
            dump_with=params._SerializerSourceVerifyBody,
            style={"expand": "deepObject", "values": "deepObject"},
            explode={"expand": True, "values": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/sources/{source}/verify",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )


class AsyncSourceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.mandate_notifications = AsyncMandateNotificationsClient(
            base_client=self._base_client
        )
        self.source_transactions = AsyncSourceTransactionsClient(
            base_client=self._base_client
        )

    async def get(
        self,
        *,
        source: str,
        client_secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        Retrieve a source

        <p>Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.</p>

        GET /v1/sources/{source}

        Args:
            client_secret: The client secret of the source. Required if a publishable key is used to retrieve the source.
            expand: Specifies which fields in the response should be expanded.
            source: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.source.get(source="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(client_secret, type_utils.NotGiven):
            encode_query_param(
                _query,
                "client_secret",
                to_encodable(item=client_secret, dump_with=str),
                style="form",
                explode=True,
            )
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
            path=f"/v1/sources/{source}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.SourceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        Shares a source

        <p>Creates a new source object.</p>

        POST /v1/sources

        Args:
            data: SourceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.source.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSourceCreateBody,
                style={
                    "amount": "form",
                    "currency": "form",
                    "customer": "form",
                    "expand": "deepObject",
                    "flow": "form",
                    "mandate": "deepObject",
                    "metadata": "deepObject",
                    "original_source": "form",
                    "owner": "deepObject",
                    "receiver": "deepObject",
                    "redirect": "deepObject",
                    "source_order": "deepObject",
                    "statement_descriptor": "form",
                    "token": "form",
                    "type": "form",
                    "usage": "form",
                },
                explode={
                    "amount": True,
                    "currency": True,
                    "customer": True,
                    "expand": True,
                    "flow": True,
                    "mandate": True,
                    "metadata": True,
                    "original_source": True,
                    "owner": True,
                    "receiver": True,
                    "redirect": True,
                    "source_order": True,
                    "statement_descriptor": True,
                    "token": True,
                    "type": True,
                    "usage": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/sources",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        source: str,
        data: typing.Union[
            typing.Optional[params.SourceUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        Update a source

        <p>Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request accepts the <code>metadata</code> and <code>owner</code> as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our <a href="/docs/sources">payment method guides</a> for more detail.</p>

        POST /v1/sources/{source}

        Args:
            data: SourceUpdateBody
            source: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.source.update(source="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSourceUpdateBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "mandate": "deepObject",
                    "metadata": "deepObject",
                    "owner": "deepObject",
                    "source_order": "deepObject",
                },
                explode={
                    "amount": True,
                    "expand": True,
                    "mandate": True,
                    "metadata": True,
                    "owner": True,
                    "source_order": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/sources/{source}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )

    async def verify(
        self,
        *,
        source: str,
        values: typing.List[str],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Source:
        """
        <p>Verify a given source.</p>

        POST /v1/sources/{source}/verify

        Args:
            expand: Specifies which fields in the response should be expanded.
            source: str
            values: The values needed to verify the source.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.source.verify(source="string", values=["string"])
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "values": values},
            dump_with=params._SerializerSourceVerifyBody,
            style={"expand": "deepObject", "values": "deepObject"},
            explode={"expand": True, "values": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/sources/{source}/verify",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Source,
            request_options=request_options or default_request_options(),
        )
