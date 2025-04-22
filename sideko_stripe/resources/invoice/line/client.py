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


class LineClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        invoice: str,
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
    ) -> models.InvoiceLineListResponse:
        """
        Retrieve an invoice's line items

        <p>When retrieving an invoice, you’ll get a <strong>lines</strong> property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

        GET /v1/invoices/{invoice}/lines

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.line.list(invoice="string")
        ```
        """
        models.InvoiceLineListResponse.model_rebuild(
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
            path=f"/v1/invoices/{invoice}/lines",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceLineListResponse,
            request_options=request_options or default_request_options(),
        )

    def create_many(
        self,
        *,
        invoice: str,
        lines: typing.List[params.InvoiceLineCreateManyBodyLinesItem],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceLineCreateManyBodyInvoiceMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Bulk add invoice line items

        <p>Adds multiple line items to an invoice. This is only possible when an invoice is still a draft.</p>

        POST /v1/invoices/{invoice}/add_lines

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            invoice: str
            lines: The line items to add.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.line.create_many(invoice="string", lines=[{}])
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "invoice_metadata": invoice_metadata,
                "lines": lines,
            },
            dump_with=params._SerializerInvoiceLineCreateManyBody,
            style={
                "expand": "deepObject",
                "invoice_metadata": "deepObject",
                "lines": "deepObject",
            },
            explode={"expand": True, "invoice_metadata": True, "lines": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/add_lines",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        invoice: str,
        line_item_id: str,
        data: typing.Union[
            typing.Optional[params.InvoiceLineUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LineItem:
        """
        Update an invoice's line item

        <p>Updates an invoice’s line item. Some fields, such as <code>tax_amounts</code>, only live on the invoice line item,
        so they can only be updated through this endpoint. Other fields, such as <code>amount</code>, live on both the invoice
        item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well.
        Updating an invoice’s line item is only possible before the invoice is finalized.</p>

        POST /v1/invoices/{invoice}/lines/{line_item_id}

        Args:
            data: InvoiceLineUpdateBody
            invoice: Invoice ID of line item
            line_item_id: Invoice line item ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.line.update(invoice="string", line_item_id="string")
        ```
        """
        models.LineItem.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceLineUpdateBody,
                style={
                    "amount": "form",
                    "description": "form",
                    "discountable": "form",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "period": "deepObject",
                    "price_data": "deepObject",
                    "pricing": "deepObject",
                    "quantity": "form",
                    "tax_amounts": "deepObject",
                    "tax_rates": "deepObject",
                },
                explode={
                    "amount": True,
                    "description": True,
                    "discountable": True,
                    "discounts": True,
                    "expand": True,
                    "metadata": True,
                    "period": True,
                    "price_data": True,
                    "pricing": True,
                    "quantity": True,
                    "tax_amounts": True,
                    "tax_rates": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/lines/{line_item_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.LineItem,
            request_options=request_options or default_request_options(),
        )

    def remove_many(
        self,
        *,
        invoice: str,
        lines: typing.List[params.InvoiceLineRemoveManyBodyLinesItem],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceLineRemoveManyBodyInvoiceMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Bulk remove invoice line items

        <p>Removes multiple line items from an invoice. This is only possible when an invoice is still a draft.</p>

        POST /v1/invoices/{invoice}/remove_lines

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            invoice: str
            lines: The line items to remove.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.line.remove_many(
            invoice="string", lines=[{"behavior": "delete", "id": "string"}]
        )
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "invoice_metadata": invoice_metadata,
                "lines": lines,
            },
            dump_with=params._SerializerInvoiceLineRemoveManyBody,
            style={
                "expand": "deepObject",
                "invoice_metadata": "deepObject",
                "lines": "deepObject",
            },
            explode={"expand": True, "invoice_metadata": True, "lines": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/remove_lines",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def update_many(
        self,
        *,
        invoice: str,
        lines: typing.List[params.InvoiceLineUpdateManyBodyLinesItem],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceLineUpdateManyBodyInvoiceMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Bulk update invoice line items

        <p>Updates multiple line items on an invoice. This is only possible when an invoice is still a draft.</p>

        POST /v1/invoices/{invoice}/update_lines

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.
            invoice: str
            lines: The line items to update.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.line.update_many(invoice="string", lines=[{"id": "string"}])
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "invoice_metadata": invoice_metadata,
                "lines": lines,
            },
            dump_with=params._SerializerInvoiceLineUpdateManyBody,
            style={
                "expand": "deepObject",
                "invoice_metadata": "deepObject",
                "lines": "deepObject",
            },
            explode={"expand": True, "invoice_metadata": True, "lines": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/update_lines",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )


class AsyncLineClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        invoice: str,
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
    ) -> models.InvoiceLineListResponse:
        """
        Retrieve an invoice's line items

        <p>When retrieving an invoice, you’ll get a <strong>lines</strong> property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

        GET /v1/invoices/{invoice}/lines

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.line.list(invoice="string")
        ```
        """
        models.InvoiceLineListResponse.model_rebuild(
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
            path=f"/v1/invoices/{invoice}/lines",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceLineListResponse,
            request_options=request_options or default_request_options(),
        )

    async def create_many(
        self,
        *,
        invoice: str,
        lines: typing.List[params.InvoiceLineCreateManyBodyLinesItem],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceLineCreateManyBodyInvoiceMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Bulk add invoice line items

        <p>Adds multiple line items to an invoice. This is only possible when an invoice is still a draft.</p>

        POST /v1/invoices/{invoice}/add_lines

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            invoice: str
            lines: The line items to add.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.line.create_many(invoice="string", lines=[{}])
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "invoice_metadata": invoice_metadata,
                "lines": lines,
            },
            dump_with=params._SerializerInvoiceLineCreateManyBody,
            style={
                "expand": "deepObject",
                "invoice_metadata": "deepObject",
                "lines": "deepObject",
            },
            explode={"expand": True, "invoice_metadata": True, "lines": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/add_lines",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        invoice: str,
        line_item_id: str,
        data: typing.Union[
            typing.Optional[params.InvoiceLineUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LineItem:
        """
        Update an invoice's line item

        <p>Updates an invoice’s line item. Some fields, such as <code>tax_amounts</code>, only live on the invoice line item,
        so they can only be updated through this endpoint. Other fields, such as <code>amount</code>, live on both the invoice
        item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well.
        Updating an invoice’s line item is only possible before the invoice is finalized.</p>

        POST /v1/invoices/{invoice}/lines/{line_item_id}

        Args:
            data: InvoiceLineUpdateBody
            invoice: Invoice ID of line item
            line_item_id: Invoice line item ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.line.update(invoice="string", line_item_id="string")
        ```
        """
        models.LineItem.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceLineUpdateBody,
                style={
                    "amount": "form",
                    "description": "form",
                    "discountable": "form",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "period": "deepObject",
                    "price_data": "deepObject",
                    "pricing": "deepObject",
                    "quantity": "form",
                    "tax_amounts": "deepObject",
                    "tax_rates": "deepObject",
                },
                explode={
                    "amount": True,
                    "description": True,
                    "discountable": True,
                    "discounts": True,
                    "expand": True,
                    "metadata": True,
                    "period": True,
                    "price_data": True,
                    "pricing": True,
                    "quantity": True,
                    "tax_amounts": True,
                    "tax_rates": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/lines/{line_item_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.LineItem,
            request_options=request_options or default_request_options(),
        )

    async def remove_many(
        self,
        *,
        invoice: str,
        lines: typing.List[params.InvoiceLineRemoveManyBodyLinesItem],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceLineRemoveManyBodyInvoiceMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Bulk remove invoice line items

        <p>Removes multiple line items from an invoice. This is only possible when an invoice is still a draft.</p>

        POST /v1/invoices/{invoice}/remove_lines

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            invoice: str
            lines: The line items to remove.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.line.remove_many(
            invoice="string", lines=[{"behavior": "delete", "id": "string"}]
        )
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "invoice_metadata": invoice_metadata,
                "lines": lines,
            },
            dump_with=params._SerializerInvoiceLineRemoveManyBody,
            style={
                "expand": "deepObject",
                "invoice_metadata": "deepObject",
                "lines": "deepObject",
            },
            explode={"expand": True, "invoice_metadata": True, "lines": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/remove_lines",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def update_many(
        self,
        *,
        invoice: str,
        lines: typing.List[params.InvoiceLineUpdateManyBodyLinesItem],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceLineUpdateManyBodyInvoiceMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Bulk update invoice line items

        <p>Updates multiple line items on an invoice. This is only possible when an invoice is still a draft.</p>

        POST /v1/invoices/{invoice}/update_lines

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.
            invoice: str
            lines: The line items to update.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.line.update_many(
            invoice="string", lines=[{"id": "string"}]
        )
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "invoice_metadata": invoice_metadata,
                "lines": lines,
            },
            dump_with=params._SerializerInvoiceLineUpdateManyBody,
            style={
                "expand": "deepObject",
                "invoice_metadata": "deepObject",
                "lines": "deepObject",
            },
            explode={"expand": True, "invoice_metadata": True, "lines": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/update_lines",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )
