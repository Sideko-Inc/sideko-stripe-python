import typing
import typing_extensions

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class ReceivedDebitClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        network: typing_extensions.Literal["ach"],
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        initiating_payment_method_details: typing.Union[
            typing.Optional[
                params.TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryReceivedDebit:
        """
        Test mode: Create a ReceivedDebit

        <p>Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.</p>

        POST /v1/test_helpers/treasury/received_debits

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            initiating_payment_method_details: Initiating payment method details for the object.
            amount: Amount (in cents) to be transferred.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            financial_account: The FinancialAccount to pull funds from.
            network: Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.received_debit.create(
            amount=123, currency="string", financial_account="string", network="ach"
        )
        ```
        """
        models.TreasuryReceivedDebit.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "initiating_payment_method_details": initiating_payment_method_details,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
                "network": network,
            },
            dump_with=params._SerializerTestHelperTreasuryReceivedDebitCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "financial_account": "form",
                "initiating_payment_method_details": "deepObject",
                "network": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "financial_account": True,
                "initiating_payment_method_details": True,
                "network": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/test_helpers/treasury/received_debits",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryReceivedDebit,
            request_options=request_options or default_request_options(),
        )


class AsyncReceivedDebitClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        network: typing_extensions.Literal["ach"],
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        initiating_payment_method_details: typing.Union[
            typing.Optional[
                params.TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryReceivedDebit:
        """
        Test mode: Create a ReceivedDebit

        <p>Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.</p>

        POST /v1/test_helpers/treasury/received_debits

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            initiating_payment_method_details: Initiating payment method details for the object.
            amount: Amount (in cents) to be transferred.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            financial_account: The FinancialAccount to pull funds from.
            network: Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.received_debit.create(
            amount=123, currency="string", financial_account="string", network="ach"
        )
        ```
        """
        models.TreasuryReceivedDebit.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "initiating_payment_method_details": initiating_payment_method_details,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
                "network": network,
            },
            dump_with=params._SerializerTestHelperTreasuryReceivedDebitCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "financial_account": "form",
                "initiating_payment_method_details": "deepObject",
                "network": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "financial_account": True,
                "initiating_payment_method_details": True,
                "network": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/test_helpers/treasury/received_debits",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryReceivedDebit,
            request_options=request_options or default_request_options(),
        )
