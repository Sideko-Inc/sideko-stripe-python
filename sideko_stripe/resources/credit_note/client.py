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


class CreditNoteClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CreditNoteListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNoteListResponse:
        """
        List all credit notes

        <p>Returns a list of credit notes.</p>

        GET /v1/credit_notes

        Args:
            created: Only return credit notes that were created during the given date interval.
            customer: Only return credit notes for the customer specified by this customer ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            invoice: Only return credit notes for the invoice specified by this invoice ID.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.list()
        ```
        """
        models.CreditNoteListResponse.model_rebuild(
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
                        params._SerializerCreditNoteListCreatedObj0, int
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
            path="/v1/credit_notes",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNoteListResponse,
            request_options=request_options or default_request_options(),
        )

    def preview_1(
        self,
        *,
        invoice: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_type: typing.Union[
            typing.Optional[typing_extensions.Literal["credit_note", "none"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lines: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreview1LinesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        memo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.CreditNotePreview1Metadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        out_of_band_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        refund_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refunds: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreview1RefundsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.CreditNotePreview1ShippingCost], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Preview a credit note

        <p>Get a preview of a credit note without creating it.</p>

        GET /v1/credit_notes/preview

        Args:
            amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
            credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
            effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
            email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
            expand: Specifies which fields in the response should be expanded.
            lines: Line items that make up the credit note.
            memo: The credit note's memo appears on the credit note PDF.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
            reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
            refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
            refunds: Refunds to link to this credit note.
            shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
            invoice: ID of the invoice.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.preview_1(invoice="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "invoice",
            to_encodable(item=invoice, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "amount",
                to_encodable(item=amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(credit_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "credit_amount",
                to_encodable(item=credit_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(effective_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "effective_at",
                to_encodable(item=effective_at, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(email_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email_type",
                to_encodable(
                    item=email_type,
                    dump_with=typing_extensions.Literal["credit_note", "none"],
                ),
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
        if not isinstance(lines, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lines",
                to_encodable(
                    item=lines,
                    dump_with=typing.List[
                        params._SerializerCreditNotePreview1LinesItem
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(memo, type_utils.NotGiven):
            encode_query_param(
                _query,
                "memo",
                to_encodable(item=memo, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "metadata",
                to_encodable(
                    item=metadata,
                    dump_with=params._SerializerCreditNotePreview1Metadata,
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(out_of_band_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "out_of_band_amount",
                to_encodable(item=out_of_band_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(reason, type_utils.NotGiven):
            encode_query_param(
                _query,
                "reason",
                to_encodable(
                    item=reason,
                    dump_with=typing_extensions.Literal[
                        "duplicate",
                        "fraudulent",
                        "order_change",
                        "product_unsatisfactory",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(refund_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refund_amount",
                to_encodable(item=refund_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(refunds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refunds",
                to_encodable(
                    item=refunds,
                    dump_with=typing.List[
                        params._SerializerCreditNotePreview1RefundsItem
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(shipping_cost, type_utils.NotGiven):
            encode_query_param(
                _query,
                "shipping_cost",
                to_encodable(
                    item=shipping_cost,
                    dump_with=params._SerializerCreditNotePreview1ShippingCost,
                ),
                style="deepObject",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/credit_notes/preview",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    def preview(
        self,
        *,
        invoice: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_type: typing.Union[
            typing.Optional[typing_extensions.Literal["credit_note", "none"]],
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
        lines: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreviewLinesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        memo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.CreditNotePreviewMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        out_of_band_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        refund_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refunds: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreviewRefundsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.CreditNotePreviewShippingCost], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNotePreviewResponse:
        """
        Retrieve a credit note preview's line items

        <p>When retrieving a credit note preview, you’ll get a <strong>lines</strong> property containing the first handful of those items. This URL you can retrieve the full (paginated) list of line items.</p>

        GET /v1/credit_notes/preview/lines

        Args:
            amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
            credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
            effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
            email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lines: Line items that make up the credit note.
            memo: The credit note's memo appears on the credit note PDF.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
            reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
            refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
            refunds: Refunds to link to this credit note.
            shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            invoice: ID of the invoice.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.preview(invoice="string")
        ```
        """
        models.CreditNotePreviewResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "invoice",
            to_encodable(item=invoice, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "amount",
                to_encodable(item=amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(credit_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "credit_amount",
                to_encodable(item=credit_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(effective_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "effective_at",
                to_encodable(item=effective_at, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(email_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email_type",
                to_encodable(
                    item=email_type,
                    dump_with=typing_extensions.Literal["credit_note", "none"],
                ),
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
        if not isinstance(lines, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lines",
                to_encodable(
                    item=lines,
                    dump_with=typing.List[params._SerializerCreditNotePreviewLinesItem],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(memo, type_utils.NotGiven):
            encode_query_param(
                _query,
                "memo",
                to_encodable(item=memo, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "metadata",
                to_encodable(
                    item=metadata, dump_with=params._SerializerCreditNotePreviewMetadata
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(out_of_band_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "out_of_band_amount",
                to_encodable(item=out_of_band_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(reason, type_utils.NotGiven):
            encode_query_param(
                _query,
                "reason",
                to_encodable(
                    item=reason,
                    dump_with=typing_extensions.Literal[
                        "duplicate",
                        "fraudulent",
                        "order_change",
                        "product_unsatisfactory",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(refund_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refund_amount",
                to_encodable(item=refund_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(refunds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refunds",
                to_encodable(
                    item=refunds,
                    dump_with=typing.List[
                        params._SerializerCreditNotePreviewRefundsItem
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(shipping_cost, type_utils.NotGiven):
            encode_query_param(
                _query,
                "shipping_cost",
                to_encodable(
                    item=shipping_cost,
                    dump_with=params._SerializerCreditNotePreviewShippingCost,
                ),
                style="deepObject",
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
            path="/v1/credit_notes/preview/lines",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNotePreviewResponse,
            request_options=request_options or default_request_options(),
        )

    def lines(
        self,
        *,
        credit_note: str,
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
    ) -> models.CreditNoteLinesResponse:
        """
        Retrieve a credit note's line items

        <p>When retrieving a credit note, you’ll get a <strong>lines</strong> property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

        GET /v1/credit_notes/{credit_note}/lines

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            credit_note: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.lines(credit_note="string")
        ```
        """
        models.CreditNoteLinesResponse.model_rebuild(
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
            path=f"/v1/credit_notes/{credit_note}/lines",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNoteLinesResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Retrieve a credit note

        <p>Retrieves the credit note object with the given identifier.</p>

        GET /v1/credit_notes/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.get(id="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/credit_notes/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        invoice: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_type: typing.Union[
            typing.Optional[typing_extensions.Literal["credit_note", "none"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lines: typing.Union[
            typing.Optional[typing.List[params.CreditNoteCreateBodyLinesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        memo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.CreditNoteCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        out_of_band_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        refund_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refunds: typing.Union[
            typing.Optional[typing.List[params.CreditNoteCreateBodyRefundsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.CreditNoteCreateBodyShippingCost],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Create a credit note

        <p>Issue a credit note to adjust the amount of a finalized invoice. For a <code>status=open</code> invoice, a credit note reduces
        its <code>amount_due</code>. For a <code>status=paid</code> invoice, a credit note does not affect its <code>amount_due</code>. Instead, it can result
        in any combination of the following:</p>

        <ul>
        <li>Refund: create a new refund (using <code>refund_amount</code>) or link an existing refund (using <code>refund</code>).</li>
        <li>Customer balance credit: credit the customer’s balance (using <code>credit_amount</code>) which will be automatically applied to their next invoice when it’s finalized.</li>
        <li>Outside of Stripe credit: record the amount that is or will be credited outside of Stripe (using <code>out_of_band_amount</code>).</li>
        </ul>

        <p>For post-payment credit notes the sum of the refund, credit and outside of Stripe amounts must equal the credit note total.</p>

        <p>You may issue multiple credit notes for an invoice. Each credit note will increment the invoice’s <code>pre_payment_credit_notes_amount</code>
        or <code>post_payment_credit_notes_amount</code> depending on its <code>status</code> at the time of credit note creation.</p>

        POST /v1/credit_notes

        Args:
            amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
            credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
            effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
            email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
            expand: Specifies which fields in the response should be expanded.
            lines: Line items that make up the credit note.
            memo: The credit note's memo appears on the credit note PDF.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
            reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
            refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
            refunds: Refunds to link to this credit note.
            shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
            invoice: ID of the invoice.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.create(invoice="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "credit_amount": credit_amount,
                "effective_at": effective_at,
                "email_type": email_type,
                "expand": expand,
                "lines": lines,
                "memo": memo,
                "metadata": metadata,
                "out_of_band_amount": out_of_band_amount,
                "reason": reason,
                "refund_amount": refund_amount,
                "refunds": refunds,
                "shipping_cost": shipping_cost,
                "invoice": invoice,
            },
            dump_with=params._SerializerCreditNoteCreateBody,
            style={
                "amount": "form",
                "credit_amount": "form",
                "effective_at": "form",
                "email_type": "form",
                "expand": "deepObject",
                "invoice": "form",
                "lines": "deepObject",
                "memo": "form",
                "metadata": "deepObject",
                "out_of_band_amount": "form",
                "reason": "form",
                "refund_amount": "form",
                "refunds": "deepObject",
                "shipping_cost": "deepObject",
            },
            explode={
                "amount": True,
                "credit_amount": True,
                "effective_at": True,
                "email_type": True,
                "expand": True,
                "invoice": True,
                "lines": True,
                "memo": True,
                "metadata": True,
                "out_of_band_amount": True,
                "reason": True,
                "refund_amount": True,
                "refunds": True,
                "shipping_cost": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/credit_notes",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.CreditNoteUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Update a credit note

        <p>Updates an existing credit note.</p>

        POST /v1/credit_notes/{id}

        Args:
            data: CreditNoteUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.update(id="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCreditNoteUpdateBody,
                style={
                    "expand": "deepObject",
                    "memo": "form",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "memo": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/credit_notes/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    def void(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.CreditNoteVoidBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Void a credit note

        <p>Marks a credit note as void. Learn more about <a href="/docs/billing/invoices/credit-notes#voiding">voiding credit notes</a>.</p>

        POST /v1/credit_notes/{id}/void

        Args:
            data: CreditNoteVoidBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_note.void(id="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCreditNoteVoidBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/credit_notes/{id}/void",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )


class AsyncCreditNoteClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CreditNoteListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNoteListResponse:
        """
        List all credit notes

        <p>Returns a list of credit notes.</p>

        GET /v1/credit_notes

        Args:
            created: Only return credit notes that were created during the given date interval.
            customer: Only return credit notes for the customer specified by this customer ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            invoice: Only return credit notes for the invoice specified by this invoice ID.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.list()
        ```
        """
        models.CreditNoteListResponse.model_rebuild(
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
                        params._SerializerCreditNoteListCreatedObj0, int
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
            path="/v1/credit_notes",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNoteListResponse,
            request_options=request_options or default_request_options(),
        )

    async def preview_1(
        self,
        *,
        invoice: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_type: typing.Union[
            typing.Optional[typing_extensions.Literal["credit_note", "none"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lines: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreview1LinesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        memo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.CreditNotePreview1Metadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        out_of_band_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        refund_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refunds: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreview1RefundsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.CreditNotePreview1ShippingCost], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Preview a credit note

        <p>Get a preview of a credit note without creating it.</p>

        GET /v1/credit_notes/preview

        Args:
            amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
            credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
            effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
            email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
            expand: Specifies which fields in the response should be expanded.
            lines: Line items that make up the credit note.
            memo: The credit note's memo appears on the credit note PDF.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
            reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
            refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
            refunds: Refunds to link to this credit note.
            shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
            invoice: ID of the invoice.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.preview_1(invoice="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "invoice",
            to_encodable(item=invoice, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "amount",
                to_encodable(item=amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(credit_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "credit_amount",
                to_encodable(item=credit_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(effective_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "effective_at",
                to_encodable(item=effective_at, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(email_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email_type",
                to_encodable(
                    item=email_type,
                    dump_with=typing_extensions.Literal["credit_note", "none"],
                ),
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
        if not isinstance(lines, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lines",
                to_encodable(
                    item=lines,
                    dump_with=typing.List[
                        params._SerializerCreditNotePreview1LinesItem
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(memo, type_utils.NotGiven):
            encode_query_param(
                _query,
                "memo",
                to_encodable(item=memo, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "metadata",
                to_encodable(
                    item=metadata,
                    dump_with=params._SerializerCreditNotePreview1Metadata,
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(out_of_band_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "out_of_band_amount",
                to_encodable(item=out_of_band_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(reason, type_utils.NotGiven):
            encode_query_param(
                _query,
                "reason",
                to_encodable(
                    item=reason,
                    dump_with=typing_extensions.Literal[
                        "duplicate",
                        "fraudulent",
                        "order_change",
                        "product_unsatisfactory",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(refund_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refund_amount",
                to_encodable(item=refund_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(refunds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refunds",
                to_encodable(
                    item=refunds,
                    dump_with=typing.List[
                        params._SerializerCreditNotePreview1RefundsItem
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(shipping_cost, type_utils.NotGiven):
            encode_query_param(
                _query,
                "shipping_cost",
                to_encodable(
                    item=shipping_cost,
                    dump_with=params._SerializerCreditNotePreview1ShippingCost,
                ),
                style="deepObject",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/credit_notes/preview",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    async def preview(
        self,
        *,
        invoice: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_type: typing.Union[
            typing.Optional[typing_extensions.Literal["credit_note", "none"]],
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
        lines: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreviewLinesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        memo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.CreditNotePreviewMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        out_of_band_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        refund_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refunds: typing.Union[
            typing.Optional[typing.List[params.CreditNotePreviewRefundsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.CreditNotePreviewShippingCost], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNotePreviewResponse:
        """
        Retrieve a credit note preview's line items

        <p>When retrieving a credit note preview, you’ll get a <strong>lines</strong> property containing the first handful of those items. This URL you can retrieve the full (paginated) list of line items.</p>

        GET /v1/credit_notes/preview/lines

        Args:
            amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
            credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
            effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
            email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lines: Line items that make up the credit note.
            memo: The credit note's memo appears on the credit note PDF.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
            reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
            refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
            refunds: Refunds to link to this credit note.
            shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            invoice: ID of the invoice.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.preview(invoice="string")
        ```
        """
        models.CreditNotePreviewResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "invoice",
            to_encodable(item=invoice, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "amount",
                to_encodable(item=amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(credit_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "credit_amount",
                to_encodable(item=credit_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(effective_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "effective_at",
                to_encodable(item=effective_at, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(email_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email_type",
                to_encodable(
                    item=email_type,
                    dump_with=typing_extensions.Literal["credit_note", "none"],
                ),
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
        if not isinstance(lines, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lines",
                to_encodable(
                    item=lines,
                    dump_with=typing.List[params._SerializerCreditNotePreviewLinesItem],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(memo, type_utils.NotGiven):
            encode_query_param(
                _query,
                "memo",
                to_encodable(item=memo, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "metadata",
                to_encodable(
                    item=metadata, dump_with=params._SerializerCreditNotePreviewMetadata
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(out_of_band_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "out_of_band_amount",
                to_encodable(item=out_of_band_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(reason, type_utils.NotGiven):
            encode_query_param(
                _query,
                "reason",
                to_encodable(
                    item=reason,
                    dump_with=typing_extensions.Literal[
                        "duplicate",
                        "fraudulent",
                        "order_change",
                        "product_unsatisfactory",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(refund_amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refund_amount",
                to_encodable(item=refund_amount, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(refunds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "refunds",
                to_encodable(
                    item=refunds,
                    dump_with=typing.List[
                        params._SerializerCreditNotePreviewRefundsItem
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(shipping_cost, type_utils.NotGiven):
            encode_query_param(
                _query,
                "shipping_cost",
                to_encodable(
                    item=shipping_cost,
                    dump_with=params._SerializerCreditNotePreviewShippingCost,
                ),
                style="deepObject",
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
            path="/v1/credit_notes/preview/lines",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNotePreviewResponse,
            request_options=request_options or default_request_options(),
        )

    async def lines(
        self,
        *,
        credit_note: str,
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
    ) -> models.CreditNoteLinesResponse:
        """
        Retrieve a credit note's line items

        <p>When retrieving a credit note, you’ll get a <strong>lines</strong> property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.</p>

        GET /v1/credit_notes/{credit_note}/lines

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            credit_note: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.lines(credit_note="string")
        ```
        """
        models.CreditNoteLinesResponse.model_rebuild(
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
            path=f"/v1/credit_notes/{credit_note}/lines",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNoteLinesResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Retrieve a credit note

        <p>Retrieves the credit note object with the given identifier.</p>

        GET /v1/credit_notes/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.get(id="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/credit_notes/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        invoice: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        email_type: typing.Union[
            typing.Optional[typing_extensions.Literal["credit_note", "none"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lines: typing.Union[
            typing.Optional[typing.List[params.CreditNoteCreateBodyLinesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        memo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.CreditNoteCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        out_of_band_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        refund_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refunds: typing.Union[
            typing.Optional[typing.List[params.CreditNoteCreateBodyRefundsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.CreditNoteCreateBodyShippingCost],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Create a credit note

        <p>Issue a credit note to adjust the amount of a finalized invoice. For a <code>status=open</code> invoice, a credit note reduces
        its <code>amount_due</code>. For a <code>status=paid</code> invoice, a credit note does not affect its <code>amount_due</code>. Instead, it can result
        in any combination of the following:</p>

        <ul>
        <li>Refund: create a new refund (using <code>refund_amount</code>) or link an existing refund (using <code>refund</code>).</li>
        <li>Customer balance credit: credit the customer’s balance (using <code>credit_amount</code>) which will be automatically applied to their next invoice when it’s finalized.</li>
        <li>Outside of Stripe credit: record the amount that is or will be credited outside of Stripe (using <code>out_of_band_amount</code>).</li>
        </ul>

        <p>For post-payment credit notes the sum of the refund, credit and outside of Stripe amounts must equal the credit note total.</p>

        <p>You may issue multiple credit notes for an invoice. Each credit note will increment the invoice’s <code>pre_payment_credit_notes_amount</code>
        or <code>post_payment_credit_notes_amount</code> depending on its <code>status</code> at the time of credit note creation.</p>

        POST /v1/credit_notes

        Args:
            amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
            credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
            effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
            email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
            expand: Specifies which fields in the response should be expanded.
            lines: Line items that make up the credit note.
            memo: The credit note's memo appears on the credit note PDF.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
            reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
            refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
            refunds: Refunds to link to this credit note.
            shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
            invoice: ID of the invoice.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.create(invoice="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "credit_amount": credit_amount,
                "effective_at": effective_at,
                "email_type": email_type,
                "expand": expand,
                "lines": lines,
                "memo": memo,
                "metadata": metadata,
                "out_of_band_amount": out_of_band_amount,
                "reason": reason,
                "refund_amount": refund_amount,
                "refunds": refunds,
                "shipping_cost": shipping_cost,
                "invoice": invoice,
            },
            dump_with=params._SerializerCreditNoteCreateBody,
            style={
                "amount": "form",
                "credit_amount": "form",
                "effective_at": "form",
                "email_type": "form",
                "expand": "deepObject",
                "invoice": "form",
                "lines": "deepObject",
                "memo": "form",
                "metadata": "deepObject",
                "out_of_band_amount": "form",
                "reason": "form",
                "refund_amount": "form",
                "refunds": "deepObject",
                "shipping_cost": "deepObject",
            },
            explode={
                "amount": True,
                "credit_amount": True,
                "effective_at": True,
                "email_type": True,
                "expand": True,
                "invoice": True,
                "lines": True,
                "memo": True,
                "metadata": True,
                "out_of_band_amount": True,
                "reason": True,
                "refund_amount": True,
                "refunds": True,
                "shipping_cost": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/credit_notes",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.CreditNoteUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Update a credit note

        <p>Updates an existing credit note.</p>

        POST /v1/credit_notes/{id}

        Args:
            data: CreditNoteUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.update(id="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCreditNoteUpdateBody,
                style={
                    "expand": "deepObject",
                    "memo": "form",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "memo": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/credit_notes/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )

    async def void(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.CreditNoteVoidBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNote:
        """
        Void a credit note

        <p>Marks a credit note as void. Learn more about <a href="/docs/billing/invoices/credit-notes#voiding">voiding credit notes</a>.</p>

        POST /v1/credit_notes/{id}/void

        Args:
            data: CreditNoteVoidBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_note.void(id="string")
        ```
        """
        models.CreditNote.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCreditNoteVoidBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/credit_notes/{id}/void",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CreditNote,
            request_options=request_options or default_request_options(),
        )
