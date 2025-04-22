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


class CardClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.IssuingCardListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exp_month: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exp_year: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last4: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        personalization_design: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["active", "canceled", "inactive"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["physical", "virtual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardListResponse:
        """
        List all cards

        <p>Returns a list of Issuing <code>Card</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/cards

        Args:
            cardholder: Only return cards belonging to the Cardholder with the provided ID.
            created: Only return cards that were issued during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            exp_month: Only return cards that have the given expiration month.
            exp_year: Only return cards that have the given expiration year.
            expand: Specifies which fields in the response should be expanded.
            last4: Only return cards that have the given last four digits.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            personalization_design: str
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return cards that have the given status. One of `active`, `inactive`, or `canceled`.
            type: Only return cards that have the given type. One of `virtual` or `physical`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.card.list()
        ```
        """
        models.IssuingCardListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(cardholder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cardholder",
                to_encodable(item=cardholder, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerIssuingCardListCreatedObj0, int
                    ],
                ),
                style="deepObject",
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
        if not isinstance(exp_month, type_utils.NotGiven):
            encode_query_param(
                _query,
                "exp_month",
                to_encodable(item=exp_month, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(exp_year, type_utils.NotGiven):
            encode_query_param(
                _query,
                "exp_year",
                to_encodable(item=exp_year, dump_with=int),
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
        if not isinstance(last4, type_utils.NotGiven):
            encode_query_param(
                _query,
                "last4",
                to_encodable(item=last4, dump_with=str),
                style="form",
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
        if not isinstance(personalization_design, type_utils.NotGiven):
            encode_query_param(
                _query,
                "personalization_design",
                to_encodable(item=personalization_design, dump_with=str),
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
                    dump_with=typing_extensions.Literal[
                        "active", "canceled", "inactive"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal["physical", "virtual"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/issuing/cards",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCardListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        card: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Retrieve a card

        <p>Retrieves an Issuing <code>Card</code> object.</p>

        GET /v1/issuing/cards/{card}

        Args:
            expand: Specifies which fields in the response should be expanded.
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.card.get(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/issuing/cards/{card}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        currency: str,
        type_: typing_extensions.Literal["physical", "virtual"],
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        financial_account: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.IssuingCardCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        personalization_design: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pin: typing.Union[
            typing.Optional[params.IssuingCardCreateBodyPin], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        replacement_for: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        replacement_reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal["damaged", "expired", "lost", "stolen"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        second_line: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        shipping: typing.Union[
            typing.Optional[params.IssuingCardCreateBodyShipping], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        spending_controls: typing.Union[
            typing.Optional[params.IssuingCardCreateBodySpendingControls],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Create a card

        <p>Creates an Issuing <code>Card</code> object.</p>

        POST /v1/issuing/cards

        Args:
            cardholder: The [Cardholder](https://stripe.com/docs/api#issuing_cardholder_object) object with which the card will be associated.
            expand: Specifies which fields in the response should be expanded.
            financial_account: str
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            personalization_design: The personalization design object belonging to this card.
            pin: The desired PIN for this card.
            replacement_for: The card this is meant to be a replacement for (if any).
            replacement_reason: If `replacement_for` is specified, this should indicate why that card is being replaced.
            second_line: The second line to print on the card. Max length: 24 characters.
            shipping: The address where the card will be shipped.
            spending_controls: Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
            status: Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
            currency: The currency for the card.
            type: The type of card to issue. Possible values are `physical` or `virtual`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.card.create(currency="string", type_="physical")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "cardholder": cardholder,
                "expand": expand,
                "financial_account": financial_account,
                "metadata": metadata,
                "personalization_design": personalization_design,
                "pin": pin,
                "replacement_for": replacement_for,
                "replacement_reason": replacement_reason,
                "second_line": second_line,
                "shipping": shipping,
                "spending_controls": spending_controls,
                "status": status,
                "currency": currency,
                "type_": type_,
            },
            dump_with=params._SerializerIssuingCardCreateBody,
            style={
                "cardholder": "form",
                "currency": "form",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "personalization_design": "form",
                "pin": "deepObject",
                "replacement_for": "form",
                "replacement_reason": "form",
                "second_line": "deepObject",
                "shipping": "deepObject",
                "spending_controls": "deepObject",
                "status": "form",
                "type": "form",
            },
            explode={
                "cardholder": True,
                "currency": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "personalization_design": True,
                "pin": True,
                "replacement_for": True,
                "replacement_reason": True,
                "second_line": True,
                "shipping": True,
                "spending_controls": True,
                "status": True,
                "type": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/issuing/cards",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.IssuingCardUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Update a card

        <p>Updates the specified Issuing <code>Card</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/cards/{card}

        Args:
            data: IssuingCardUpdateBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.card.update(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingCardUpdateBody,
                style={
                    "cancellation_reason": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "personalization_design": "form",
                    "pin": "deepObject",
                    "shipping": "deepObject",
                    "spending_controls": "deepObject",
                    "status": "form",
                },
                explode={
                    "cancellation_reason": True,
                    "expand": True,
                    "metadata": True,
                    "personalization_design": True,
                    "pin": True,
                    "shipping": True,
                    "spending_controls": True,
                    "status": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/cards/{card}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )


class AsyncCardClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.IssuingCardListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exp_month: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exp_year: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last4: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        personalization_design: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["active", "canceled", "inactive"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["physical", "virtual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardListResponse:
        """
        List all cards

        <p>Returns a list of Issuing <code>Card</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/cards

        Args:
            cardholder: Only return cards belonging to the Cardholder with the provided ID.
            created: Only return cards that were issued during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            exp_month: Only return cards that have the given expiration month.
            exp_year: Only return cards that have the given expiration year.
            expand: Specifies which fields in the response should be expanded.
            last4: Only return cards that have the given last four digits.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            personalization_design: str
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return cards that have the given status. One of `active`, `inactive`, or `canceled`.
            type: Only return cards that have the given type. One of `virtual` or `physical`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.card.list()
        ```
        """
        models.IssuingCardListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(cardholder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cardholder",
                to_encodable(item=cardholder, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerIssuingCardListCreatedObj0, int
                    ],
                ),
                style="deepObject",
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
        if not isinstance(exp_month, type_utils.NotGiven):
            encode_query_param(
                _query,
                "exp_month",
                to_encodable(item=exp_month, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(exp_year, type_utils.NotGiven):
            encode_query_param(
                _query,
                "exp_year",
                to_encodable(item=exp_year, dump_with=int),
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
        if not isinstance(last4, type_utils.NotGiven):
            encode_query_param(
                _query,
                "last4",
                to_encodable(item=last4, dump_with=str),
                style="form",
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
        if not isinstance(personalization_design, type_utils.NotGiven):
            encode_query_param(
                _query,
                "personalization_design",
                to_encodable(item=personalization_design, dump_with=str),
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
                    dump_with=typing_extensions.Literal[
                        "active", "canceled", "inactive"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal["physical", "virtual"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/issuing/cards",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCardListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        card: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Retrieve a card

        <p>Retrieves an Issuing <code>Card</code> object.</p>

        GET /v1/issuing/cards/{card}

        Args:
            expand: Specifies which fields in the response should be expanded.
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.card.get(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/issuing/cards/{card}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        currency: str,
        type_: typing_extensions.Literal["physical", "virtual"],
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        financial_account: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.IssuingCardCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        personalization_design: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pin: typing.Union[
            typing.Optional[params.IssuingCardCreateBodyPin], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        replacement_for: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        replacement_reason: typing.Union[
            typing.Optional[
                typing_extensions.Literal["damaged", "expired", "lost", "stolen"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        second_line: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        shipping: typing.Union[
            typing.Optional[params.IssuingCardCreateBodyShipping], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        spending_controls: typing.Union[
            typing.Optional[params.IssuingCardCreateBodySpendingControls],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Create a card

        <p>Creates an Issuing <code>Card</code> object.</p>

        POST /v1/issuing/cards

        Args:
            cardholder: The [Cardholder](https://stripe.com/docs/api#issuing_cardholder_object) object with which the card will be associated.
            expand: Specifies which fields in the response should be expanded.
            financial_account: str
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            personalization_design: The personalization design object belonging to this card.
            pin: The desired PIN for this card.
            replacement_for: The card this is meant to be a replacement for (if any).
            replacement_reason: If `replacement_for` is specified, this should indicate why that card is being replaced.
            second_line: The second line to print on the card. Max length: 24 characters.
            shipping: The address where the card will be shipped.
            spending_controls: Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
            status: Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
            currency: The currency for the card.
            type: The type of card to issue. Possible values are `physical` or `virtual`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.card.create(currency="string", type_="physical")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "cardholder": cardholder,
                "expand": expand,
                "financial_account": financial_account,
                "metadata": metadata,
                "personalization_design": personalization_design,
                "pin": pin,
                "replacement_for": replacement_for,
                "replacement_reason": replacement_reason,
                "second_line": second_line,
                "shipping": shipping,
                "spending_controls": spending_controls,
                "status": status,
                "currency": currency,
                "type_": type_,
            },
            dump_with=params._SerializerIssuingCardCreateBody,
            style={
                "cardholder": "form",
                "currency": "form",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "personalization_design": "form",
                "pin": "deepObject",
                "replacement_for": "form",
                "replacement_reason": "form",
                "second_line": "deepObject",
                "shipping": "deepObject",
                "spending_controls": "deepObject",
                "status": "form",
                "type": "form",
            },
            explode={
                "cardholder": True,
                "currency": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "personalization_design": True,
                "pin": True,
                "replacement_for": True,
                "replacement_reason": True,
                "second_line": True,
                "shipping": True,
                "spending_controls": True,
                "status": True,
                "type": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/issuing/cards",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.IssuingCardUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Update a card

        <p>Updates the specified Issuing <code>Card</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/cards/{card}

        Args:
            data: IssuingCardUpdateBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.card.update(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingCardUpdateBody,
                style={
                    "cancellation_reason": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "personalization_design": "form",
                    "pin": "deepObject",
                    "shipping": "deepObject",
                    "spending_controls": "deepObject",
                    "status": "form",
                },
                explode={
                    "cancellation_reason": True,
                    "expand": True,
                    "metadata": True,
                    "personalization_design": True,
                    "pin": True,
                    "shipping": True,
                    "spending_controls": True,
                    "status": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/cards/{card}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )
