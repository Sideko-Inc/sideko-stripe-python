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


class PersonClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        account: str,
        person: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedPerson:
        """
        Delete a person

        <p>Deletes an existing person’s relationship to the account’s legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the <code>account_opener</code>. If your integration is using the <code>executive</code> parameter, you cannot delete the only verified <code>executive</code> on file.</p>

        DELETE /v1/accounts/{account}/persons/{person}

        Args:
            account: str
            person: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.person.delete(account="string", person="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/accounts/{account}/persons/{person}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedPerson,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        account: str,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        relationship: typing.Union[
            typing.Optional[params.AccountPersonListRelationship], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountPersonListResponse:
        """
        List all persons

        <p>Returns a list of people associated with the account’s legal entity. The people are returned sorted by creation date, with the most recent people appearing first.</p>

        GET /v1/accounts/{account}/persons

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            relationship: Filters on the list of people returned based on the person's relationship to the account's company.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.person.list(account="string")
        ```
        """
        models.AccountPersonListResponse.model_rebuild(
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
        if not isinstance(relationship, type_utils.NotGiven):
            encode_query_param(
                _query,
                "relationship",
                to_encodable(
                    item=relationship,
                    dump_with=params._SerializerAccountPersonListRelationship,
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
        return self._base_client.request(
            method="GET",
            path=f"/v1/accounts/{account}/persons",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.AccountPersonListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account: str,
        person: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Person:
        """
        Retrieve a person

        <p>Retrieves an existing person.</p>

        GET /v1/accounts/{account}/persons/{person}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            person: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.person.get(account="string", person="string")
        ```
        """
        models.Person.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}/persons/{person}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Person,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountPersonCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Person:
        """
        Create a person

        <p>Creates a new person.</p>

        POST /v1/accounts/{account}/persons

        Args:
            data: AccountPersonCreateBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.person.create(account="string")
        ```
        """
        models.Person.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountPersonCreateBody,
                style={
                    "additional_tos_acceptances": "deepObject",
                    "address": "deepObject",
                    "address_kana": "deepObject",
                    "address_kanji": "deepObject",
                    "dob": "deepObject",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "first_name": "form",
                    "first_name_kana": "form",
                    "first_name_kanji": "form",
                    "full_name_aliases": "deepObject",
                    "gender": "form",
                    "id_number": "form",
                    "id_number_secondary": "form",
                    "last_name": "form",
                    "last_name_kana": "form",
                    "last_name_kanji": "form",
                    "maiden_name": "form",
                    "metadata": "deepObject",
                    "nationality": "form",
                    "person_token": "form",
                    "phone": "form",
                    "political_exposure": "form",
                    "registered_address": "deepObject",
                    "relationship": "deepObject",
                    "ssn_last_4": "form",
                    "verification": "deepObject",
                },
                explode={
                    "additional_tos_acceptances": True,
                    "address": True,
                    "address_kana": True,
                    "address_kanji": True,
                    "dob": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "first_name": True,
                    "first_name_kana": True,
                    "first_name_kanji": True,
                    "full_name_aliases": True,
                    "gender": True,
                    "id_number": True,
                    "id_number_secondary": True,
                    "last_name": True,
                    "last_name_kana": True,
                    "last_name_kanji": True,
                    "maiden_name": True,
                    "metadata": True,
                    "nationality": True,
                    "person_token": True,
                    "phone": True,
                    "political_exposure": True,
                    "registered_address": True,
                    "relationship": True,
                    "ssn_last_4": True,
                    "verification": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/persons",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Person,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        account: str,
        person: str,
        data: typing.Union[
            typing.Optional[params.AccountPersonUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Person:
        """
        Update a person

        <p>Updates an existing person.</p>

        POST /v1/accounts/{account}/persons/{person}

        Args:
            data: AccountPersonUpdateBody
            account: str
            person: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.person.update(account="string", person="string")
        ```
        """
        models.Person.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountPersonUpdateBody,
                style={
                    "additional_tos_acceptances": "deepObject",
                    "address": "deepObject",
                    "address_kana": "deepObject",
                    "address_kanji": "deepObject",
                    "dob": "deepObject",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "first_name": "form",
                    "first_name_kana": "form",
                    "first_name_kanji": "form",
                    "full_name_aliases": "deepObject",
                    "gender": "form",
                    "id_number": "form",
                    "id_number_secondary": "form",
                    "last_name": "form",
                    "last_name_kana": "form",
                    "last_name_kanji": "form",
                    "maiden_name": "form",
                    "metadata": "deepObject",
                    "nationality": "form",
                    "person_token": "form",
                    "phone": "form",
                    "political_exposure": "form",
                    "registered_address": "deepObject",
                    "relationship": "deepObject",
                    "ssn_last_4": "form",
                    "verification": "deepObject",
                },
                explode={
                    "additional_tos_acceptances": True,
                    "address": True,
                    "address_kana": True,
                    "address_kanji": True,
                    "dob": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "first_name": True,
                    "first_name_kana": True,
                    "first_name_kanji": True,
                    "full_name_aliases": True,
                    "gender": True,
                    "id_number": True,
                    "id_number_secondary": True,
                    "last_name": True,
                    "last_name_kana": True,
                    "last_name_kanji": True,
                    "maiden_name": True,
                    "metadata": True,
                    "nationality": True,
                    "person_token": True,
                    "phone": True,
                    "political_exposure": True,
                    "registered_address": True,
                    "relationship": True,
                    "ssn_last_4": True,
                    "verification": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/persons/{person}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Person,
            request_options=request_options or default_request_options(),
        )


class AsyncPersonClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        account: str,
        person: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedPerson:
        """
        Delete a person

        <p>Deletes an existing person’s relationship to the account’s legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the <code>account_opener</code>. If your integration is using the <code>executive</code> parameter, you cannot delete the only verified <code>executive</code> on file.</p>

        DELETE /v1/accounts/{account}/persons/{person}

        Args:
            account: str
            person: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.person.delete(account="string", person="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/accounts/{account}/persons/{person}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedPerson,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        account: str,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        relationship: typing.Union[
            typing.Optional[params.AccountPersonListRelationship], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountPersonListResponse:
        """
        List all persons

        <p>Returns a list of people associated with the account’s legal entity. The people are returned sorted by creation date, with the most recent people appearing first.</p>

        GET /v1/accounts/{account}/persons

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            relationship: Filters on the list of people returned based on the person's relationship to the account's company.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.person.list(account="string")
        ```
        """
        models.AccountPersonListResponse.model_rebuild(
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
        if not isinstance(relationship, type_utils.NotGiven):
            encode_query_param(
                _query,
                "relationship",
                to_encodable(
                    item=relationship,
                    dump_with=params._SerializerAccountPersonListRelationship,
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
        return await self._base_client.request(
            method="GET",
            path=f"/v1/accounts/{account}/persons",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.AccountPersonListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account: str,
        person: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Person:
        """
        Retrieve a person

        <p>Retrieves an existing person.</p>

        GET /v1/accounts/{account}/persons/{person}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            person: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.person.get(account="string", person="string")
        ```
        """
        models.Person.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}/persons/{person}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Person,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountPersonCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Person:
        """
        Create a person

        <p>Creates a new person.</p>

        POST /v1/accounts/{account}/persons

        Args:
            data: AccountPersonCreateBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.person.create(account="string")
        ```
        """
        models.Person.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountPersonCreateBody,
                style={
                    "additional_tos_acceptances": "deepObject",
                    "address": "deepObject",
                    "address_kana": "deepObject",
                    "address_kanji": "deepObject",
                    "dob": "deepObject",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "first_name": "form",
                    "first_name_kana": "form",
                    "first_name_kanji": "form",
                    "full_name_aliases": "deepObject",
                    "gender": "form",
                    "id_number": "form",
                    "id_number_secondary": "form",
                    "last_name": "form",
                    "last_name_kana": "form",
                    "last_name_kanji": "form",
                    "maiden_name": "form",
                    "metadata": "deepObject",
                    "nationality": "form",
                    "person_token": "form",
                    "phone": "form",
                    "political_exposure": "form",
                    "registered_address": "deepObject",
                    "relationship": "deepObject",
                    "ssn_last_4": "form",
                    "verification": "deepObject",
                },
                explode={
                    "additional_tos_acceptances": True,
                    "address": True,
                    "address_kana": True,
                    "address_kanji": True,
                    "dob": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "first_name": True,
                    "first_name_kana": True,
                    "first_name_kanji": True,
                    "full_name_aliases": True,
                    "gender": True,
                    "id_number": True,
                    "id_number_secondary": True,
                    "last_name": True,
                    "last_name_kana": True,
                    "last_name_kanji": True,
                    "maiden_name": True,
                    "metadata": True,
                    "nationality": True,
                    "person_token": True,
                    "phone": True,
                    "political_exposure": True,
                    "registered_address": True,
                    "relationship": True,
                    "ssn_last_4": True,
                    "verification": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/persons",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Person,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        account: str,
        person: str,
        data: typing.Union[
            typing.Optional[params.AccountPersonUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Person:
        """
        Update a person

        <p>Updates an existing person.</p>

        POST /v1/accounts/{account}/persons/{person}

        Args:
            data: AccountPersonUpdateBody
            account: str
            person: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.person.update(account="string", person="string")
        ```
        """
        models.Person.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountPersonUpdateBody,
                style={
                    "additional_tos_acceptances": "deepObject",
                    "address": "deepObject",
                    "address_kana": "deepObject",
                    "address_kanji": "deepObject",
                    "dob": "deepObject",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "first_name": "form",
                    "first_name_kana": "form",
                    "first_name_kanji": "form",
                    "full_name_aliases": "deepObject",
                    "gender": "form",
                    "id_number": "form",
                    "id_number_secondary": "form",
                    "last_name": "form",
                    "last_name_kana": "form",
                    "last_name_kanji": "form",
                    "maiden_name": "form",
                    "metadata": "deepObject",
                    "nationality": "form",
                    "person_token": "form",
                    "phone": "form",
                    "political_exposure": "form",
                    "registered_address": "deepObject",
                    "relationship": "deepObject",
                    "ssn_last_4": "form",
                    "verification": "deepObject",
                },
                explode={
                    "additional_tos_acceptances": True,
                    "address": True,
                    "address_kana": True,
                    "address_kanji": True,
                    "dob": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "first_name": True,
                    "first_name_kana": True,
                    "first_name_kanji": True,
                    "full_name_aliases": True,
                    "gender": True,
                    "id_number": True,
                    "id_number_secondary": True,
                    "last_name": True,
                    "last_name_kana": True,
                    "last_name_kanji": True,
                    "maiden_name": True,
                    "metadata": True,
                    "nationality": True,
                    "person_token": True,
                    "phone": True,
                    "political_exposure": True,
                    "registered_address": True,
                    "relationship": True,
                    "ssn_last_4": True,
                    "verification": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/persons/{person}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Person,
            request_options=request_options or default_request_options(),
        )
