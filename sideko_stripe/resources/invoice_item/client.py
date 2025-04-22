import typing
import typing_extensions

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


class InvoiceItemClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        invoiceitem: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedInvoiceitem:
        """
        Delete an invoice item

        <p>Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.</p>

        DELETE /v1/invoiceitems/{invoiceitem}

        Args:
            invoiceitem: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_item.delete(invoiceitem="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/invoiceitems/{invoiceitem}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedInvoiceitem,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.InvoiceItemListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pending: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceItemListResponse:
        """
        List all invoice items

        <p>Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.</p>

        GET /v1/invoiceitems

        Args:
            created: Only return invoice items that were created during the given date interval.
            customer: The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            invoice: Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            pending: Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_item.list()
        ```
        """
        models.InvoiceItemListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerInvoiceItemListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
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
        if not isinstance(invoice, type_utils.NotGiven):
            encode_query_param(
                _query,
                "invoice",
                to_encodable(item=invoice, dump_with=str),
                style="form",
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
        if not isinstance(pending, type_utils.NotGiven):
            encode_query_param(
                _query,
                "pending",
                to_encodable(item=pending, dump_with=bool),
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
            path="/v1/invoiceitems",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceItemListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        invoiceitem: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoiceitem:
        """
        Retrieve an invoice item

        <p>Retrieves the invoice item with the given ID.</p>

        GET /v1/invoiceitems/{invoiceitem}

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoiceitem: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_item.get(invoiceitem="string")
        ```
        """
        models.Invoiceitem.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/invoiceitems/{invoiceitem}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Invoiceitem,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        customer: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        discountable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        discounts: typing.Union[
            typing.Optional[
                typing.Union[
                    typing.List[params.InvoiceItemCreateBodyDiscountsArr0Item], str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceItemCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        period: typing.Union[
            typing.Optional[params.InvoiceItemCreateBodyPeriod], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        price_data: typing.Union[
            typing.Optional[params.InvoiceItemCreateBodyPriceData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pricing: typing.Union[
            typing.Optional[params.InvoiceItemCreateBodyPricing], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quantity: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        subscription: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_code: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_rates: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit_amount_decimal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoiceitem:
        """
        Create an invoice item

        <p>Creates an item to be added to a draft invoice (up to 250 items per invoice). If no invoice is specified, the item will be on the next invoice created for the customer specified.</p>

        POST /v1/invoiceitems

        Args:
            amount: The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            description: An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
            discountable: Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items.
            discounts: The coupons and promotion codes to redeem into discounts for the invoice item or invoice line item.
            expand: Specifies which fields in the response should be expanded.
            invoice: The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            period: The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
            price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            pricing: The pricing information for the invoice item.
            quantity: Non-negative integer. The quantity of units for the invoice item.
            subscription: The ID of a subscription to add this invoice item to. When left blank, the invoice item is added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription.
            tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
            tax_rates: The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.
            unit_amount_decimal: The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places.
            customer: The ID of the customer who will be billed when this invoice item is billed.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_item.create(customer="string")
        ```
        """
        models.Invoiceitem.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "currency": currency,
                "description": description,
                "discountable": discountable,
                "discounts": discounts,
                "expand": expand,
                "invoice": invoice,
                "metadata": metadata,
                "period": period,
                "price_data": price_data,
                "pricing": pricing,
                "quantity": quantity,
                "subscription": subscription,
                "tax_behavior": tax_behavior,
                "tax_code": tax_code,
                "tax_rates": tax_rates,
                "unit_amount_decimal": unit_amount_decimal,
                "customer": customer,
            },
            dump_with=params._SerializerInvoiceItemCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "customer": "form",
                "description": "form",
                "discountable": "form",
                "discounts": "deepObject",
                "expand": "deepObject",
                "invoice": "form",
                "metadata": "deepObject",
                "period": "deepObject",
                "price_data": "deepObject",
                "pricing": "deepObject",
                "quantity": "form",
                "subscription": "form",
                "tax_behavior": "form",
                "tax_code": "deepObject",
                "tax_rates": "deepObject",
                "unit_amount_decimal": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "customer": True,
                "description": True,
                "discountable": True,
                "discounts": True,
                "expand": True,
                "invoice": True,
                "metadata": True,
                "period": True,
                "price_data": True,
                "pricing": True,
                "quantity": True,
                "subscription": True,
                "tax_behavior": True,
                "tax_code": True,
                "tax_rates": True,
                "unit_amount_decimal": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/invoiceitems",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoiceitem,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        invoiceitem: str,
        data: typing.Union[
            typing.Optional[params.InvoiceItemUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoiceitem:
        """
        Update an invoice item

        <p>Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.</p>

        POST /v1/invoiceitems/{invoiceitem}

        Args:
            data: InvoiceItemUpdateBody
            invoiceitem: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_item.update(invoiceitem="string")
        ```
        """
        models.Invoiceitem.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceItemUpdateBody,
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
                    "tax_behavior": "form",
                    "tax_code": "deepObject",
                    "tax_rates": "deepObject",
                    "unit_amount_decimal": "form",
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
                    "tax_behavior": True,
                    "tax_code": True,
                    "tax_rates": True,
                    "unit_amount_decimal": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoiceitems/{invoiceitem}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoiceitem,
            request_options=request_options or default_request_options(),
        )


class AsyncInvoiceItemClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        invoiceitem: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedInvoiceitem:
        """
        Delete an invoice item

        <p>Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.</p>

        DELETE /v1/invoiceitems/{invoiceitem}

        Args:
            invoiceitem: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_item.delete(invoiceitem="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/invoiceitems/{invoiceitem}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedInvoiceitem,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.InvoiceItemListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pending: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceItemListResponse:
        """
        List all invoice items

        <p>Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.</p>

        GET /v1/invoiceitems

        Args:
            created: Only return invoice items that were created during the given date interval.
            customer: The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            invoice: Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            pending: Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_item.list()
        ```
        """
        models.InvoiceItemListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerInvoiceItemListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
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
        if not isinstance(invoice, type_utils.NotGiven):
            encode_query_param(
                _query,
                "invoice",
                to_encodable(item=invoice, dump_with=str),
                style="form",
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
        if not isinstance(pending, type_utils.NotGiven):
            encode_query_param(
                _query,
                "pending",
                to_encodable(item=pending, dump_with=bool),
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
            path="/v1/invoiceitems",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceItemListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        invoiceitem: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoiceitem:
        """
        Retrieve an invoice item

        <p>Retrieves the invoice item with the given ID.</p>

        GET /v1/invoiceitems/{invoiceitem}

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoiceitem: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_item.get(invoiceitem="string")
        ```
        """
        models.Invoiceitem.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/invoiceitems/{invoiceitem}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Invoiceitem,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        customer: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        discountable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        discounts: typing.Union[
            typing.Optional[
                typing.Union[
                    typing.List[params.InvoiceItemCreateBodyDiscountsArr0Item], str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.InvoiceItemCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        period: typing.Union[
            typing.Optional[params.InvoiceItemCreateBodyPeriod], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        price_data: typing.Union[
            typing.Optional[params.InvoiceItemCreateBodyPriceData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pricing: typing.Union[
            typing.Optional[params.InvoiceItemCreateBodyPricing], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quantity: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        subscription: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_code: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_rates: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit_amount_decimal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoiceitem:
        """
        Create an invoice item

        <p>Creates an item to be added to a draft invoice (up to 250 items per invoice). If no invoice is specified, the item will be on the next invoice created for the customer specified.</p>

        POST /v1/invoiceitems

        Args:
            amount: The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            description: An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
            discountable: Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items.
            discounts: The coupons and promotion codes to redeem into discounts for the invoice item or invoice line item.
            expand: Specifies which fields in the response should be expanded.
            invoice: The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            period: The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
            price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            pricing: The pricing information for the invoice item.
            quantity: Non-negative integer. The quantity of units for the invoice item.
            subscription: The ID of a subscription to add this invoice item to. When left blank, the invoice item is added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription.
            tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
            tax_rates: The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.
            unit_amount_decimal: The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places.
            customer: The ID of the customer who will be billed when this invoice item is billed.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_item.create(customer="string")
        ```
        """
        models.Invoiceitem.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "currency": currency,
                "description": description,
                "discountable": discountable,
                "discounts": discounts,
                "expand": expand,
                "invoice": invoice,
                "metadata": metadata,
                "period": period,
                "price_data": price_data,
                "pricing": pricing,
                "quantity": quantity,
                "subscription": subscription,
                "tax_behavior": tax_behavior,
                "tax_code": tax_code,
                "tax_rates": tax_rates,
                "unit_amount_decimal": unit_amount_decimal,
                "customer": customer,
            },
            dump_with=params._SerializerInvoiceItemCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "customer": "form",
                "description": "form",
                "discountable": "form",
                "discounts": "deepObject",
                "expand": "deepObject",
                "invoice": "form",
                "metadata": "deepObject",
                "period": "deepObject",
                "price_data": "deepObject",
                "pricing": "deepObject",
                "quantity": "form",
                "subscription": "form",
                "tax_behavior": "form",
                "tax_code": "deepObject",
                "tax_rates": "deepObject",
                "unit_amount_decimal": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "customer": True,
                "description": True,
                "discountable": True,
                "discounts": True,
                "expand": True,
                "invoice": True,
                "metadata": True,
                "period": True,
                "price_data": True,
                "pricing": True,
                "quantity": True,
                "subscription": True,
                "tax_behavior": True,
                "tax_code": True,
                "tax_rates": True,
                "unit_amount_decimal": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/invoiceitems",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoiceitem,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        invoiceitem: str,
        data: typing.Union[
            typing.Optional[params.InvoiceItemUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoiceitem:
        """
        Update an invoice item

        <p>Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.</p>

        POST /v1/invoiceitems/{invoiceitem}

        Args:
            data: InvoiceItemUpdateBody
            invoiceitem: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_item.update(invoiceitem="string")
        ```
        """
        models.Invoiceitem.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceItemUpdateBody,
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
                    "tax_behavior": "form",
                    "tax_code": "deepObject",
                    "tax_rates": "deepObject",
                    "unit_amount_decimal": "form",
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
                    "tax_behavior": True,
                    "tax_code": True,
                    "tax_rates": True,
                    "unit_amount_decimal": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoiceitems/{invoiceitem}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Invoiceitem,
            request_options=request_options or default_request_options(),
        )
