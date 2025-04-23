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


class SettlementClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        bin: str,
        clearing_date: int,
        currency: str,
        net_total_amount: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interchange_fees_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        network: typing.Union[
            typing.Optional[typing_extensions.Literal["maestro", "visa"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        network_settlement_identifier: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transaction_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transaction_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Create a test-mode settlement

        <p>Allows the user to create an Issuing settlement.</p>

        POST /v1/test_helpers/issuing/settlements

        Args:
            expand: Specifies which fields in the response should be expanded.
            interchange_fees_amount: The total interchange received as reimbursement for the transactions.
            network: The card network for this settlement. One of ["visa", "maestro"]
            network_settlement_identifier: The Settlement Identification Number assigned by the network.
            transaction_amount: The total transaction amount reflected in this settlement.
            transaction_count: The total number of transactions reflected in this settlement.
            bin: The Bank Identification Number reflecting this settlement record.
            clearing_date: The date that the transactions are cleared and posted to user's accounts.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            net_total_amount: The total net amount required to settle with the network.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.settlement.create(
            bin="string", clearing_date=123, currency="string", net_total_amount=123
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "interchange_fees_amount": interchange_fees_amount,
                "network": network,
                "network_settlement_identifier": network_settlement_identifier,
                "transaction_amount": transaction_amount,
                "transaction_count": transaction_count,
                "bin": bin,
                "clearing_date": clearing_date,
                "currency": currency,
                "net_total_amount": net_total_amount,
            },
            dump_with=params._SerializerTestHelperIssuingSettlementCreateBody,
            style={
                "bin": "form",
                "clearing_date": "form",
                "currency": "form",
                "expand": "deepObject",
                "interchange_fees_amount": "form",
                "net_total_amount": "form",
                "network": "form",
                "network_settlement_identifier": "form",
                "transaction_amount": "form",
                "transaction_count": "form",
            },
            explode={
                "bin": True,
                "clearing_date": True,
                "currency": True,
                "expand": True,
                "interchange_fees_amount": True,
                "net_total_amount": True,
                "network": True,
                "network_settlement_identifier": True,
                "transaction_amount": True,
                "transaction_count": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/settlements",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )

    def complete(
        self,
        *,
        settlement: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingSettlementCompleteBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Complete a test-mode settlement

        <p>Allows the user to mark an Issuing settlement as complete.</p>

        POST /v1/test_helpers/issuing/settlements/{settlement}/complete

        Args:
            data: TestHelperIssuingSettlementCompleteBody
            settlement: The settlement token to mark as complete.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.settlement.complete(settlement="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingSettlementCompleteBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/settlements/{settlement}/complete",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )


class AsyncSettlementClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        bin: str,
        clearing_date: int,
        currency: str,
        net_total_amount: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interchange_fees_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        network: typing.Union[
            typing.Optional[typing_extensions.Literal["maestro", "visa"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        network_settlement_identifier: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transaction_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transaction_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Create a test-mode settlement

        <p>Allows the user to create an Issuing settlement.</p>

        POST /v1/test_helpers/issuing/settlements

        Args:
            expand: Specifies which fields in the response should be expanded.
            interchange_fees_amount: The total interchange received as reimbursement for the transactions.
            network: The card network for this settlement. One of ["visa", "maestro"]
            network_settlement_identifier: The Settlement Identification Number assigned by the network.
            transaction_amount: The total transaction amount reflected in this settlement.
            transaction_count: The total number of transactions reflected in this settlement.
            bin: The Bank Identification Number reflecting this settlement record.
            clearing_date: The date that the transactions are cleared and posted to user's accounts.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            net_total_amount: The total net amount required to settle with the network.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.settlement.create(
            bin="string", clearing_date=123, currency="string", net_total_amount=123
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "interchange_fees_amount": interchange_fees_amount,
                "network": network,
                "network_settlement_identifier": network_settlement_identifier,
                "transaction_amount": transaction_amount,
                "transaction_count": transaction_count,
                "bin": bin,
                "clearing_date": clearing_date,
                "currency": currency,
                "net_total_amount": net_total_amount,
            },
            dump_with=params._SerializerTestHelperIssuingSettlementCreateBody,
            style={
                "bin": "form",
                "clearing_date": "form",
                "currency": "form",
                "expand": "deepObject",
                "interchange_fees_amount": "form",
                "net_total_amount": "form",
                "network": "form",
                "network_settlement_identifier": "form",
                "transaction_amount": "form",
                "transaction_count": "form",
            },
            explode={
                "bin": True,
                "clearing_date": True,
                "currency": True,
                "expand": True,
                "interchange_fees_amount": True,
                "net_total_amount": True,
                "network": True,
                "network_settlement_identifier": True,
                "transaction_amount": True,
                "transaction_count": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/settlements",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )

    async def complete(
        self,
        *,
        settlement: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingSettlementCompleteBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Complete a test-mode settlement

        <p>Allows the user to mark an Issuing settlement as complete.</p>

        POST /v1/test_helpers/issuing/settlements/{settlement}/complete

        Args:
            data: TestHelperIssuingSettlementCompleteBody
            settlement: The settlement token to mark as complete.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.settlement.complete(settlement="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingSettlementCompleteBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/settlements/{settlement}/complete",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )
