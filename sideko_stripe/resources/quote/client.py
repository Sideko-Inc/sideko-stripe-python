import typing
import typing_extensions

from sideko_stripe.core import (
    AsyncBaseClient,
    BinaryResponse,
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


class QuoteClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["accepted", "canceled", "draft", "open"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        test_clock: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.QuoteListResponse:
        """
        List all quotes

        <p>Returns a list of your quotes.</p>

        GET /v1/quotes

        Args:
            customer: The ID of the customer whose quotes will be retrieved.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the quote.
            test_clock: Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.list()
        ```
        """
        models.QuoteListResponse.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
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
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "accepted", "canceled", "draft", "open"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(test_clock, type_utils.NotGiven):
            encode_query_param(
                _query,
                "test_clock",
                to_encodable(item=test_clock, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/quotes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.QuoteListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        quote: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Retrieve a quote

        <p>Retrieves the quote with the given ID.</p>

        GET /v1/quotes/{quote}

        Args:
            expand: Specifies which fields in the response should be expanded.
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.get(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/quotes/{quote}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    def computed_upfront_line_items(
        self,
        *,
        quote: str,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.QuoteComputedUpfrontLineItemsResponse:
        """
        Retrieve a quote's upfront line items

        <p>When retrieving a quote, there is an includable <a href="https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items"><strong>computed.upfront.line_items</strong></a> property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.</p>

        GET /v1/quotes/{quote}/computed_upfront_line_items

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.computed_upfront_line_items(quote="string")
        ```
        """
        models.QuoteComputedUpfrontLineItemsResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
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
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v1/quotes/{quote}/computed_upfront_line_items",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.QuoteComputedUpfrontLineItemsResponse,
            request_options=request_options or default_request_options(),
        )

    def pdf(
        self,
        *,
        quote: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Download quote PDF

        <p>Download the PDF for a finalized quote. Explanation for special handling can be found <a href="https://docs.stripe.com/quotes/overview#quote_pdf">here</a></p>

        GET /v1/quotes/{quote}/pdf

        Args:
            expand: Specifies which fields in the response should be expanded.
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.pdf(quote="string")
        ```
        """
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
            path=f"/v1/quotes/{quote}/pdf",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.QuoteCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Create a quote

        <p>A quote models prices and services for a customer. Default options for <code>header</code>, <code>description</code>, <code>footer</code>, and <code>expires_at</code> can be set in the dashboard via the <a href="https://dashboard.stripe.com/settings/billing/quote">quote template</a>.</p>

        POST /v1/quotes

        Args:
            data: QuoteCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.create()
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteCreateBody,
                style={
                    "application_fee_amount": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "collection_method": "form",
                    "customer": "form",
                    "default_tax_rates": "deepObject",
                    "description": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "form",
                    "footer": "deepObject",
                    "from_quote": "deepObject",
                    "header": "deepObject",
                    "invoice_settings": "deepObject",
                    "line_items": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "deepObject",
                    "subscription_data": "deepObject",
                    "test_clock": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "application_fee_amount": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "collection_method": True,
                    "customer": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "expand": True,
                    "expires_at": True,
                    "footer": True,
                    "from_quote": True,
                    "header": True,
                    "invoice_settings": True,
                    "line_items": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "subscription_data": True,
                    "test_clock": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/quotes",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Update a quote

        <p>A quote models prices and services for a customer.</p>

        POST /v1/quotes/{quote}

        Args:
            data: QuoteUpdateBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.update(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteUpdateBody,
                style={
                    "application_fee_amount": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "collection_method": "form",
                    "customer": "form",
                    "default_tax_rates": "deepObject",
                    "description": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "form",
                    "footer": "deepObject",
                    "header": "deepObject",
                    "invoice_settings": "deepObject",
                    "line_items": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "deepObject",
                    "subscription_data": "deepObject",
                    "transfer_data": "deepObject",
                },
                explode={
                    "application_fee_amount": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "collection_method": True,
                    "customer": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "expand": True,
                    "expires_at": True,
                    "footer": True,
                    "header": True,
                    "invoice_settings": True,
                    "line_items": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "subscription_data": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    def accept(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteAcceptBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Accept a quote

        <p>Accepts the specified quote.</p>

        POST /v1/quotes/{quote}/accept

        Args:
            data: QuoteAcceptBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.accept(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteAcceptBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}/accept",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Cancel a quote

        <p>Cancels the quote.</p>

        POST /v1/quotes/{quote}/cancel

        Args:
            data: QuoteCancelBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.cancel(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    def finalize(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteFinalizeBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Finalize a quote

        <p>Finalizes the quote.</p>

        POST /v1/quotes/{quote}/finalize

        Args:
            data: QuoteFinalizeBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quote.finalize(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteFinalizeBody,
                style={"expand": "deepObject", "expires_at": "form"},
                explode={"expand": True, "expires_at": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}/finalize",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )


class AsyncQuoteClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["accepted", "canceled", "draft", "open"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        test_clock: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.QuoteListResponse:
        """
        List all quotes

        <p>Returns a list of your quotes.</p>

        GET /v1/quotes

        Args:
            customer: The ID of the customer whose quotes will be retrieved.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the quote.
            test_clock: Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.list()
        ```
        """
        models.QuoteListResponse.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
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
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "accepted", "canceled", "draft", "open"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(test_clock, type_utils.NotGiven):
            encode_query_param(
                _query,
                "test_clock",
                to_encodable(item=test_clock, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/quotes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.QuoteListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        quote: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Retrieve a quote

        <p>Retrieves the quote with the given ID.</p>

        GET /v1/quotes/{quote}

        Args:
            expand: Specifies which fields in the response should be expanded.
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.get(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/quotes/{quote}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    async def computed_upfront_line_items(
        self,
        *,
        quote: str,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.QuoteComputedUpfrontLineItemsResponse:
        """
        Retrieve a quote's upfront line items

        <p>When retrieving a quote, there is an includable <a href="https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items"><strong>computed.upfront.line_items</strong></a> property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.</p>

        GET /v1/quotes/{quote}/computed_upfront_line_items

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.computed_upfront_line_items(quote="string")
        ```
        """
        models.QuoteComputedUpfrontLineItemsResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
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
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v1/quotes/{quote}/computed_upfront_line_items",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.QuoteComputedUpfrontLineItemsResponse,
            request_options=request_options or default_request_options(),
        )

    async def pdf(
        self,
        *,
        quote: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Download quote PDF

        <p>Download the PDF for a finalized quote. Explanation for special handling can be found <a href="https://docs.stripe.com/quotes/overview#quote_pdf">here</a></p>

        GET /v1/quotes/{quote}/pdf

        Args:
            expand: Specifies which fields in the response should be expanded.
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.pdf(quote="string")
        ```
        """
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
            path=f"/v1/quotes/{quote}/pdf",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.QuoteCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Create a quote

        <p>A quote models prices and services for a customer. Default options for <code>header</code>, <code>description</code>, <code>footer</code>, and <code>expires_at</code> can be set in the dashboard via the <a href="https://dashboard.stripe.com/settings/billing/quote">quote template</a>.</p>

        POST /v1/quotes

        Args:
            data: QuoteCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.create()
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteCreateBody,
                style={
                    "application_fee_amount": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "collection_method": "form",
                    "customer": "form",
                    "default_tax_rates": "deepObject",
                    "description": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "form",
                    "footer": "deepObject",
                    "from_quote": "deepObject",
                    "header": "deepObject",
                    "invoice_settings": "deepObject",
                    "line_items": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "deepObject",
                    "subscription_data": "deepObject",
                    "test_clock": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "application_fee_amount": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "collection_method": True,
                    "customer": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "expand": True,
                    "expires_at": True,
                    "footer": True,
                    "from_quote": True,
                    "header": True,
                    "invoice_settings": True,
                    "line_items": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "subscription_data": True,
                    "test_clock": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/quotes",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Update a quote

        <p>A quote models prices and services for a customer.</p>

        POST /v1/quotes/{quote}

        Args:
            data: QuoteUpdateBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.update(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteUpdateBody,
                style={
                    "application_fee_amount": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "collection_method": "form",
                    "customer": "form",
                    "default_tax_rates": "deepObject",
                    "description": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "form",
                    "footer": "deepObject",
                    "header": "deepObject",
                    "invoice_settings": "deepObject",
                    "line_items": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "deepObject",
                    "subscription_data": "deepObject",
                    "transfer_data": "deepObject",
                },
                explode={
                    "application_fee_amount": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "collection_method": True,
                    "customer": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "expand": True,
                    "expires_at": True,
                    "footer": True,
                    "header": True,
                    "invoice_settings": True,
                    "line_items": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "subscription_data": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    async def accept(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteAcceptBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Accept a quote

        <p>Accepts the specified quote.</p>

        POST /v1/quotes/{quote}/accept

        Args:
            data: QuoteAcceptBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.accept(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteAcceptBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}/accept",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Cancel a quote

        <p>Cancels the quote.</p>

        POST /v1/quotes/{quote}/cancel

        Args:
            data: QuoteCancelBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.cancel(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )

    async def finalize(
        self,
        *,
        quote: str,
        data: typing.Union[
            typing.Optional[params.QuoteFinalizeBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quote:
        """
        Finalize a quote

        <p>Finalizes the quote.</p>

        POST /v1/quotes/{quote}/finalize

        Args:
            data: QuoteFinalizeBody
            quote: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quote.finalize(quote="string")
        ```
        """
        models.Quote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerQuoteFinalizeBody,
                style={"expand": "deepObject", "expires_at": "form"},
                explode={"expand": True, "expires_at": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/quotes/{quote}/finalize",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Quote,
            request_options=request_options or default_request_options(),
        )
