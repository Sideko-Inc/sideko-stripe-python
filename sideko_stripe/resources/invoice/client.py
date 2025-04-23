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
from sideko_stripe.resources.invoice.line import AsyncLineClient, LineClient
from sideko_stripe.types import models, params


class InvoiceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.line = LineClient(base_client=self._base_client)

    def delete(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedInvoice:
        """
        Delete a draft invoice

        <p>Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be <a href="#void_invoice">voided</a>.</p>

        DELETE /v1/invoices/{invoice}

        Args:
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.delete(invoice="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/invoices/{invoice}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedInvoice,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        collection_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["charge_automatically", "send_invoice"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.InvoiceListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        due_date: typing.Union[
            typing.Optional[typing.Union[params.InvoiceListDueDateObj0, int]],
            type_utils.NotGiven,
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
                typing_extensions.Literal[
                    "draft", "open", "paid", "uncollectible", "void"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        subscription: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceListResponse:
        """
        List all invoices

        <p>You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.</p>

        GET /v1/invoices

        Args:
            collection_method: The collection method of the invoice to retrieve. Either `charge_automatically` or `send_invoice`.
            created: Only return invoices that were created during the given date interval.
            customer: Only return invoices for the customer specified by this customer ID.
            due_date: typing.Union[InvoiceListDueDateObj0, int]
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)
            subscription: Only return invoices for the subscription specified by this subscription ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.list()
        ```
        """
        models.InvoiceListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(collection_method, type_utils.NotGiven):
            encode_query_param(
                _query,
                "collection_method",
                to_encodable(
                    item=collection_method,
                    dump_with=typing_extensions.Literal[
                        "charge_automatically", "send_invoice"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerInvoiceListCreatedObj0, int
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
        if not isinstance(due_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "due_date",
                to_encodable(
                    item=due_date,
                    dump_with=typing.Union[
                        params._SerializerInvoiceListDueDateObj0, int
                    ],
                ),
                style="deepObject",
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
                        "draft", "open", "paid", "uncollectible", "void"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(subscription, type_utils.NotGiven):
            encode_query_param(
                _query,
                "subscription",
                to_encodable(item=subscription, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/invoices",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceListResponse,
            request_options=request_options or default_request_options(),
        )

    def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceSearchResponse:
        """
        Search invoices

        <p>Search for invoices you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/invoices/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for invoices](https://stripe.com/docs/search#query-fields-for-invoices).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.search(query="string")
        ```
        """
        models.InvoiceSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/invoices/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceSearchResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        invoice: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Retrieve an invoice

        <p>Retrieves the invoice with the given ID.</p>

        GET /v1/invoices/{invoice}

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.get(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/invoices/{invoice}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.InvoiceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Create an invoice

        <p>This endpoint creates a draft invoice for a given customer. The invoice remains a draft until you <a href="#finalize_invoice">finalize</a> the invoice, which allows you to <a href="#pay_invoice">pay</a> or <a href="#send_invoice">send</a> the invoice to your customers.</p>

        POST /v1/invoices

        Args:
            data: InvoiceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.create()
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceCreateBody,
                style={
                    "account_tax_ids": "deepObject",
                    "application_fee_amount": "form",
                    "auto_advance": "form",
                    "automatic_tax": "deepObject",
                    "automatically_finalizes_at": "form",
                    "collection_method": "form",
                    "currency": "form",
                    "custom_fields": "deepObject",
                    "customer": "form",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "form",
                    "default_tax_rates": "deepObject",
                    "description": "form",
                    "discounts": "deepObject",
                    "due_date": "form",
                    "effective_at": "form",
                    "expand": "deepObject",
                    "footer": "form",
                    "from_invoice": "deepObject",
                    "issuer": "deepObject",
                    "metadata": "deepObject",
                    "number": "form",
                    "on_behalf_of": "form",
                    "payment_settings": "deepObject",
                    "pending_invoice_items_behavior": "form",
                    "rendering": "deepObject",
                    "shipping_cost": "deepObject",
                    "shipping_details": "deepObject",
                    "statement_descriptor": "form",
                    "subscription": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "account_tax_ids": True,
                    "application_fee_amount": True,
                    "auto_advance": True,
                    "automatic_tax": True,
                    "automatically_finalizes_at": True,
                    "collection_method": True,
                    "currency": True,
                    "custom_fields": True,
                    "customer": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "due_date": True,
                    "effective_at": True,
                    "expand": True,
                    "footer": True,
                    "from_invoice": True,
                    "issuer": True,
                    "metadata": True,
                    "number": True,
                    "on_behalf_of": True,
                    "payment_settings": True,
                    "pending_invoice_items_behavior": True,
                    "rendering": True,
                    "shipping_cost": True,
                    "shipping_details": True,
                    "statement_descriptor": True,
                    "subscription": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/invoices",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def preview(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.InvoicePreviewBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Create a preview invoice

        <p>At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.</p>

        <p>Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.</p>

        <p>You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the <code>subscription_details.proration_date</code> parameter when doing the actual subscription update. The recommended way to get only the prorations being previewed is to consider only proration line items where <code>period[start]</code> is equal to the <code>subscription_details.proration_date</code> value passed in the request. </p>

        <p>Note: Currency conversion calculations use the latest exchange rates. Exchange rates may vary between the time of the preview and the time of the actual invoice creation. <a href="https://docs.stripe.com/currencies/conversions">Learn more</a></p>

        POST /v1/invoices/create_preview

        Args:
            data: InvoicePreviewBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.preview()
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoicePreviewBody,
                style={
                    "automatic_tax": "deepObject",
                    "currency": "form",
                    "customer": "form",
                    "customer_details": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_items": "deepObject",
                    "issuer": "deepObject",
                    "on_behalf_of": "deepObject",
                    "preview_mode": "form",
                    "schedule": "form",
                    "schedule_details": "deepObject",
                    "subscription": "form",
                    "subscription_details": "deepObject",
                },
                explode={
                    "automatic_tax": True,
                    "currency": True,
                    "customer": True,
                    "customer_details": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_items": True,
                    "issuer": True,
                    "on_behalf_of": True,
                    "preview_mode": True,
                    "schedule": True,
                    "schedule_details": True,
                    "subscription": True,
                    "subscription_details": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/invoices/create_preview",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Update an invoice

        <p>Draft invoices are fully editable. Once an invoice is <a href="/docs/billing/invoices/workflow#finalized">finalized</a>,
        monetary values, as well as <code>collection_method</code>, become uneditable.</p>

        <p>If you would like to stop the Stripe Billing engine from automatically finalizing, reattempting payments on,
        sending reminders for, or <a href="/docs/billing/invoices/reconciliation">automatically reconciling</a> invoices, pass
        <code>auto_advance=false</code>.</p>

        POST /v1/invoices/{invoice}

        Args:
            data: InvoiceUpdateBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.update(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceUpdateBody,
                style={
                    "account_tax_ids": "deepObject",
                    "application_fee_amount": "form",
                    "auto_advance": "form",
                    "automatic_tax": "deepObject",
                    "automatically_finalizes_at": "form",
                    "collection_method": "form",
                    "custom_fields": "deepObject",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "deepObject",
                    "default_tax_rates": "deepObject",
                    "description": "form",
                    "discounts": "deepObject",
                    "due_date": "form",
                    "effective_at": "deepObject",
                    "expand": "deepObject",
                    "footer": "form",
                    "issuer": "deepObject",
                    "metadata": "deepObject",
                    "number": "deepObject",
                    "on_behalf_of": "deepObject",
                    "payment_settings": "deepObject",
                    "rendering": "deepObject",
                    "shipping_cost": "deepObject",
                    "shipping_details": "deepObject",
                    "statement_descriptor": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "account_tax_ids": True,
                    "application_fee_amount": True,
                    "auto_advance": True,
                    "automatic_tax": True,
                    "automatically_finalizes_at": True,
                    "collection_method": True,
                    "custom_fields": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "due_date": True,
                    "effective_at": True,
                    "expand": True,
                    "footer": True,
                    "issuer": True,
                    "metadata": True,
                    "number": True,
                    "on_behalf_of": True,
                    "payment_settings": True,
                    "rendering": True,
                    "shipping_cost": True,
                    "shipping_details": True,
                    "statement_descriptor": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def finalize(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceFinalizeBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Finalize an invoice

        <p>Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.</p>

        POST /v1/invoices/{invoice}/finalize

        Args:
            data: InvoiceFinalizeBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.finalize(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceFinalizeBody,
                style={"auto_advance": "form", "expand": "deepObject"},
                explode={"auto_advance": True, "expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/finalize",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def mark_uncollectible(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceMarkUncollectibleBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Mark an invoice as uncollectible

        <p>Marking an invoice as uncollectible is useful for keeping track of bad debts that can be written off for accounting purposes.</p>

        POST /v1/invoices/{invoice}/mark_uncollectible

        Args:
            data: InvoiceMarkUncollectibleBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.mark_uncollectible(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceMarkUncollectibleBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/mark_uncollectible",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def pay(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoicePayBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Pay an invoice

        <p>Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your <a href="https://dashboard.stripe.com/account/billing/automatic">subscriptions settings</a>. However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.</p>

        POST /v1/invoices/{invoice}/pay

        Args:
            data: InvoicePayBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.pay(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoicePayBody,
                style={
                    "expand": "deepObject",
                    "forgive": "form",
                    "mandate": "deepObject",
                    "off_session": "form",
                    "paid_out_of_band": "form",
                    "payment_method": "form",
                    "source": "form",
                },
                explode={
                    "expand": True,
                    "forgive": True,
                    "mandate": True,
                    "off_session": True,
                    "paid_out_of_band": True,
                    "payment_method": True,
                    "source": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/pay",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def send(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceSendBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Send an invoice for manual payment

        <p>Stripe will automatically send invoices to customers according to your <a href="https://dashboard.stripe.com/account/billing/automatic">subscriptions settings</a>. However, if you’d like to manually send an invoice to your customer out of the normal schedule, you can do so. When sending invoices that have already been paid, there will be no reference to the payment in the email.</p>

        <p>Requests made in test-mode result in no emails being sent, despite sending an <code>invoice.sent</code> event.</p>

        POST /v1/invoices/{invoice}/send

        Args:
            data: InvoiceSendBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.send(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceSendBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/send",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    def void(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceVoidBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Void an invoice

        <p>Mark a finalized invoice as void. This cannot be undone. Voiding an invoice is similar to <a href="#delete_invoice">deletion</a>, however it only applies to finalized invoices and maintains a papertrail where the invoice can still be found.</p>

        <p>Consult with local regulations to determine whether and how an invoice might be amended, canceled, or voided in the jurisdiction you’re doing business in. You might need to <a href="#create_invoice">issue another invoice</a> or <a href="#create_credit_note">credit note</a> instead. Stripe recommends that you consult with your legal counsel for advice specific to your business.</p>

        POST /v1/invoices/{invoice}/void

        Args:
            data: InvoiceVoidBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice.void(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceVoidBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/void",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )


class AsyncInvoiceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.line = AsyncLineClient(base_client=self._base_client)

    async def delete(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedInvoice:
        """
        Delete a draft invoice

        <p>Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be <a href="#void_invoice">voided</a>.</p>

        DELETE /v1/invoices/{invoice}

        Args:
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.delete(invoice="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/invoices/{invoice}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedInvoice,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        collection_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["charge_automatically", "send_invoice"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.InvoiceListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        due_date: typing.Union[
            typing.Optional[typing.Union[params.InvoiceListDueDateObj0, int]],
            type_utils.NotGiven,
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
                typing_extensions.Literal[
                    "draft", "open", "paid", "uncollectible", "void"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        subscription: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceListResponse:
        """
        List all invoices

        <p>You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.</p>

        GET /v1/invoices

        Args:
            collection_method: The collection method of the invoice to retrieve. Either `charge_automatically` or `send_invoice`.
            created: Only return invoices that were created during the given date interval.
            customer: Only return invoices for the customer specified by this customer ID.
            due_date: typing.Union[InvoiceListDueDateObj0, int]
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)
            subscription: Only return invoices for the subscription specified by this subscription ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.list()
        ```
        """
        models.InvoiceListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(collection_method, type_utils.NotGiven):
            encode_query_param(
                _query,
                "collection_method",
                to_encodable(
                    item=collection_method,
                    dump_with=typing_extensions.Literal[
                        "charge_automatically", "send_invoice"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerInvoiceListCreatedObj0, int
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
        if not isinstance(due_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "due_date",
                to_encodable(
                    item=due_date,
                    dump_with=typing.Union[
                        params._SerializerInvoiceListDueDateObj0, int
                    ],
                ),
                style="deepObject",
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
                        "draft", "open", "paid", "uncollectible", "void"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(subscription, type_utils.NotGiven):
            encode_query_param(
                _query,
                "subscription",
                to_encodable(item=subscription, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/invoices",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceListResponse,
            request_options=request_options or default_request_options(),
        )

    async def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceSearchResponse:
        """
        Search invoices

        <p>Search for invoices you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/invoices/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for invoices](https://stripe.com/docs/search#query-fields-for-invoices).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.search(query="string")
        ```
        """
        models.InvoiceSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/invoices/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceSearchResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        invoice: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Retrieve an invoice

        <p>Retrieves the invoice with the given ID.</p>

        GET /v1/invoices/{invoice}

        Args:
            expand: Specifies which fields in the response should be expanded.
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.get(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/invoices/{invoice}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.InvoiceCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Create an invoice

        <p>This endpoint creates a draft invoice for a given customer. The invoice remains a draft until you <a href="#finalize_invoice">finalize</a> the invoice, which allows you to <a href="#pay_invoice">pay</a> or <a href="#send_invoice">send</a> the invoice to your customers.</p>

        POST /v1/invoices

        Args:
            data: InvoiceCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.create()
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceCreateBody,
                style={
                    "account_tax_ids": "deepObject",
                    "application_fee_amount": "form",
                    "auto_advance": "form",
                    "automatic_tax": "deepObject",
                    "automatically_finalizes_at": "form",
                    "collection_method": "form",
                    "currency": "form",
                    "custom_fields": "deepObject",
                    "customer": "form",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "form",
                    "default_tax_rates": "deepObject",
                    "description": "form",
                    "discounts": "deepObject",
                    "due_date": "form",
                    "effective_at": "form",
                    "expand": "deepObject",
                    "footer": "form",
                    "from_invoice": "deepObject",
                    "issuer": "deepObject",
                    "metadata": "deepObject",
                    "number": "form",
                    "on_behalf_of": "form",
                    "payment_settings": "deepObject",
                    "pending_invoice_items_behavior": "form",
                    "rendering": "deepObject",
                    "shipping_cost": "deepObject",
                    "shipping_details": "deepObject",
                    "statement_descriptor": "form",
                    "subscription": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "account_tax_ids": True,
                    "application_fee_amount": True,
                    "auto_advance": True,
                    "automatic_tax": True,
                    "automatically_finalizes_at": True,
                    "collection_method": True,
                    "currency": True,
                    "custom_fields": True,
                    "customer": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "due_date": True,
                    "effective_at": True,
                    "expand": True,
                    "footer": True,
                    "from_invoice": True,
                    "issuer": True,
                    "metadata": True,
                    "number": True,
                    "on_behalf_of": True,
                    "payment_settings": True,
                    "pending_invoice_items_behavior": True,
                    "rendering": True,
                    "shipping_cost": True,
                    "shipping_details": True,
                    "statement_descriptor": True,
                    "subscription": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/invoices",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def preview(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.InvoicePreviewBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Create a preview invoice

        <p>At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.</p>

        <p>Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.</p>

        <p>You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the <code>subscription_details.proration_date</code> parameter when doing the actual subscription update. The recommended way to get only the prorations being previewed is to consider only proration line items where <code>period[start]</code> is equal to the <code>subscription_details.proration_date</code> value passed in the request. </p>

        <p>Note: Currency conversion calculations use the latest exchange rates. Exchange rates may vary between the time of the preview and the time of the actual invoice creation. <a href="https://docs.stripe.com/currencies/conversions">Learn more</a></p>

        POST /v1/invoices/create_preview

        Args:
            data: InvoicePreviewBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.preview()
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoicePreviewBody,
                style={
                    "automatic_tax": "deepObject",
                    "currency": "form",
                    "customer": "form",
                    "customer_details": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_items": "deepObject",
                    "issuer": "deepObject",
                    "on_behalf_of": "deepObject",
                    "preview_mode": "form",
                    "schedule": "form",
                    "schedule_details": "deepObject",
                    "subscription": "form",
                    "subscription_details": "deepObject",
                },
                explode={
                    "automatic_tax": True,
                    "currency": True,
                    "customer": True,
                    "customer_details": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_items": True,
                    "issuer": True,
                    "on_behalf_of": True,
                    "preview_mode": True,
                    "schedule": True,
                    "schedule_details": True,
                    "subscription": True,
                    "subscription_details": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/invoices/create_preview",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Update an invoice

        <p>Draft invoices are fully editable. Once an invoice is <a href="/docs/billing/invoices/workflow#finalized">finalized</a>,
        monetary values, as well as <code>collection_method</code>, become uneditable.</p>

        <p>If you would like to stop the Stripe Billing engine from automatically finalizing, reattempting payments on,
        sending reminders for, or <a href="/docs/billing/invoices/reconciliation">automatically reconciling</a> invoices, pass
        <code>auto_advance=false</code>.</p>

        POST /v1/invoices/{invoice}

        Args:
            data: InvoiceUpdateBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.update(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceUpdateBody,
                style={
                    "account_tax_ids": "deepObject",
                    "application_fee_amount": "form",
                    "auto_advance": "form",
                    "automatic_tax": "deepObject",
                    "automatically_finalizes_at": "form",
                    "collection_method": "form",
                    "custom_fields": "deepObject",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "deepObject",
                    "default_tax_rates": "deepObject",
                    "description": "form",
                    "discounts": "deepObject",
                    "due_date": "form",
                    "effective_at": "deepObject",
                    "expand": "deepObject",
                    "footer": "form",
                    "issuer": "deepObject",
                    "metadata": "deepObject",
                    "number": "deepObject",
                    "on_behalf_of": "deepObject",
                    "payment_settings": "deepObject",
                    "rendering": "deepObject",
                    "shipping_cost": "deepObject",
                    "shipping_details": "deepObject",
                    "statement_descriptor": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "account_tax_ids": True,
                    "application_fee_amount": True,
                    "auto_advance": True,
                    "automatic_tax": True,
                    "automatically_finalizes_at": True,
                    "collection_method": True,
                    "custom_fields": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "description": True,
                    "discounts": True,
                    "due_date": True,
                    "effective_at": True,
                    "expand": True,
                    "footer": True,
                    "issuer": True,
                    "metadata": True,
                    "number": True,
                    "on_behalf_of": True,
                    "payment_settings": True,
                    "rendering": True,
                    "shipping_cost": True,
                    "shipping_details": True,
                    "statement_descriptor": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def finalize(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceFinalizeBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Finalize an invoice

        <p>Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.</p>

        POST /v1/invoices/{invoice}/finalize

        Args:
            data: InvoiceFinalizeBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.finalize(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceFinalizeBody,
                style={"auto_advance": "form", "expand": "deepObject"},
                explode={"auto_advance": True, "expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/finalize",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def mark_uncollectible(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceMarkUncollectibleBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Mark an invoice as uncollectible

        <p>Marking an invoice as uncollectible is useful for keeping track of bad debts that can be written off for accounting purposes.</p>

        POST /v1/invoices/{invoice}/mark_uncollectible

        Args:
            data: InvoiceMarkUncollectibleBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.mark_uncollectible(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceMarkUncollectibleBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/mark_uncollectible",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def pay(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoicePayBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Pay an invoice

        <p>Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your <a href="https://dashboard.stripe.com/account/billing/automatic">subscriptions settings</a>. However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.</p>

        POST /v1/invoices/{invoice}/pay

        Args:
            data: InvoicePayBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.pay(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoicePayBody,
                style={
                    "expand": "deepObject",
                    "forgive": "form",
                    "mandate": "deepObject",
                    "off_session": "form",
                    "paid_out_of_band": "form",
                    "payment_method": "form",
                    "source": "form",
                },
                explode={
                    "expand": True,
                    "forgive": True,
                    "mandate": True,
                    "off_session": True,
                    "paid_out_of_band": True,
                    "payment_method": True,
                    "source": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/pay",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def send(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceSendBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Send an invoice for manual payment

        <p>Stripe will automatically send invoices to customers according to your <a href="https://dashboard.stripe.com/account/billing/automatic">subscriptions settings</a>. However, if you’d like to manually send an invoice to your customer out of the normal schedule, you can do so. When sending invoices that have already been paid, there will be no reference to the payment in the email.</p>

        <p>Requests made in test-mode result in no emails being sent, despite sending an <code>invoice.sent</code> event.</p>

        POST /v1/invoices/{invoice}/send

        Args:
            data: InvoiceSendBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.send(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceSendBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/send",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )

    async def void(
        self,
        *,
        invoice: str,
        data: typing.Union[
            typing.Optional[params.InvoiceVoidBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoice:
        """
        Void an invoice

        <p>Mark a finalized invoice as void. This cannot be undone. Voiding an invoice is similar to <a href="#delete_invoice">deletion</a>, however it only applies to finalized invoices and maintains a papertrail where the invoice can still be found.</p>

        <p>Consult with local regulations to determine whether and how an invoice might be amended, canceled, or voided in the jurisdiction you’re doing business in. You might need to <a href="#create_invoice">issue another invoice</a> or <a href="#create_credit_note">credit note</a> instead. Stripe recommends that you consult with your legal counsel for advice specific to your business.</p>

        POST /v1/invoices/{invoice}/void

        Args:
            data: InvoiceVoidBody
            invoice: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice.void(invoice="string")
        ```
        """
        models.Invoice.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceVoidBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoices/{invoice}/void",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Invoice,
            request_options=request_options or default_request_options(),
        )
