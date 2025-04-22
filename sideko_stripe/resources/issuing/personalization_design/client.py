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


class PersonalizationDesignClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_keys: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        preferences: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignListPreferences],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["active", "inactive", "rejected", "review"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesignListResponse:
        """
        List all personalization designs

        <p>Returns a list of personalization design objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/personalization_designs

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lookup_keys: Only return personalization designs with the given lookup keys.
            preferences: Only return personalization designs with the given preferences.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return personalization designs with the given status.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.personalization_design.list()
        ```
        """
        models.IssuingPersonalizationDesignListResponse.model_rebuild(
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
        if not isinstance(lookup_keys, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lookup_keys",
                to_encodable(item=lookup_keys, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        if not isinstance(preferences, type_utils.NotGiven):
            encode_query_param(
                _query,
                "preferences",
                to_encodable(
                    item=preferences,
                    dump_with=params._SerializerIssuingPersonalizationDesignListPreferences,
                ),
                style="deepObject",
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
                        "active", "inactive", "rejected", "review"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/issuing/personalization_designs",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingPersonalizationDesignListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        personalization_design: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Retrieve a personalization design

        <p>Retrieves a personalization design object.</p>

        GET /v1/issuing/personalization_designs/{personalization_design}

        Args:
            expand: Specifies which fields in the response should be expanded.
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.personalization_design.get(personalization_design="string")
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/issuing/personalization_designs/{personalization_design}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        physical_bundle: str,
        card_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        carrier_text: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignCreateBodyCarrierText],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        preferences: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignCreateBodyPreferences],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_lookup_key: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Create a personalization design

        <p>Creates a personalization design object.</p>

        POST /v1/issuing/personalization_designs

        Args:
            card_logo: The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.
            carrier_text: Hash containing carrier text, for use with physical bundles that support carrier text.
            expand: Specifies which fields in the response should be expanded.
            lookup_key: A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            name: Friendly display name.
            preferences: Information on whether this personalization design is used to create cards when one is not specified.
            transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design.
            physical_bundle: The physical bundle object belonging to this personalization design.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.personalization_design.create(physical_bundle="string")
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "card_logo": card_logo,
                "carrier_text": carrier_text,
                "expand": expand,
                "lookup_key": lookup_key,
                "metadata": metadata,
                "name": name,
                "preferences": preferences,
                "transfer_lookup_key": transfer_lookup_key,
                "physical_bundle": physical_bundle,
            },
            dump_with=params._SerializerIssuingPersonalizationDesignCreateBody,
            style={
                "card_logo": "form",
                "carrier_text": "deepObject",
                "expand": "deepObject",
                "lookup_key": "form",
                "metadata": "deepObject",
                "name": "form",
                "physical_bundle": "form",
                "preferences": "deepObject",
                "transfer_lookup_key": "form",
            },
            explode={
                "card_logo": True,
                "carrier_text": True,
                "expand": True,
                "lookup_key": True,
                "metadata": True,
                "name": True,
                "physical_bundle": True,
                "preferences": True,
                "transfer_lookup_key": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/issuing/personalization_designs",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        personalization_design: str,
        data: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Update a personalization design

        <p>Updates a card personalization object.</p>

        POST /v1/issuing/personalization_designs/{personalization_design}

        Args:
            data: IssuingPersonalizationDesignUpdateBody
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.personalization_design.update(personalization_design="string")
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingPersonalizationDesignUpdateBody,
                style={
                    "card_logo": "deepObject",
                    "carrier_text": "deepObject",
                    "expand": "deepObject",
                    "lookup_key": "deepObject",
                    "metadata": "deepObject",
                    "name": "deepObject",
                    "physical_bundle": "form",
                    "preferences": "deepObject",
                    "transfer_lookup_key": "form",
                },
                explode={
                    "card_logo": True,
                    "carrier_text": True,
                    "expand": True,
                    "lookup_key": True,
                    "metadata": True,
                    "name": True,
                    "physical_bundle": True,
                    "preferences": True,
                    "transfer_lookup_key": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/personalization_designs/{personalization_design}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )


class AsyncPersonalizationDesignClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_keys: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        preferences: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignListPreferences],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["active", "inactive", "rejected", "review"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesignListResponse:
        """
        List all personalization designs

        <p>Returns a list of personalization design objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/personalization_designs

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lookup_keys: Only return personalization designs with the given lookup keys.
            preferences: Only return personalization designs with the given preferences.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return personalization designs with the given status.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.personalization_design.list()
        ```
        """
        models.IssuingPersonalizationDesignListResponse.model_rebuild(
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
        if not isinstance(lookup_keys, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lookup_keys",
                to_encodable(item=lookup_keys, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        if not isinstance(preferences, type_utils.NotGiven):
            encode_query_param(
                _query,
                "preferences",
                to_encodable(
                    item=preferences,
                    dump_with=params._SerializerIssuingPersonalizationDesignListPreferences,
                ),
                style="deepObject",
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
                        "active", "inactive", "rejected", "review"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/issuing/personalization_designs",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingPersonalizationDesignListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        personalization_design: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Retrieve a personalization design

        <p>Retrieves a personalization design object.</p>

        GET /v1/issuing/personalization_designs/{personalization_design}

        Args:
            expand: Specifies which fields in the response should be expanded.
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.personalization_design.get(personalization_design="string")
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/issuing/personalization_designs/{personalization_design}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        physical_bundle: str,
        card_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        carrier_text: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignCreateBodyCarrierText],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        preferences: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignCreateBodyPreferences],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_lookup_key: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Create a personalization design

        <p>Creates a personalization design object.</p>

        POST /v1/issuing/personalization_designs

        Args:
            card_logo: The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.
            carrier_text: Hash containing carrier text, for use with physical bundles that support carrier text.
            expand: Specifies which fields in the response should be expanded.
            lookup_key: A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            name: Friendly display name.
            preferences: Information on whether this personalization design is used to create cards when one is not specified.
            transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design.
            physical_bundle: The physical bundle object belonging to this personalization design.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.personalization_design.create(physical_bundle="string")
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "card_logo": card_logo,
                "carrier_text": carrier_text,
                "expand": expand,
                "lookup_key": lookup_key,
                "metadata": metadata,
                "name": name,
                "preferences": preferences,
                "transfer_lookup_key": transfer_lookup_key,
                "physical_bundle": physical_bundle,
            },
            dump_with=params._SerializerIssuingPersonalizationDesignCreateBody,
            style={
                "card_logo": "form",
                "carrier_text": "deepObject",
                "expand": "deepObject",
                "lookup_key": "form",
                "metadata": "deepObject",
                "name": "form",
                "physical_bundle": "form",
                "preferences": "deepObject",
                "transfer_lookup_key": "form",
            },
            explode={
                "card_logo": True,
                "carrier_text": True,
                "expand": True,
                "lookup_key": True,
                "metadata": True,
                "name": True,
                "physical_bundle": True,
                "preferences": True,
                "transfer_lookup_key": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/issuing/personalization_designs",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        personalization_design: str,
        data: typing.Union[
            typing.Optional[params.IssuingPersonalizationDesignUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Update a personalization design

        <p>Updates a card personalization object.</p>

        POST /v1/issuing/personalization_designs/{personalization_design}

        Args:
            data: IssuingPersonalizationDesignUpdateBody
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.personalization_design.update(
            personalization_design="string"
        )
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingPersonalizationDesignUpdateBody,
                style={
                    "card_logo": "deepObject",
                    "carrier_text": "deepObject",
                    "expand": "deepObject",
                    "lookup_key": "deepObject",
                    "metadata": "deepObject",
                    "name": "deepObject",
                    "physical_bundle": "form",
                    "preferences": "deepObject",
                    "transfer_lookup_key": "form",
                },
                explode={
                    "card_logo": True,
                    "carrier_text": True,
                    "expand": True,
                    "lookup_key": True,
                    "metadata": True,
                    "name": True,
                    "physical_bundle": True,
                    "preferences": True,
                    "transfer_lookup_key": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/personalization_designs/{personalization_design}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )
