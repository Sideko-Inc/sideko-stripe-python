import typing

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


class RefundClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        charge: str,
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
    ) -> models.ChargeRefundListResponse:
        """
        List all refunds

        <p>You can see a list of the refunds belonging to a specific charge. Note that the 10 most recent refunds are always available by default on the charge object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional refunds.</p>

        GET /v1/charges/{charge}/refunds

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.refund.list(charge="string")
        ```
        """
        models.ChargeRefundListResponse.model_rebuild(
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
            path=f"/v1/charges/{charge}/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ChargeRefundListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        charge: str,
        refund: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        <p>Retrieves the details of an existing refund.</p>

        GET /v1/charges/{charge}/refunds/{refund}

        Args:
            expand: Specifies which fields in the response should be expanded.
            charge: str
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.refund.get(charge="string", refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/charges/{charge}/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeRefundCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Create a refund

        <p>When you create a new refund, you must specify either a Charge or a PaymentIntent object.</p>

        <p>This action refunds a previously created charge that’s not refunded yet.
        Funds are refunded to the credit or debit card that’s originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can repeat this until the entire charge is refunded.</p>

        <p>After you entirely refund a charge, you can’t refund it again.
        This method raises an error when it’s called on an already-refunded charge,
        or when you attempt to refund more money than is left on a charge.</p>

        POST /v1/charges/{charge}/refund

        Args:
            data: ChargeRefundCreateBody
            charge: The identifier of the charge to refund.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.refund.create(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeRefundCreateBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "instructions_email": "form",
                    "metadata": "deepObject",
                    "payment_intent": "form",
                    "reason": "form",
                    "refund_application_fee": "form",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "expand": True,
                    "instructions_email": True,
                    "metadata": True,
                    "payment_intent": True,
                    "reason": True,
                    "refund_application_fee": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/refund",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    def create_1(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeRefundCreate1Body], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Create customer balance refund

        <p>When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.</p>

        <p>Creating a new refund will refund a charge that has previously been created but not yet refunded.
        Funds will be refunded to the credit or debit card that was originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can do so multiple times, until the entire charge has been refunded.</p>

        <p>Once entirely refunded, a charge can’t be refunded again.
        This method will raise an error when called on an already-refunded charge,
        or when trying to refund more money than is left on a charge.</p>

        POST /v1/charges/{charge}/refunds

        Args:
            data: ChargeRefundCreate1Body
            charge: The identifier of the charge to refund.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.refund.create_1(charge="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeRefundCreate1Body,
                style={
                    "amount": "form",
                    "currency": "form",
                    "customer": "form",
                    "expand": "deepObject",
                    "instructions_email": "form",
                    "metadata": "deepObject",
                    "origin": "form",
                    "payment_intent": "form",
                    "reason": "form",
                    "refund_application_fee": "form",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "currency": True,
                    "customer": True,
                    "expand": True,
                    "instructions_email": True,
                    "metadata": True,
                    "origin": True,
                    "payment_intent": True,
                    "reason": True,
                    "refund_application_fee": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        charge: str,
        refund: str,
        data: typing.Union[
            typing.Optional[params.ChargeRefundUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        <p>Update a specified refund.</p>

        POST /v1/charges/{charge}/refunds/{refund}

        Args:
            data: ChargeRefundUpdateBody
            charge: str
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.refund.update(charge="string", refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeRefundUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )


class AsyncRefundClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        charge: str,
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
    ) -> models.ChargeRefundListResponse:
        """
        List all refunds

        <p>You can see a list of the refunds belonging to a specific charge. Note that the 10 most recent refunds are always available by default on the charge object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional refunds.</p>

        GET /v1/charges/{charge}/refunds

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.refund.list(charge="string")
        ```
        """
        models.ChargeRefundListResponse.model_rebuild(
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
            path=f"/v1/charges/{charge}/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ChargeRefundListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        charge: str,
        refund: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        <p>Retrieves the details of an existing refund.</p>

        GET /v1/charges/{charge}/refunds/{refund}

        Args:
            expand: Specifies which fields in the response should be expanded.
            charge: str
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.refund.get(charge="string", refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/charges/{charge}/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeRefundCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Create a refund

        <p>When you create a new refund, you must specify either a Charge or a PaymentIntent object.</p>

        <p>This action refunds a previously created charge that’s not refunded yet.
        Funds are refunded to the credit or debit card that’s originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can repeat this until the entire charge is refunded.</p>

        <p>After you entirely refund a charge, you can’t refund it again.
        This method raises an error when it’s called on an already-refunded charge,
        or when you attempt to refund more money than is left on a charge.</p>

        POST /v1/charges/{charge}/refund

        Args:
            data: ChargeRefundCreateBody
            charge: The identifier of the charge to refund.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.refund.create(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeRefundCreateBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "instructions_email": "form",
                    "metadata": "deepObject",
                    "payment_intent": "form",
                    "reason": "form",
                    "refund_application_fee": "form",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "expand": True,
                    "instructions_email": True,
                    "metadata": True,
                    "payment_intent": True,
                    "reason": True,
                    "refund_application_fee": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/refund",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    async def create_1(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeRefundCreate1Body], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Create customer balance refund

        <p>When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.</p>

        <p>Creating a new refund will refund a charge that has previously been created but not yet refunded.
        Funds will be refunded to the credit or debit card that was originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can do so multiple times, until the entire charge has been refunded.</p>

        <p>Once entirely refunded, a charge can’t be refunded again.
        This method will raise an error when called on an already-refunded charge,
        or when trying to refund more money than is left on a charge.</p>

        POST /v1/charges/{charge}/refunds

        Args:
            data: ChargeRefundCreate1Body
            charge: The identifier of the charge to refund.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.refund.create_1(charge="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeRefundCreate1Body,
                style={
                    "amount": "form",
                    "currency": "form",
                    "customer": "form",
                    "expand": "deepObject",
                    "instructions_email": "form",
                    "metadata": "deepObject",
                    "origin": "form",
                    "payment_intent": "form",
                    "reason": "form",
                    "refund_application_fee": "form",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "currency": True,
                    "customer": True,
                    "expand": True,
                    "instructions_email": True,
                    "metadata": True,
                    "origin": True,
                    "payment_intent": True,
                    "reason": True,
                    "refund_application_fee": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        charge: str,
        refund: str,
        data: typing.Union[
            typing.Optional[params.ChargeRefundUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        <p>Update a specified refund.</p>

        POST /v1/charges/{charge}/refunds/{refund}

        Args:
            data: ChargeRefundUpdateBody
            charge: str
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.refund.update(charge="string", refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeRefundUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )
