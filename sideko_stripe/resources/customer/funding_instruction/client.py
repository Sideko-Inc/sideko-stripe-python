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


class FundingInstructionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        bank_transfer: params.CustomerFundingInstructionCreateBodyBankTransfer,
        currency: str,
        customer: str,
        funding_type: typing_extensions.Literal["bank_transfer"],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FundingInstructions:
        """
        Create or retrieve funding instructions for a customer cash balance

        <p>Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.</p>

        POST /v1/customers/{customer}/funding_instructions

        Args:
            expand: Specifies which fields in the response should be expanded.
            bank_transfer: Additional parameters for `bank_transfer` funding types
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            customer: str
            funding_type: The `funding_type` to get the instructions for.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.funding_instruction.create(
            bank_transfer={"type_": "eu_bank_transfer"},
            currency="string",
            customer="string",
            funding_type="bank_transfer",
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "bank_transfer": bank_transfer,
                "currency": currency,
                "funding_type": funding_type,
            },
            dump_with=params._SerializerCustomerFundingInstructionCreateBody,
            style={
                "bank_transfer": "deepObject",
                "currency": "form",
                "expand": "deepObject",
                "funding_type": "form",
            },
            explode={
                "bank_transfer": True,
                "currency": True,
                "expand": True,
                "funding_type": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/funding_instructions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FundingInstructions,
            request_options=request_options or default_request_options(),
        )


class AsyncFundingInstructionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        bank_transfer: params.CustomerFundingInstructionCreateBodyBankTransfer,
        currency: str,
        customer: str,
        funding_type: typing_extensions.Literal["bank_transfer"],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FundingInstructions:
        """
        Create or retrieve funding instructions for a customer cash balance

        <p>Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.</p>

        POST /v1/customers/{customer}/funding_instructions

        Args:
            expand: Specifies which fields in the response should be expanded.
            bank_transfer: Additional parameters for `bank_transfer` funding types
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            customer: str
            funding_type: The `funding_type` to get the instructions for.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.funding_instruction.create(
            bank_transfer={"type_": "eu_bank_transfer"},
            currency="string",
            customer="string",
            funding_type="bank_transfer",
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "bank_transfer": bank_transfer,
                "currency": currency,
                "funding_type": funding_type,
            },
            dump_with=params._SerializerCustomerFundingInstructionCreateBody,
            style={
                "bank_transfer": "deepObject",
                "currency": "form",
                "expand": "deepObject",
                "funding_type": "form",
            },
            explode={
                "bank_transfer": True,
                "currency": True,
                "expand": True,
                "funding_type": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/funding_instructions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FundingInstructions,
            request_options=request_options or default_request_options(),
        )
