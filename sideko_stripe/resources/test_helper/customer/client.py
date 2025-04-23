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


class CustomerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def fund_cash_balance(
        self,
        *,
        amount: int,
        currency: str,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reference: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerCashBalanceTransaction:
        """
        Fund a test mode cash balance

        <p>Create an incoming testmode bank transfer</p>

        POST /v1/test_helpers/customers/{customer}/fund_cash_balance

        Args:
            expand: Specifies which fields in the response should be expanded.
            reference: A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe's [reconciliation algorithm](https://stripe.com/docs/payments/customer-balance/reconciliation) applies to different user inputs.
            amount: Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.customer.fund_cash_balance(
            amount=123, currency="string", customer="string"
        )
        ```
        """
        models.CustomerCashBalanceTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "reference": reference,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerTestHelperCustomerFundCashBalanceBody,
            style={
                "amount": "form",
                "currency": "form",
                "expand": "deepObject",
                "reference": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "expand": True,
                "reference": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/customers/{customer}/fund_cash_balance",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.CustomerCashBalanceTransaction,
            request_options=request_options or default_request_options(),
        )


class AsyncCustomerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def fund_cash_balance(
        self,
        *,
        amount: int,
        currency: str,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reference: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerCashBalanceTransaction:
        """
        Fund a test mode cash balance

        <p>Create an incoming testmode bank transfer</p>

        POST /v1/test_helpers/customers/{customer}/fund_cash_balance

        Args:
            expand: Specifies which fields in the response should be expanded.
            reference: A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe's [reconciliation algorithm](https://stripe.com/docs/payments/customer-balance/reconciliation) applies to different user inputs.
            amount: Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.customer.fund_cash_balance(
            amount=123, currency="string", customer="string"
        )
        ```
        """
        models.CustomerCashBalanceTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "reference": reference,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerTestHelperCustomerFundCashBalanceBody,
            style={
                "amount": "form",
                "currency": "form",
                "expand": "deepObject",
                "reference": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "expand": True,
                "reference": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/customers/{customer}/fund_cash_balance",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.CustomerCashBalanceTransaction,
            request_options=request_options or default_request_options(),
        )
