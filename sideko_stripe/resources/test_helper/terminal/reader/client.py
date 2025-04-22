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


class ReaderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def present_payment_method(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTerminalReaderPresentPaymentMethodBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Simulate presenting a payment method

        <p>Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.</p>

        POST /v1/test_helpers/terminal/readers/{reader}/present_payment_method

        Args:
            data: TestHelperTerminalReaderPresentPaymentMethodBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.terminal.reader.present_payment_method(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTerminalReaderPresentPaymentMethodBody,
                style={
                    "amount_tip": "form",
                    "card_present": "deepObject",
                    "expand": "deepObject",
                    "interac_present": "deepObject",
                    "type": "form",
                },
                explode={
                    "amount_tip": True,
                    "card_present": True,
                    "expand": True,
                    "interac_present": True,
                    "type": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/terminal/readers/{reader}/present_payment_method",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )


class AsyncReaderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def present_payment_method(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTerminalReaderPresentPaymentMethodBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Simulate presenting a payment method

        <p>Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.</p>

        POST /v1/test_helpers/terminal/readers/{reader}/present_payment_method

        Args:
            data: TestHelperTerminalReaderPresentPaymentMethodBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.terminal.reader.present_payment_method(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTerminalReaderPresentPaymentMethodBody,
                style={
                    "amount_tip": "form",
                    "card_present": "deepObject",
                    "expand": "deepObject",
                    "interac_present": "deepObject",
                    "type": "form",
                },
                explode={
                    "amount_tip": True,
                    "card_present": True,
                    "expand": True,
                    "interac_present": True,
                    "type": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/terminal/readers/{reader}/present_payment_method",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )
