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


class PayoutClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        arrival_date: typing.Union[
            typing.Optional[typing.Union[params.PayoutListArrivalDateObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PayoutListCreatedObj0, int]],
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
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PayoutListResponse:
        """
        List all payouts

        <p>Returns a list of existing payouts sent to third-party bank accounts or payouts that Stripe sent to you. The payouts return in sorted order, with the most recently created payouts appearing first.</p>

        GET /v1/payouts

        Args:
            arrival_date: Only return payouts that are expected to arrive during the given date interval.
            created: Only return payouts that were created during the given date interval.
            destination: The ID of an external account - only return payouts sent to this external account.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payout.list()
        ```
        """
        models.PayoutListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(arrival_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "arrival_date",
                to_encodable(
                    item=arrival_date,
                    dump_with=typing.Union[
                        params._SerializerPayoutListArrivalDateObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerPayoutListCreatedObj0, int
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/payouts",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PayoutListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        payout: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Retrieve a payout

        <p>Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.</p>

        GET /v1/payouts/{payout}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payout.get(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payouts/{payout}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: int,
        currency: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PayoutCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        method: typing.Union[
            typing.Optional[typing_extensions.Literal["instant", "standard"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        source_type: typing.Union[
            typing.Optional[typing_extensions.Literal["bank_account", "card", "fpx"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Create a payout

        <p>To send funds to your own bank account, create a new payout object. Your <a href="#balance">Stripe balance</a> must cover the payout amount. If it doesn’t, you receive an “Insufficient Funds” error.</p>

        <p>If your API key is in test mode, money won’t actually be sent, though every other action occurs as if you’re in live mode.</p>

        <p>If you create a manual payout on a Stripe account that uses multiple payment source types, you need to specify the source type balance that the payout draws from. The <a href="#balance_object">balance object</a> details available and pending amounts by source type.</p>

        POST /v1/payouts

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            destination: The ID of a bank account or a card to send the payout to. If you don't provide a destination, we use the default external account for the specified currency.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            method: The method used to send this payout, which is `standard` or `instant`. We support `instant` for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).
            source_type: The balance type of your Stripe balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the Balances API. One of `bank_account`, `card`, or `fpx`.
            statement_descriptor: A string that displays on the recipient's bank or card statement (up to 22 characters). A `statement_descriptor` that's longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.
            amount: A positive integer in cents representing how much to payout.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payout.create(amount=123, currency="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "description": description,
                "destination": destination,
                "expand": expand,
                "metadata": metadata,
                "method": method,
                "source_type": source_type,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerPayoutCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "destination": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "method": "form",
                "source_type": "form",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "destination": True,
                "expand": True,
                "metadata": True,
                "method": True,
                "source_type": True,
                "statement_descriptor": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/payouts",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        payout: str,
        data: typing.Union[
            typing.Optional[params.PayoutUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Update a payout

        <p>Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.</p>

        POST /v1/payouts/{payout}

        Args:
            data: PayoutUpdateBody
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payout.update(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPayoutUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payouts/{payout}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        payout: str,
        data: typing.Union[
            typing.Optional[params.PayoutCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Cancel a payout

        <p>You can cancel a previously created payout if its status is <code>pending</code>. Stripe refunds the funds to your available balance. You can’t cancel automatic Stripe payouts.</p>

        POST /v1/payouts/{payout}/cancel

        Args:
            data: PayoutCancelBody
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payout.cancel(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPayoutCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payouts/{payout}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    def reverse(
        self,
        *,
        payout: str,
        data: typing.Union[
            typing.Optional[params.PayoutReverseBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Reverse a payout

        <p>Reverses a payout by debiting the destination bank account. At this time, you can only reverse payouts for connected accounts to US bank accounts. If the payout is manual and in the <code>pending</code> status, use <code>/v1/payouts/:id/cancel</code> instead.</p>

        <p>By requesting a reversal through <code>/v1/payouts/:id/reverse</code>, you confirm that the authorized signatory of the selected bank account authorizes the debit on the bank account and that no other authorization is required.</p>

        POST /v1/payouts/{payout}/reverse

        Args:
            data: PayoutReverseBody
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payout.reverse(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPayoutReverseBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payouts/{payout}/reverse",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )


class AsyncPayoutClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        arrival_date: typing.Union[
            typing.Optional[typing.Union[params.PayoutListArrivalDateObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PayoutListCreatedObj0, int]],
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
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PayoutListResponse:
        """
        List all payouts

        <p>Returns a list of existing payouts sent to third-party bank accounts or payouts that Stripe sent to you. The payouts return in sorted order, with the most recently created payouts appearing first.</p>

        GET /v1/payouts

        Args:
            arrival_date: Only return payouts that are expected to arrive during the given date interval.
            created: Only return payouts that were created during the given date interval.
            destination: The ID of an external account - only return payouts sent to this external account.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payout.list()
        ```
        """
        models.PayoutListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(arrival_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "arrival_date",
                to_encodable(
                    item=arrival_date,
                    dump_with=typing.Union[
                        params._SerializerPayoutListArrivalDateObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerPayoutListCreatedObj0, int
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/payouts",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PayoutListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        payout: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Retrieve a payout

        <p>Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.</p>

        GET /v1/payouts/{payout}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payout.get(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payouts/{payout}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PayoutCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        method: typing.Union[
            typing.Optional[typing_extensions.Literal["instant", "standard"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        source_type: typing.Union[
            typing.Optional[typing_extensions.Literal["bank_account", "card", "fpx"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Create a payout

        <p>To send funds to your own bank account, create a new payout object. Your <a href="#balance">Stripe balance</a> must cover the payout amount. If it doesn’t, you receive an “Insufficient Funds” error.</p>

        <p>If your API key is in test mode, money won’t actually be sent, though every other action occurs as if you’re in live mode.</p>

        <p>If you create a manual payout on a Stripe account that uses multiple payment source types, you need to specify the source type balance that the payout draws from. The <a href="#balance_object">balance object</a> details available and pending amounts by source type.</p>

        POST /v1/payouts

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            destination: The ID of a bank account or a card to send the payout to. If you don't provide a destination, we use the default external account for the specified currency.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            method: The method used to send this payout, which is `standard` or `instant`. We support `instant` for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).
            source_type: The balance type of your Stripe balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the Balances API. One of `bank_account`, `card`, or `fpx`.
            statement_descriptor: A string that displays on the recipient's bank or card statement (up to 22 characters). A `statement_descriptor` that's longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.
            amount: A positive integer in cents representing how much to payout.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payout.create(amount=123, currency="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "description": description,
                "destination": destination,
                "expand": expand,
                "metadata": metadata,
                "method": method,
                "source_type": source_type,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerPayoutCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "destination": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "method": "form",
                "source_type": "form",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "destination": True,
                "expand": True,
                "metadata": True,
                "method": True,
                "source_type": True,
                "statement_descriptor": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/payouts",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        payout: str,
        data: typing.Union[
            typing.Optional[params.PayoutUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Update a payout

        <p>Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.</p>

        POST /v1/payouts/{payout}

        Args:
            data: PayoutUpdateBody
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payout.update(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPayoutUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payouts/{payout}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        payout: str,
        data: typing.Union[
            typing.Optional[params.PayoutCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Cancel a payout

        <p>You can cancel a previously created payout if its status is <code>pending</code>. Stripe refunds the funds to your available balance. You can’t cancel automatic Stripe payouts.</p>

        POST /v1/payouts/{payout}/cancel

        Args:
            data: PayoutCancelBody
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payout.cancel(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPayoutCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payouts/{payout}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )

    async def reverse(
        self,
        *,
        payout: str,
        data: typing.Union[
            typing.Optional[params.PayoutReverseBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payout:
        """
        Reverse a payout

        <p>Reverses a payout by debiting the destination bank account. At this time, you can only reverse payouts for connected accounts to US bank accounts. If the payout is manual and in the <code>pending</code> status, use <code>/v1/payouts/:id/cancel</code> instead.</p>

        <p>By requesting a reversal through <code>/v1/payouts/:id/reverse</code>, you confirm that the authorized signatory of the selected bank account authorizes the debit on the bank account and that no other authorization is required.</p>

        POST /v1/payouts/{payout}/reverse

        Args:
            data: PayoutReverseBody
            payout: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payout.reverse(payout="string")
        ```
        """
        models.Payout.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPayoutReverseBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payouts/{payout}/reverse",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Payout,
            request_options=request_options or default_request_options(),
        )
