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


class ReaderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, reader: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedTerminalReader:
        """
        Delete a Reader

        <p>Deletes a <code>Reader</code> object.</p>

        DELETE /v1/terminal/readers/{reader}

        Args:
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.delete(reader="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/terminal/readers/{reader}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTerminalReader,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        device_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "bbpos_chipper2x",
                    "bbpos_wisepad3",
                    "bbpos_wisepos_e",
                    "mobile_phone_reader",
                    "simulated_wisepos_e",
                    "stripe_m2",
                    "stripe_s700",
                    "verifone_P400",
                ]
            ],
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
        location: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        serial_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["offline", "online"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReaderListResponse:
        """
        List all Readers

        <p>Returns a list of <code>Reader</code> objects.</p>

        GET /v1/terminal/readers

        Args:
            device_type: Filters readers by device type
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            location: A location ID to filter the response list to only readers at the specific location
            serial_number: Filters readers by serial number
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: A status filter to filter readers to only offline or online readers
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.list()
        ```
        """
        models.TerminalReaderListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(device_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "device_type",
                to_encodable(
                    item=device_type,
                    dump_with=typing_extensions.Literal[
                        "bbpos_chipper2x",
                        "bbpos_wisepad3",
                        "bbpos_wisepos_e",
                        "mobile_phone_reader",
                        "simulated_wisepos_e",
                        "stripe_m2",
                        "stripe_s700",
                        "verifone_P400",
                    ],
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
        if not isinstance(location, type_utils.NotGiven):
            encode_query_param(
                _query,
                "location",
                to_encodable(item=location, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(serial_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "serial_number",
                to_encodable(item=serial_number, dump_with=str),
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
                    dump_with=typing_extensions.Literal["offline", "online"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/terminal/readers",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TerminalReaderListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        reader: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalReader, models.DeletedTerminalReader]:
        """
        Retrieve a Reader

        <p>Retrieves a <code>Reader</code> object.</p>

        GET /v1/terminal/readers/{reader}

        Args:
            expand: Specifies which fields in the response should be expanded.
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.get(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/terminal/readers/{reader}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[models.TerminalReader, models.DeletedTerminalReader],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        registration_code: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        label: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        location: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.TerminalReaderCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Create a Reader

        <p>Creates a new <code>Reader</code> object.</p>

        POST /v1/terminal/readers

        Args:
            expand: Specifies which fields in the response should be expanded.
            label: Custom label given to the reader for easier identification. If no label is specified, the registration code will be used.
            location: The location to assign the reader to.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            registration_code: A code generated by the reader used for registering to an account.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.create(registration_code="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "label": label,
                "location": location,
                "metadata": metadata,
                "registration_code": registration_code,
            },
            dump_with=params._SerializerTerminalReaderCreateBody,
            style={
                "expand": "deepObject",
                "label": "form",
                "location": "form",
                "metadata": "deepObject",
                "registration_code": "form",
            },
            explode={
                "expand": True,
                "label": True,
                "location": True,
                "metadata": True,
                "registration_code": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/terminal/readers",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TerminalReaderUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalReader, models.DeletedTerminalReader]:
        """
        Update a Reader

        <p>Updates a <code>Reader</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/terminal/readers/{reader}

        Args:
            data: TerminalReaderUpdateBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.update(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalReaderUpdateBody,
                style={
                    "expand": "deepObject",
                    "label": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "label": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.TerminalReader, models.DeletedTerminalReader],
            request_options=request_options or default_request_options(),
        )

    def cancel_action(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TerminalReaderCancelActionBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Cancel the current reader action

        <p>Cancels the current reader action.</p>

        POST /v1/terminal/readers/{reader}/cancel_action

        Args:
            data: TerminalReaderCancelActionBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.cancel_action(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalReaderCancelActionBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/cancel_action",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    def process_payment_intent(
        self,
        *,
        payment_intent: str,
        reader: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        process_config: typing.Union[
            typing.Optional[params.TerminalReaderProcessPaymentIntentBodyProcessConfig],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Hand-off a PaymentIntent to a Reader

        <p>Initiates a payment flow on a Reader.</p>

        POST /v1/terminal/readers/{reader}/process_payment_intent

        Args:
            expand: Specifies which fields in the response should be expanded.
            process_config: Configuration overrides
            payment_intent: PaymentIntent ID
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.process_payment_intent(
            payment_intent="string", reader="string"
        )
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "process_config": process_config,
                "payment_intent": payment_intent,
            },
            dump_with=params._SerializerTerminalReaderProcessPaymentIntentBody,
            style={
                "expand": "deepObject",
                "payment_intent": "form",
                "process_config": "deepObject",
            },
            explode={"expand": True, "payment_intent": True, "process_config": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/process_payment_intent",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    def process_setup_intent(
        self,
        *,
        allow_redisplay: typing_extensions.Literal["always", "limited", "unspecified"],
        reader: str,
        setup_intent: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        process_config: typing.Union[
            typing.Optional[params.TerminalReaderProcessSetupIntentBodyProcessConfig],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Hand-off a SetupIntent to a Reader

        <p>Initiates a setup intent flow on a Reader.</p>

        POST /v1/terminal/readers/{reader}/process_setup_intent

        Args:
            expand: Specifies which fields in the response should be expanded.
            process_config: Configuration overrides
            allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
            reader: str
            setup_intent: SetupIntent ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.process_setup_intent(
            allow_redisplay="always", reader="string", setup_intent="string"
        )
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "process_config": process_config,
                "allow_redisplay": allow_redisplay,
                "setup_intent": setup_intent,
            },
            dump_with=params._SerializerTerminalReaderProcessSetupIntentBody,
            style={
                "allow_redisplay": "form",
                "expand": "deepObject",
                "process_config": "deepObject",
                "setup_intent": "form",
            },
            explode={
                "allow_redisplay": True,
                "expand": True,
                "process_config": True,
                "setup_intent": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/process_setup_intent",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    def refund_payment(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TerminalReaderRefundPaymentBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Refund a Charge or a PaymentIntent in-person

        <p>Initiates a refund on a Reader</p>

        POST /v1/terminal/readers/{reader}/refund_payment

        Args:
            data: TerminalReaderRefundPaymentBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.refund_payment(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalReaderRefundPaymentBody,
                style={
                    "amount": "form",
                    "charge": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "payment_intent": "form",
                    "refund_application_fee": "form",
                    "refund_payment_config": "deepObject",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "charge": True,
                    "expand": True,
                    "metadata": True,
                    "payment_intent": True,
                    "refund_application_fee": True,
                    "refund_payment_config": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/refund_payment",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    def set_reader_display(
        self,
        *,
        reader: str,
        type_: typing_extensions.Literal["cart"],
        cart: typing.Union[
            typing.Optional[params.TerminalReaderSetReaderDisplayBodyCart],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Set reader display

        <p>Sets reader display to show cart details.</p>

        POST /v1/terminal/readers/{reader}/set_reader_display

        Args:
            cart: Cart
            expand: Specifies which fields in the response should be expanded.
            reader: str
            type: Type
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.reader.set_reader_display(reader="string", type_="cart")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"cart": cart, "expand": expand, "type_": type_},
            dump_with=params._SerializerTerminalReaderSetReaderDisplayBody,
            style={"cart": "deepObject", "expand": "deepObject", "type": "form"},
            explode={"cart": True, "expand": True, "type": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/set_reader_display",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )


class AsyncReaderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, reader: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedTerminalReader:
        """
        Delete a Reader

        <p>Deletes a <code>Reader</code> object.</p>

        DELETE /v1/terminal/readers/{reader}

        Args:
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.delete(reader="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/terminal/readers/{reader}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTerminalReader,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        device_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "bbpos_chipper2x",
                    "bbpos_wisepad3",
                    "bbpos_wisepos_e",
                    "mobile_phone_reader",
                    "simulated_wisepos_e",
                    "stripe_m2",
                    "stripe_s700",
                    "verifone_P400",
                ]
            ],
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
        location: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        serial_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["offline", "online"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReaderListResponse:
        """
        List all Readers

        <p>Returns a list of <code>Reader</code> objects.</p>

        GET /v1/terminal/readers

        Args:
            device_type: Filters readers by device type
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            location: A location ID to filter the response list to only readers at the specific location
            serial_number: Filters readers by serial number
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: A status filter to filter readers to only offline or online readers
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.list()
        ```
        """
        models.TerminalReaderListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(device_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "device_type",
                to_encodable(
                    item=device_type,
                    dump_with=typing_extensions.Literal[
                        "bbpos_chipper2x",
                        "bbpos_wisepad3",
                        "bbpos_wisepos_e",
                        "mobile_phone_reader",
                        "simulated_wisepos_e",
                        "stripe_m2",
                        "stripe_s700",
                        "verifone_P400",
                    ],
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
        if not isinstance(location, type_utils.NotGiven):
            encode_query_param(
                _query,
                "location",
                to_encodable(item=location, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(serial_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "serial_number",
                to_encodable(item=serial_number, dump_with=str),
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
                    dump_with=typing_extensions.Literal["offline", "online"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/terminal/readers",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TerminalReaderListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        reader: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalReader, models.DeletedTerminalReader]:
        """
        Retrieve a Reader

        <p>Retrieves a <code>Reader</code> object.</p>

        GET /v1/terminal/readers/{reader}

        Args:
            expand: Specifies which fields in the response should be expanded.
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.get(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/terminal/readers/{reader}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[models.TerminalReader, models.DeletedTerminalReader],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        registration_code: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        label: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        location: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.TerminalReaderCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Create a Reader

        <p>Creates a new <code>Reader</code> object.</p>

        POST /v1/terminal/readers

        Args:
            expand: Specifies which fields in the response should be expanded.
            label: Custom label given to the reader for easier identification. If no label is specified, the registration code will be used.
            location: The location to assign the reader to.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            registration_code: A code generated by the reader used for registering to an account.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.create(registration_code="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "label": label,
                "location": location,
                "metadata": metadata,
                "registration_code": registration_code,
            },
            dump_with=params._SerializerTerminalReaderCreateBody,
            style={
                "expand": "deepObject",
                "label": "form",
                "location": "form",
                "metadata": "deepObject",
                "registration_code": "form",
            },
            explode={
                "expand": True,
                "label": True,
                "location": True,
                "metadata": True,
                "registration_code": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/terminal/readers",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TerminalReaderUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalReader, models.DeletedTerminalReader]:
        """
        Update a Reader

        <p>Updates a <code>Reader</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/terminal/readers/{reader}

        Args:
            data: TerminalReaderUpdateBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.update(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalReaderUpdateBody,
                style={
                    "expand": "deepObject",
                    "label": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "label": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.TerminalReader, models.DeletedTerminalReader],
            request_options=request_options or default_request_options(),
        )

    async def cancel_action(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TerminalReaderCancelActionBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Cancel the current reader action

        <p>Cancels the current reader action.</p>

        POST /v1/terminal/readers/{reader}/cancel_action

        Args:
            data: TerminalReaderCancelActionBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.cancel_action(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalReaderCancelActionBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/cancel_action",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    async def process_payment_intent(
        self,
        *,
        payment_intent: str,
        reader: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        process_config: typing.Union[
            typing.Optional[params.TerminalReaderProcessPaymentIntentBodyProcessConfig],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Hand-off a PaymentIntent to a Reader

        <p>Initiates a payment flow on a Reader.</p>

        POST /v1/terminal/readers/{reader}/process_payment_intent

        Args:
            expand: Specifies which fields in the response should be expanded.
            process_config: Configuration overrides
            payment_intent: PaymentIntent ID
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.process_payment_intent(
            payment_intent="string", reader="string"
        )
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "process_config": process_config,
                "payment_intent": payment_intent,
            },
            dump_with=params._SerializerTerminalReaderProcessPaymentIntentBody,
            style={
                "expand": "deepObject",
                "payment_intent": "form",
                "process_config": "deepObject",
            },
            explode={"expand": True, "payment_intent": True, "process_config": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/process_payment_intent",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    async def process_setup_intent(
        self,
        *,
        allow_redisplay: typing_extensions.Literal["always", "limited", "unspecified"],
        reader: str,
        setup_intent: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        process_config: typing.Union[
            typing.Optional[params.TerminalReaderProcessSetupIntentBodyProcessConfig],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Hand-off a SetupIntent to a Reader

        <p>Initiates a setup intent flow on a Reader.</p>

        POST /v1/terminal/readers/{reader}/process_setup_intent

        Args:
            expand: Specifies which fields in the response should be expanded.
            process_config: Configuration overrides
            allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
            reader: str
            setup_intent: SetupIntent ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.process_setup_intent(
            allow_redisplay="always", reader="string", setup_intent="string"
        )
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "process_config": process_config,
                "allow_redisplay": allow_redisplay,
                "setup_intent": setup_intent,
            },
            dump_with=params._SerializerTerminalReaderProcessSetupIntentBody,
            style={
                "allow_redisplay": "form",
                "expand": "deepObject",
                "process_config": "deepObject",
                "setup_intent": "form",
            },
            explode={
                "allow_redisplay": True,
                "expand": True,
                "process_config": True,
                "setup_intent": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/process_setup_intent",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    async def refund_payment(
        self,
        *,
        reader: str,
        data: typing.Union[
            typing.Optional[params.TerminalReaderRefundPaymentBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Refund a Charge or a PaymentIntent in-person

        <p>Initiates a refund on a Reader</p>

        POST /v1/terminal/readers/{reader}/refund_payment

        Args:
            data: TerminalReaderRefundPaymentBody
            reader: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.refund_payment(reader="string")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalReaderRefundPaymentBody,
                style={
                    "amount": "form",
                    "charge": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "payment_intent": "form",
                    "refund_application_fee": "form",
                    "refund_payment_config": "deepObject",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "charge": True,
                    "expand": True,
                    "metadata": True,
                    "payment_intent": True,
                    "refund_application_fee": True,
                    "refund_payment_config": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/refund_payment",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )

    async def set_reader_display(
        self,
        *,
        reader: str,
        type_: typing_extensions.Literal["cart"],
        cart: typing.Union[
            typing.Optional[params.TerminalReaderSetReaderDisplayBodyCart],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalReader:
        """
        Set reader display

        <p>Sets reader display to show cart details.</p>

        POST /v1/terminal/readers/{reader}/set_reader_display

        Args:
            cart: Cart
            expand: Specifies which fields in the response should be expanded.
            reader: str
            type: Type
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.reader.set_reader_display(reader="string", type_="cart")
        ```
        """
        models.TerminalReader.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"cart": cart, "expand": expand, "type_": type_},
            dump_with=params._SerializerTerminalReaderSetReaderDisplayBody,
            style={"cart": "deepObject", "expand": "deepObject", "type": "form"},
            explode={"cart": True, "expand": True, "type": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/readers/{reader}/set_reader_display",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalReader,
            request_options=request_options or default_request_options(),
        )
