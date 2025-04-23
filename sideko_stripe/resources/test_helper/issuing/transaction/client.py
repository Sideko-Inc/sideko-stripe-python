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


class TransactionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create_force_capture(
        self,
        *,
        amount: int,
        card: str,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateForceCaptureBodyMerchantData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        purchase_details: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Create a test-mode force capture

        <p>Allows the user to capture an arbitrary amount, also known as a forced capture.</p>

        POST /v1/test_helpers/issuing/transactions/create_force_capture

        Args:
            currency: The currency of the capture. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            expand: Specifies which fields in the response should be expanded.
            merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
            purchase_details: Additional purchase information that is optionally provided by the merchant.
            amount: The total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            card: Card associated with this transaction.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.transaction.create_force_capture(
            amount=123, card="string"
        )
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "currency": currency,
                "expand": expand,
                "merchant_data": merchant_data,
                "purchase_details": purchase_details,
                "amount": amount,
                "card": card,
            },
            dump_with=params._SerializerTestHelperIssuingTransactionCreateForceCaptureBody,
            style={
                "amount": "form",
                "card": "form",
                "currency": "form",
                "expand": "deepObject",
                "merchant_data": "deepObject",
                "purchase_details": "deepObject",
            },
            explode={
                "amount": True,
                "card": True,
                "currency": True,
                "expand": True,
                "merchant_data": True,
                "purchase_details": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/transactions/create_force_capture",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )

    def create_unlinked_refund(
        self,
        *,
        amount: int,
        card: str,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateUnlinkedRefundBodyMerchantData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        purchase_details: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Create a test-mode unlinked refund

        <p>Allows the user to refund an arbitrary amount, also known as a unlinked refund.</p>

        POST /v1/test_helpers/issuing/transactions/create_unlinked_refund

        Args:
            currency: The currency of the unlinked refund. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            expand: Specifies which fields in the response should be expanded.
            merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
            purchase_details: Additional purchase information that is optionally provided by the merchant.
            amount: The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            card: Card associated with this unlinked refund transaction.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.transaction.create_unlinked_refund(
            amount=123, card="string"
        )
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "currency": currency,
                "expand": expand,
                "merchant_data": merchant_data,
                "purchase_details": purchase_details,
                "amount": amount,
                "card": card,
            },
            dump_with=params._SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBody,
            style={
                "amount": "form",
                "card": "form",
                "currency": "form",
                "expand": "deepObject",
                "merchant_data": "deepObject",
                "purchase_details": "deepObject",
            },
            explode={
                "amount": True,
                "card": True,
                "currency": True,
                "expand": True,
                "merchant_data": True,
                "purchase_details": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/transactions/create_unlinked_refund",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )

    def refund(
        self,
        *,
        transaction: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingTransactionRefundBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Refund a test-mode transaction

        <p>Refund a test-mode Transaction.</p>

        POST /v1/test_helpers/issuing/transactions/{transaction}/refund

        Args:
            data: TestHelperIssuingTransactionRefundBody
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.transaction.refund(transaction="string")
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingTransactionRefundBody,
                style={"expand": "deepObject", "refund_amount": "form"},
                explode={"expand": True, "refund_amount": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/transactions/{transaction}/refund",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )


class AsyncTransactionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create_force_capture(
        self,
        *,
        amount: int,
        card: str,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateForceCaptureBodyMerchantData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        purchase_details: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Create a test-mode force capture

        <p>Allows the user to capture an arbitrary amount, also known as a forced capture.</p>

        POST /v1/test_helpers/issuing/transactions/create_force_capture

        Args:
            currency: The currency of the capture. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            expand: Specifies which fields in the response should be expanded.
            merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
            purchase_details: Additional purchase information that is optionally provided by the merchant.
            amount: The total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            card: Card associated with this transaction.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.transaction.create_force_capture(
            amount=123, card="string"
        )
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "currency": currency,
                "expand": expand,
                "merchant_data": merchant_data,
                "purchase_details": purchase_details,
                "amount": amount,
                "card": card,
            },
            dump_with=params._SerializerTestHelperIssuingTransactionCreateForceCaptureBody,
            style={
                "amount": "form",
                "card": "form",
                "currency": "form",
                "expand": "deepObject",
                "merchant_data": "deepObject",
                "purchase_details": "deepObject",
            },
            explode={
                "amount": True,
                "card": True,
                "currency": True,
                "expand": True,
                "merchant_data": True,
                "purchase_details": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/transactions/create_force_capture",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )

    async def create_unlinked_refund(
        self,
        *,
        amount: int,
        card: str,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateUnlinkedRefundBodyMerchantData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        purchase_details: typing.Union[
            typing.Optional[
                params.TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Create a test-mode unlinked refund

        <p>Allows the user to refund an arbitrary amount, also known as a unlinked refund.</p>

        POST /v1/test_helpers/issuing/transactions/create_unlinked_refund

        Args:
            currency: The currency of the unlinked refund. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            expand: Specifies which fields in the response should be expanded.
            merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
            purchase_details: Additional purchase information that is optionally provided by the merchant.
            amount: The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            card: Card associated with this unlinked refund transaction.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.transaction.create_unlinked_refund(
            amount=123, card="string"
        )
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "currency": currency,
                "expand": expand,
                "merchant_data": merchant_data,
                "purchase_details": purchase_details,
                "amount": amount,
                "card": card,
            },
            dump_with=params._SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBody,
            style={
                "amount": "form",
                "card": "form",
                "currency": "form",
                "expand": "deepObject",
                "merchant_data": "deepObject",
                "purchase_details": "deepObject",
            },
            explode={
                "amount": True,
                "card": True,
                "currency": True,
                "expand": True,
                "merchant_data": True,
                "purchase_details": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/transactions/create_unlinked_refund",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )

    async def refund(
        self,
        *,
        transaction: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingTransactionRefundBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Refund a test-mode transaction

        <p>Refund a test-mode Transaction.</p>

        POST /v1/test_helpers/issuing/transactions/{transaction}/refund

        Args:
            data: TestHelperIssuingTransactionRefundBody
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.transaction.refund(transaction="string")
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingTransactionRefundBody,
                style={"expand": "deepObject", "refund_amount": "form"},
                explode={"expand": True, "refund_amount": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/transactions/{transaction}/refund",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )
