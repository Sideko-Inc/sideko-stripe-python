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
from sideko_stripe.resources.account.bank_account import (
    AsyncBankAccountClient,
    BankAccountClient,
)
from sideko_stripe.resources.account.capability import (
    AsyncCapabilityClient,
    CapabilityClient,
)
from sideko_stripe.resources.account.external_account import (
    AsyncExternalAccountClient,
    ExternalAccountClient,
)
from sideko_stripe.resources.account.people import AsyncPeopleClient, PeopleClient
from sideko_stripe.resources.account.person import AsyncPersonClient, PersonClient
from sideko_stripe.types import models, params


class AccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.bank_account = BankAccountClient(base_client=self._base_client)
        self.external_account = ExternalAccountClient(base_client=self._base_client)
        self.people = PeopleClient(base_client=self._base_client)
        self.person = PersonClient(base_client=self._base_client)
        self.capability = CapabilityClient(base_client=self._base_client)

    def delete(
        self, *, account: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedAccount:
        """
        Delete an account

        <p>With <a href="/connect">Connect</a>, you can delete accounts you manage.</p>

        <p>Test-mode accounts can be deleted at any time.</p>

        <p>Live-mode accounts where Stripe is responsible for negative account balances cannot be deleted, which includes Standard accounts. Live-mode accounts where your platform is liable for negative account balances, which includes Custom and Express accounts, can be deleted when all <a href="/api/balance/balance_object">balances</a> are zero.</p>

        <p>If you want to delete your own account, use the <a href="https://dashboard.stripe.com/settings/account">account information tab in your account settings</a> instead.</p>

        DELETE /v1/accounts/{account}

        Args:
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.delete(account="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedAccount,
            request_options=request_options or default_request_options(),
        )

    def details(
        self,
        *,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Retrieve account

        <p>Retrieves the details of an account.</p>

        GET /v1/account

        Args:
            expand: Specifies which fields in the response should be expanded.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.details()
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/v1/account",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.AccountListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountListResponse:
        """
        List all connected accounts

        <p>Returns a list of accounts connected to your platform via <a href="/docs/connect">Connect</a>. If you’re not a platform, the list is empty.</p>

        GET /v1/accounts

        Args:
            created: Only return connected accounts that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.list()
        ```
        """
        models.AccountListResponse.model_rebuild(
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
                        params._SerializerAccountListCreatedObj0, int
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
            path="/v1/accounts",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.AccountListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Retrieve account

        <p>Retrieves the details of an account.</p>

        GET /v1/accounts/{account}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.get(account="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.AccountCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        <p>With <a href="/docs/connect">Connect</a>, you can create Stripe accounts for your users.
        To do this, you’ll first need to <a href="https://dashboard.stripe.com/account/applications/settings">register your platform</a>.</p>

        <p>If you’ve already collected information for your connected accounts, you <a href="/docs/connect/best-practices#onboarding">can prefill that information</a> when
        creating the account. Connect Onboarding won’t ask for the prefilled information during account onboarding.
        You can prefill any information on the account.</p>

        POST /v1/accounts

        Args:
            data: AccountCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.create()
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountCreateBody,
                style={
                    "account_token": "form",
                    "bank_account": "deepObject",
                    "business_profile": "deepObject",
                    "business_type": "form",
                    "capabilities": "deepObject",
                    "company": "deepObject",
                    "controller": "deepObject",
                    "country": "form",
                    "default_currency": "form",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "external_account": "form",
                    "groups": "deepObject",
                    "individual": "deepObject",
                    "metadata": "deepObject",
                    "settings": "deepObject",
                    "tos_acceptance": "deepObject",
                    "type": "form",
                },
                explode={
                    "account_token": True,
                    "bank_account": True,
                    "business_profile": True,
                    "business_type": True,
                    "capabilities": True,
                    "company": True,
                    "controller": True,
                    "country": True,
                    "default_currency": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "external_account": True,
                    "groups": True,
                    "individual": True,
                    "metadata": True,
                    "settings": True,
                    "tos_acceptance": True,
                    "type": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/accounts",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Update an account

        <p>Updates a <a href="/connect/accounts">connected account</a> by setting the values of the parameters passed. Any parameters not provided are
        left unchanged.</p>

        <p>For accounts where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a>
        is <code>application</code>, which includes Custom accounts, you can update any information on the account.</p>

        <p>For accounts where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a>
        is <code>stripe</code>, which includes Standard and Express accounts, you can update all information until you create
        an <a href="/api/account_links">Account Link</a> or <a href="/api/account_sessions">Account Session</a> to start Connect onboarding,
        after which some properties can no longer be updated.</p>

        <p>To update your own account, use the <a href="https://dashboard.stripe.com/settings/account">Dashboard</a>. Refer to our
        <a href="/docs/connect/updating-accounts">Connect</a> documentation to learn more about updating accounts.</p>

        POST /v1/accounts/{account}

        Args:
            data: AccountUpdateBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.update(account="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountUpdateBody,
                style={
                    "account_token": "form",
                    "business_profile": "deepObject",
                    "business_type": "form",
                    "capabilities": "deepObject",
                    "company": "deepObject",
                    "default_currency": "form",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "external_account": "form",
                    "groups": "deepObject",
                    "individual": "deepObject",
                    "metadata": "deepObject",
                    "settings": "deepObject",
                    "tos_acceptance": "deepObject",
                },
                explode={
                    "account_token": True,
                    "business_profile": True,
                    "business_type": True,
                    "capabilities": True,
                    "company": True,
                    "default_currency": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "external_account": True,
                    "groups": True,
                    "individual": True,
                    "metadata": True,
                    "settings": True,
                    "tos_acceptance": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    def create_login_link(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountCreateLoginLinkBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LoginLink:
        """
        Create a login link

        <p>Creates a login link for a connected account to access the Express Dashboard.</p>

        <p><strong>You can only create login links for accounts that use the <a href="/connect/express-dashboard">Express Dashboard</a> and are connected to your platform</strong>.</p>

        POST /v1/accounts/{account}/login_links

        Args:
            data: AccountCreateLoginLinkBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.create_login_link(account="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountCreateLoginLinkBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/login_links",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.LoginLink,
            request_options=request_options or default_request_options(),
        )

    def reject(
        self,
        *,
        account: str,
        reason: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Reject an account

        <p>With <a href="/connect">Connect</a>, you can reject accounts that you have flagged as suspicious.</p>

        <p>Only accounts where your platform is liable for negative account balances, which includes Custom and Express accounts, can be rejected. Test-mode accounts can be rejected at any time. Live-mode accounts can only be rejected after all balances are zero.</p>

        POST /v1/accounts/{account}/reject

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            reason: The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.reject(account="string", reason="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"expand": expand, "reason": reason},
            dump_with=params._SerializerAccountRejectBody,
            style={"expand": "deepObject", "reason": "form"},
            explode={"expand": True, "reason": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/reject",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.bank_account = AsyncBankAccountClient(base_client=self._base_client)
        self.external_account = AsyncExternalAccountClient(
            base_client=self._base_client
        )
        self.people = AsyncPeopleClient(base_client=self._base_client)
        self.person = AsyncPersonClient(base_client=self._base_client)
        self.capability = AsyncCapabilityClient(base_client=self._base_client)

    async def delete(
        self, *, account: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedAccount:
        """
        Delete an account

        <p>With <a href="/connect">Connect</a>, you can delete accounts you manage.</p>

        <p>Test-mode accounts can be deleted at any time.</p>

        <p>Live-mode accounts where Stripe is responsible for negative account balances cannot be deleted, which includes Standard accounts. Live-mode accounts where your platform is liable for negative account balances, which includes Custom and Express accounts, can be deleted when all <a href="/api/balance/balance_object">balances</a> are zero.</p>

        <p>If you want to delete your own account, use the <a href="https://dashboard.stripe.com/settings/account">account information tab in your account settings</a> instead.</p>

        DELETE /v1/accounts/{account}

        Args:
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.delete(account="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedAccount,
            request_options=request_options or default_request_options(),
        )

    async def details(
        self,
        *,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Retrieve account

        <p>Retrieves the details of an account.</p>

        GET /v1/account

        Args:
            expand: Specifies which fields in the response should be expanded.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.details()
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/v1/account",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.AccountListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountListResponse:
        """
        List all connected accounts

        <p>Returns a list of accounts connected to your platform via <a href="/docs/connect">Connect</a>. If you’re not a platform, the list is empty.</p>

        GET /v1/accounts

        Args:
            created: Only return connected accounts that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.list()
        ```
        """
        models.AccountListResponse.model_rebuild(
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
                        params._SerializerAccountListCreatedObj0, int
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
            path="/v1/accounts",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.AccountListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Retrieve account

        <p>Retrieves the details of an account.</p>

        GET /v1/accounts/{account}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.get(account="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.AccountCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        <p>With <a href="/docs/connect">Connect</a>, you can create Stripe accounts for your users.
        To do this, you’ll first need to <a href="https://dashboard.stripe.com/account/applications/settings">register your platform</a>.</p>

        <p>If you’ve already collected information for your connected accounts, you <a href="/docs/connect/best-practices#onboarding">can prefill that information</a> when
        creating the account. Connect Onboarding won’t ask for the prefilled information during account onboarding.
        You can prefill any information on the account.</p>

        POST /v1/accounts

        Args:
            data: AccountCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.create()
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountCreateBody,
                style={
                    "account_token": "form",
                    "bank_account": "deepObject",
                    "business_profile": "deepObject",
                    "business_type": "form",
                    "capabilities": "deepObject",
                    "company": "deepObject",
                    "controller": "deepObject",
                    "country": "form",
                    "default_currency": "form",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "external_account": "form",
                    "groups": "deepObject",
                    "individual": "deepObject",
                    "metadata": "deepObject",
                    "settings": "deepObject",
                    "tos_acceptance": "deepObject",
                    "type": "form",
                },
                explode={
                    "account_token": True,
                    "bank_account": True,
                    "business_profile": True,
                    "business_type": True,
                    "capabilities": True,
                    "company": True,
                    "controller": True,
                    "country": True,
                    "default_currency": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "external_account": True,
                    "groups": True,
                    "individual": True,
                    "metadata": True,
                    "settings": True,
                    "tos_acceptance": True,
                    "type": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/accounts",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Update an account

        <p>Updates a <a href="/connect/accounts">connected account</a> by setting the values of the parameters passed. Any parameters not provided are
        left unchanged.</p>

        <p>For accounts where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a>
        is <code>application</code>, which includes Custom accounts, you can update any information on the account.</p>

        <p>For accounts where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a>
        is <code>stripe</code>, which includes Standard and Express accounts, you can update all information until you create
        an <a href="/api/account_links">Account Link</a> or <a href="/api/account_sessions">Account Session</a> to start Connect onboarding,
        after which some properties can no longer be updated.</p>

        <p>To update your own account, use the <a href="https://dashboard.stripe.com/settings/account">Dashboard</a>. Refer to our
        <a href="/docs/connect/updating-accounts">Connect</a> documentation to learn more about updating accounts.</p>

        POST /v1/accounts/{account}

        Args:
            data: AccountUpdateBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.update(account="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountUpdateBody,
                style={
                    "account_token": "form",
                    "business_profile": "deepObject",
                    "business_type": "form",
                    "capabilities": "deepObject",
                    "company": "deepObject",
                    "default_currency": "form",
                    "documents": "deepObject",
                    "email": "form",
                    "expand": "deepObject",
                    "external_account": "form",
                    "groups": "deepObject",
                    "individual": "deepObject",
                    "metadata": "deepObject",
                    "settings": "deepObject",
                    "tos_acceptance": "deepObject",
                },
                explode={
                    "account_token": True,
                    "business_profile": True,
                    "business_type": True,
                    "capabilities": True,
                    "company": True,
                    "default_currency": True,
                    "documents": True,
                    "email": True,
                    "expand": True,
                    "external_account": True,
                    "groups": True,
                    "individual": True,
                    "metadata": True,
                    "settings": True,
                    "tos_acceptance": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )

    async def create_login_link(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountCreateLoginLinkBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LoginLink:
        """
        Create a login link

        <p>Creates a login link for a connected account to access the Express Dashboard.</p>

        <p><strong>You can only create login links for accounts that use the <a href="/connect/express-dashboard">Express Dashboard</a> and are connected to your platform</strong>.</p>

        POST /v1/accounts/{account}/login_links

        Args:
            data: AccountCreateLoginLinkBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.create_login_link(account="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountCreateLoginLinkBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/login_links",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.LoginLink,
            request_options=request_options or default_request_options(),
        )

    async def reject(
        self,
        *,
        account: str,
        reason: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Reject an account

        <p>With <a href="/connect">Connect</a>, you can reject accounts that you have flagged as suspicious.</p>

        <p>Only accounts where your platform is liable for negative account balances, which includes Custom and Express accounts, can be rejected. Test-mode accounts can be rejected at any time. Live-mode accounts can only be rejected after all balances are zero.</p>

        POST /v1/accounts/{account}/reject

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            reason: The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.reject(account="string", reason="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"expand": expand, "reason": reason},
            dump_with=params._SerializerAccountRejectBody,
            style={"expand": "deepObject", "reason": "form"},
            explode={"expand": True, "reason": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/reject",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )
