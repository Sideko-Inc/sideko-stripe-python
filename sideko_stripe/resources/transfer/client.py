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


class TransferClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.TransferListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        destination: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferListResponse:
        """
        List all transfers

        <p>Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.</p>

        GET /v1/transfers

        Args:
            created: Only return transfers that were created during the given date interval.
            destination: Only return transfers for the destination specified by this account ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transfer_group: Only return transfers with the specified transfer group.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.transfer.list()
        ```
        """
        models.TransferListResponse.model_rebuild(
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
                        params._SerializerTransferListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(destination, type_utils.NotGiven):
            encode_query_param(
                _query,
                "destination",
                to_encodable(item=destination, dump_with=str),
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
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(transfer_group, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transfer_group",
                to_encodable(item=transfer_group, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/transfers",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TransferListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        transfer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transfer:
        """
        Retrieve a transfer

        <p>Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.</p>

        GET /v1/transfers/{transfer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.transfer.get(transfer="string")
        ```
        """
        models.Transfer.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/transfers/{transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Transfer,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        currency: str,
        destination: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TransferCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_type: typing.Union[
            typing.Optional[typing_extensions.Literal["bank_account", "card", "fpx"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transfer:
        """
        Create a transfer

        <p>To send funds from your Stripe account to a connected account, you create a new transfer object. Your <a href="#balance">Stripe balance</a> must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.</p>

        POST /v1/transfers

        Args:
            amount: A positive integer in cents (or local equivalent) representing how much to transfer.
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            source_transaction: You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-availability) for details.
            source_type: The source balance to use for this transfer. One of `bank_account`, `card`, or `fpx`. For most users, this will default to `card`.
            transfer_group: A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
            currency: Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies).
            destination: The ID of a connected Stripe account. <a href="/docs/connect/separate-charges-and-transfers">See the Connect documentation</a> for details.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.transfer.create(currency="string", destination="string")
        ```
        """
        models.Transfer.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "source_transaction": source_transaction,
                "source_type": source_type,
                "transfer_group": transfer_group,
                "currency": currency,
                "destination": destination,
            },
            dump_with=params._SerializerTransferCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "destination": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "source_transaction": "form",
                "source_type": "form",
                "transfer_group": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "destination": True,
                "expand": True,
                "metadata": True,
                "source_transaction": True,
                "source_type": True,
                "transfer_group": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/transfers",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Transfer,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        transfer: str,
        data: typing.Union[
            typing.Optional[params.TransferUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transfer:
        """
        Update a transfer

        <p>Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request accepts only metadata as an argument.</p>

        POST /v1/transfers/{transfer}

        Args:
            data: TransferUpdateBody
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.transfer.update(transfer="string")
        ```
        """
        models.Transfer.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTransferUpdateBody,
                style={
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"description": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/transfers/{transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Transfer,
            request_options=request_options or default_request_options(),
        )


class AsyncTransferClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.TransferListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        destination: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferListResponse:
        """
        List all transfers

        <p>Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.</p>

        GET /v1/transfers

        Args:
            created: Only return transfers that were created during the given date interval.
            destination: Only return transfers for the destination specified by this account ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transfer_group: Only return transfers with the specified transfer group.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.transfer.list()
        ```
        """
        models.TransferListResponse.model_rebuild(
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
                        params._SerializerTransferListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(destination, type_utils.NotGiven):
            encode_query_param(
                _query,
                "destination",
                to_encodable(item=destination, dump_with=str),
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
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(transfer_group, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transfer_group",
                to_encodable(item=transfer_group, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/transfers",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TransferListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        transfer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transfer:
        """
        Retrieve a transfer

        <p>Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.</p>

        GET /v1/transfers/{transfer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.transfer.get(transfer="string")
        ```
        """
        models.Transfer.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/transfers/{transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Transfer,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        currency: str,
        destination: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TransferCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_type: typing.Union[
            typing.Optional[typing_extensions.Literal["bank_account", "card", "fpx"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transfer:
        """
        Create a transfer

        <p>To send funds from your Stripe account to a connected account, you create a new transfer object. Your <a href="#balance">Stripe balance</a> must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.</p>

        POST /v1/transfers

        Args:
            amount: A positive integer in cents (or local equivalent) representing how much to transfer.
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            source_transaction: You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-availability) for details.
            source_type: The source balance to use for this transfer. One of `bank_account`, `card`, or `fpx`. For most users, this will default to `card`.
            transfer_group: A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
            currency: Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies).
            destination: The ID of a connected Stripe account. <a href="/docs/connect/separate-charges-and-transfers">See the Connect documentation</a> for details.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.transfer.create(currency="string", destination="string")
        ```
        """
        models.Transfer.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "source_transaction": source_transaction,
                "source_type": source_type,
                "transfer_group": transfer_group,
                "currency": currency,
                "destination": destination,
            },
            dump_with=params._SerializerTransferCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "destination": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "source_transaction": "form",
                "source_type": "form",
                "transfer_group": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "destination": True,
                "expand": True,
                "metadata": True,
                "source_transaction": True,
                "source_type": True,
                "transfer_group": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/transfers",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Transfer,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        transfer: str,
        data: typing.Union[
            typing.Optional[params.TransferUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transfer:
        """
        Update a transfer

        <p>Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request accepts only metadata as an argument.</p>

        POST /v1/transfers/{transfer}

        Args:
            data: TransferUpdateBody
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.transfer.update(transfer="string")
        ```
        """
        models.Transfer.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTransferUpdateBody,
                style={
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"description": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/transfers/{transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Transfer,
            request_options=request_options or default_request_options(),
        )
