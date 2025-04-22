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


class CardholderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.IssuingCardholderListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
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
        phone_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "blocked", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["company", "individual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholderListResponse:
        """
        List all cardholders

        <p>Returns a list of Issuing <code>Cardholder</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/cardholders

        Args:
            created: Only return cardholders that were created during the given date interval.
            email: Only return cardholders that have the given email address.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            phone_number: Only return cardholders that have the given phone number.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return cardholders that have the given status. One of `active`, `inactive`, or `blocked`.
            type: Only return cardholders that have the given type. One of `individual` or `company`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.cardholder.list()
        ```
        """
        models.IssuingCardholderListResponse.model_rebuild(
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
                        params._SerializerIssuingCardholderListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email, dump_with=str),
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
        if not isinstance(phone_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "phone_number",
                to_encodable(item=phone_number, dump_with=str),
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
                        "active", "blocked", "inactive"
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
                    dump_with=typing_extensions.Literal["company", "individual"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/issuing/cardholders",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCardholderListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        cardholder: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholder:
        """
        Retrieve a cardholder

        <p>Retrieves an Issuing <code>Cardholder</code> object.</p>

        GET /v1/issuing/cardholders/{cardholder}

        Args:
            expand: Specifies which fields in the response should be expanded.
            cardholder: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.cardholder.get(cardholder="string")
        ```
        """
        models.IssuingCardholder.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/issuing/cardholders/{cardholder}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCardholder,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        billing: params.IssuingCardholderCreateBodyBilling,
        name: str,
        company: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodyCompany],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        individual: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodyIndividual],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        phone_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        preferred_locales: typing.Union[
            typing.Optional[
                typing.List[typing_extensions.Literal["de", "en", "es", "fr", "it"]]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        spending_controls: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodySpendingControls],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["company", "individual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholder:
        """
        Create a cardholder

        <p>Creates a new Issuing <code>Cardholder</code> object that can be issued cards.</p>

        POST /v1/issuing/cardholders

        Args:
            company: Additional information about a `company` cardholder.
            email: The cardholder's email address.
            expand: Specifies which fields in the response should be expanded.
            individual: Additional information about an `individual` cardholder.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            phone_number: The cardholder's phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details.
            preferred_locales: The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.
         This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder.
            spending_controls: Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
            status: Specifies whether to permit authorizations on this cardholder's cards. Defaults to `active`.
            type: One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details.
            billing: The cardholder's billing address.
            name: The cardholder's name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.cardholder.create(
            billing={
                "address": {
                    "city": "string",
                    "country": "string",
                    "line1": "string",
                    "postal_code": "string",
                }
            },
            name="string",
        )
        ```
        """
        models.IssuingCardholder.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "company": company,
                "email": email,
                "expand": expand,
                "individual": individual,
                "metadata": metadata,
                "phone_number": phone_number,
                "preferred_locales": preferred_locales,
                "spending_controls": spending_controls,
                "status": status,
                "type_": type_,
                "billing": billing,
                "name": name,
            },
            dump_with=params._SerializerIssuingCardholderCreateBody,
            style={
                "billing": "deepObject",
                "company": "deepObject",
                "email": "form",
                "expand": "deepObject",
                "individual": "deepObject",
                "metadata": "deepObject",
                "name": "form",
                "phone_number": "form",
                "preferred_locales": "deepObject",
                "spending_controls": "deepObject",
                "status": "form",
                "type": "form",
            },
            explode={
                "billing": True,
                "company": True,
                "email": True,
                "expand": True,
                "individual": True,
                "metadata": True,
                "name": True,
                "phone_number": True,
                "preferred_locales": True,
                "spending_controls": True,
                "status": True,
                "type": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/issuing/cardholders",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCardholder,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        cardholder: str,
        data: typing.Union[
            typing.Optional[params.IssuingCardholderUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholder:
        """
        Update a cardholder

        <p>Updates the specified Issuing <code>Cardholder</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/cardholders/{cardholder}

        Args:
            data: IssuingCardholderUpdateBody
            cardholder: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.cardholder.update(cardholder="string")
        ```
        """
        models.IssuingCardholder.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingCardholderUpdateBody,
                style={
                    "billing": "deepObject",
                    "company": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "individual": "deepObject",
                    "metadata": "deepObject",
                    "phone_number": "form",
                    "preferred_locales": "deepObject",
                    "spending_controls": "deepObject",
                    "status": "form",
                },
                explode={
                    "billing": True,
                    "company": True,
                    "email": True,
                    "expand": True,
                    "individual": True,
                    "metadata": True,
                    "phone_number": True,
                    "preferred_locales": True,
                    "spending_controls": True,
                    "status": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/cardholders/{cardholder}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCardholder,
            request_options=request_options or default_request_options(),
        )


class AsyncCardholderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.IssuingCardholderListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
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
        phone_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "blocked", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["company", "individual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholderListResponse:
        """
        List all cardholders

        <p>Returns a list of Issuing <code>Cardholder</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/cardholders

        Args:
            created: Only return cardholders that were created during the given date interval.
            email: Only return cardholders that have the given email address.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            phone_number: Only return cardholders that have the given phone number.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return cardholders that have the given status. One of `active`, `inactive`, or `blocked`.
            type: Only return cardholders that have the given type. One of `individual` or `company`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.cardholder.list()
        ```
        """
        models.IssuingCardholderListResponse.model_rebuild(
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
                        params._SerializerIssuingCardholderListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email, dump_with=str),
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
        if not isinstance(phone_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "phone_number",
                to_encodable(item=phone_number, dump_with=str),
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
                        "active", "blocked", "inactive"
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
                    dump_with=typing_extensions.Literal["company", "individual"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/issuing/cardholders",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCardholderListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        cardholder: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholder:
        """
        Retrieve a cardholder

        <p>Retrieves an Issuing <code>Cardholder</code> object.</p>

        GET /v1/issuing/cardholders/{cardholder}

        Args:
            expand: Specifies which fields in the response should be expanded.
            cardholder: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.cardholder.get(cardholder="string")
        ```
        """
        models.IssuingCardholder.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/issuing/cardholders/{cardholder}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingCardholder,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        billing: params.IssuingCardholderCreateBodyBilling,
        name: str,
        company: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodyCompany],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        individual: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodyIndividual],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        phone_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        preferred_locales: typing.Union[
            typing.Optional[
                typing.List[typing_extensions.Literal["de", "en", "es", "fr", "it"]]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        spending_controls: typing.Union[
            typing.Optional[params.IssuingCardholderCreateBodySpendingControls],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["company", "individual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholder:
        """
        Create a cardholder

        <p>Creates a new Issuing <code>Cardholder</code> object that can be issued cards.</p>

        POST /v1/issuing/cardholders

        Args:
            company: Additional information about a `company` cardholder.
            email: The cardholder's email address.
            expand: Specifies which fields in the response should be expanded.
            individual: Additional information about an `individual` cardholder.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            phone_number: The cardholder's phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details.
            preferred_locales: The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.
         This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder.
            spending_controls: Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
            status: Specifies whether to permit authorizations on this cardholder's cards. Defaults to `active`.
            type: One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details.
            billing: The cardholder's billing address.
            name: The cardholder's name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.cardholder.create(
            billing={
                "address": {
                    "city": "string",
                    "country": "string",
                    "line1": "string",
                    "postal_code": "string",
                }
            },
            name="string",
        )
        ```
        """
        models.IssuingCardholder.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "company": company,
                "email": email,
                "expand": expand,
                "individual": individual,
                "metadata": metadata,
                "phone_number": phone_number,
                "preferred_locales": preferred_locales,
                "spending_controls": spending_controls,
                "status": status,
                "type_": type_,
                "billing": billing,
                "name": name,
            },
            dump_with=params._SerializerIssuingCardholderCreateBody,
            style={
                "billing": "deepObject",
                "company": "deepObject",
                "email": "form",
                "expand": "deepObject",
                "individual": "deepObject",
                "metadata": "deepObject",
                "name": "form",
                "phone_number": "form",
                "preferred_locales": "deepObject",
                "spending_controls": "deepObject",
                "status": "form",
                "type": "form",
            },
            explode={
                "billing": True,
                "company": True,
                "email": True,
                "expand": True,
                "individual": True,
                "metadata": True,
                "name": True,
                "phone_number": True,
                "preferred_locales": True,
                "spending_controls": True,
                "status": True,
                "type": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/issuing/cardholders",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCardholder,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        cardholder: str,
        data: typing.Union[
            typing.Optional[params.IssuingCardholderUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCardholder:
        """
        Update a cardholder

        <p>Updates the specified Issuing <code>Cardholder</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/cardholders/{cardholder}

        Args:
            data: IssuingCardholderUpdateBody
            cardholder: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.cardholder.update(cardholder="string")
        ```
        """
        models.IssuingCardholder.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingCardholderUpdateBody,
                style={
                    "billing": "deepObject",
                    "company": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "individual": "deepObject",
                    "metadata": "deepObject",
                    "phone_number": "form",
                    "preferred_locales": "deepObject",
                    "spending_controls": "deepObject",
                    "status": "form",
                },
                explode={
                    "billing": True,
                    "company": True,
                    "email": True,
                    "expand": True,
                    "individual": True,
                    "metadata": True,
                    "phone_number": True,
                    "preferred_locales": True,
                    "spending_controls": True,
                    "status": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/cardholders/{cardholder}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCardholder,
            request_options=request_options or default_request_options(),
        )
