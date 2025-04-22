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
from sideko_stripe.resources.tax.transaction.line_items import (
    AsyncLineItemsClient,
    LineItemsClient,
)
from sideko_stripe.types import models, params


class TransactionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.line_items = LineItemsClient(base_client=self._base_client)

    def get(
        self,
        *,
        transaction: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxTransaction:
        """
        Retrieve a transaction

        <p>Retrieves a Tax <code>Transaction</code> object.</p>

        GET /v1/tax/transactions/{transaction}

        Args:
            expand: Specifies which fields in the response should be expanded.
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.transaction.get(transaction="string")
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
            path=f"/v1/tax/transactions/{transaction}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxTransaction,
            request_options=request_options or default_request_options(),
        )

    def create_from_calculation(
        self,
        *,
        calculation: str,
        reference: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TaxTransactionCreateFromCalculationBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        posted_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxTransaction:
        """
        Create a transaction from a calculation

        <p>Creates a Tax Transaction from a calculation, if that calculation hasn’t expired. Calculations expire after 90 days.</p>

        POST /v1/tax/transactions/create_from_calculation

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            posted_at: The Unix timestamp representing when the tax liability is assumed or reduced, which determines the liability posting period and handling in tax liability reports. The timestamp must fall within the `tax_date` and the current time, unless the `tax_date` is scheduled in advance. Defaults to the current time.
            calculation: Tax Calculation ID to be used as input when creating the transaction.
            reference: A custom order or sale identifier, such as 'myOrder_123'. Must be unique across all transactions, including reversals.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.transaction.create_from_calculation(
            calculation="string", reference="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "posted_at": posted_at,
                "calculation": calculation,
                "reference": reference,
            },
            dump_with=params._SerializerTaxTransactionCreateFromCalculationBody,
            style={
                "calculation": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "posted_at": "form",
                "reference": "form",
            },
            explode={
                "calculation": True,
                "expand": True,
                "metadata": True,
                "posted_at": True,
                "reference": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/tax/transactions/create_from_calculation",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxTransaction,
            request_options=request_options or default_request_options(),
        )

    def create_reversal(
        self,
        *,
        mode: typing_extensions.Literal["full", "partial"],
        original_transaction: str,
        reference: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        flat_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        line_items: typing.Union[
            typing.Optional[
                typing.List[params.TaxTransactionCreateReversalBodyLineItemsItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TaxTransactionCreateReversalBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.TaxTransactionCreateReversalBodyShippingCost],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxTransaction:
        """
        Create a reversal transaction

        <p>Partially or fully reverses a previously created <code>Transaction</code>.</p>

        POST /v1/tax/transactions/create_reversal

        Args:
            expand: Specifies which fields in the response should be expanded.
            flat_amount: A flat amount to reverse across the entire transaction, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) in negative. This value represents the total amount to refund from the transaction, including taxes.
            line_items: The line item amounts to reverse.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            shipping_cost: The shipping cost to reverse.
            mode: If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed.
            original_transaction: The ID of the Transaction to partially or fully reverse.
            reference: A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://stripe.com/docs/tax/reports).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.transaction.create_reversal(
            mode="full", original_transaction="string", reference="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "flat_amount": flat_amount,
                "line_items": line_items,
                "metadata": metadata,
                "shipping_cost": shipping_cost,
                "mode": mode,
                "original_transaction": original_transaction,
                "reference": reference,
            },
            dump_with=params._SerializerTaxTransactionCreateReversalBody,
            style={
                "expand": "deepObject",
                "flat_amount": "form",
                "line_items": "deepObject",
                "metadata": "deepObject",
                "mode": "form",
                "original_transaction": "form",
                "reference": "form",
                "shipping_cost": "deepObject",
            },
            explode={
                "expand": True,
                "flat_amount": True,
                "line_items": True,
                "metadata": True,
                "mode": True,
                "original_transaction": True,
                "reference": True,
                "shipping_cost": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/tax/transactions/create_reversal",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxTransaction,
            request_options=request_options or default_request_options(),
        )


class AsyncTransactionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.line_items = AsyncLineItemsClient(base_client=self._base_client)

    async def get(
        self,
        *,
        transaction: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxTransaction:
        """
        Retrieve a transaction

        <p>Retrieves a Tax <code>Transaction</code> object.</p>

        GET /v1/tax/transactions/{transaction}

        Args:
            expand: Specifies which fields in the response should be expanded.
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.transaction.get(transaction="string")
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
            path=f"/v1/tax/transactions/{transaction}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxTransaction,
            request_options=request_options or default_request_options(),
        )

    async def create_from_calculation(
        self,
        *,
        calculation: str,
        reference: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TaxTransactionCreateFromCalculationBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        posted_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxTransaction:
        """
        Create a transaction from a calculation

        <p>Creates a Tax Transaction from a calculation, if that calculation hasn’t expired. Calculations expire after 90 days.</p>

        POST /v1/tax/transactions/create_from_calculation

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            posted_at: The Unix timestamp representing when the tax liability is assumed or reduced, which determines the liability posting period and handling in tax liability reports. The timestamp must fall within the `tax_date` and the current time, unless the `tax_date` is scheduled in advance. Defaults to the current time.
            calculation: Tax Calculation ID to be used as input when creating the transaction.
            reference: A custom order or sale identifier, such as 'myOrder_123'. Must be unique across all transactions, including reversals.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.transaction.create_from_calculation(
            calculation="string", reference="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "posted_at": posted_at,
                "calculation": calculation,
                "reference": reference,
            },
            dump_with=params._SerializerTaxTransactionCreateFromCalculationBody,
            style={
                "calculation": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "posted_at": "form",
                "reference": "form",
            },
            explode={
                "calculation": True,
                "expand": True,
                "metadata": True,
                "posted_at": True,
                "reference": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/tax/transactions/create_from_calculation",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxTransaction,
            request_options=request_options or default_request_options(),
        )

    async def create_reversal(
        self,
        *,
        mode: typing_extensions.Literal["full", "partial"],
        original_transaction: str,
        reference: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        flat_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        line_items: typing.Union[
            typing.Optional[
                typing.List[params.TaxTransactionCreateReversalBodyLineItemsItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TaxTransactionCreateReversalBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.TaxTransactionCreateReversalBodyShippingCost],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxTransaction:
        """
        Create a reversal transaction

        <p>Partially or fully reverses a previously created <code>Transaction</code>.</p>

        POST /v1/tax/transactions/create_reversal

        Args:
            expand: Specifies which fields in the response should be expanded.
            flat_amount: A flat amount to reverse across the entire transaction, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) in negative. This value represents the total amount to refund from the transaction, including taxes.
            line_items: The line item amounts to reverse.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            shipping_cost: The shipping cost to reverse.
            mode: If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed.
            original_transaction: The ID of the Transaction to partially or fully reverse.
            reference: A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://stripe.com/docs/tax/reports).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.transaction.create_reversal(
            mode="full", original_transaction="string", reference="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "flat_amount": flat_amount,
                "line_items": line_items,
                "metadata": metadata,
                "shipping_cost": shipping_cost,
                "mode": mode,
                "original_transaction": original_transaction,
                "reference": reference,
            },
            dump_with=params._SerializerTaxTransactionCreateReversalBody,
            style={
                "expand": "deepObject",
                "flat_amount": "form",
                "line_items": "deepObject",
                "metadata": "deepObject",
                "mode": "form",
                "original_transaction": "form",
                "reference": "form",
                "shipping_cost": "deepObject",
            },
            explode={
                "expand": True,
                "flat_amount": True,
                "line_items": True,
                "metadata": True,
                "mode": True,
                "original_transaction": True,
                "reference": True,
                "shipping_cost": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/tax/transactions/create_reversal",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxTransaction,
            request_options=request_options or default_request_options(),
        )
