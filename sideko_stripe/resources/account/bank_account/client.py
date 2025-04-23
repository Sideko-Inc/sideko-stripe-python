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


class BankAccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        account: str,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.DeletedBankAccount, models.DeletedCard]:
        """
        Delete an external account

        <p>Delete a specified external account for a given account.</p>

        DELETE /v1/accounts/{account}/bank_accounts/{id}

        Args:
            account: str
            id: Unique identifier for the external account to be deleted.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.bank_account.delete(account="string", id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/accounts/{account}/bank_accounts/{id}",
            auth_names=["bearerAuth"],
            cast_to=typing.Union[models.DeletedBankAccount, models.DeletedCard],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account: str,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.BankAccount, models.Card]:
        """
        Retrieve an external account

        <p>Retrieve a specified external account for a given account.</p>

        GET /v1/accounts/{account}/bank_accounts/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            id: Unique identifier for the external account to be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.bank_account.get(account="string", id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}/bank_accounts/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountBankAccountCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.BankAccount, models.Card]:
        """
        Create an external account

        <p>Create an external account for a given account.</p>

        POST /v1/accounts/{account}/bank_accounts

        Args:
            data: AccountBankAccountCreateBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.bank_account.create(account="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountBankAccountCreateBody,
                style={
                    "bank_account": "deepObject",
                    "default_for_currency": "form",
                    "expand": "deepObject",
                    "external_account": "form",
                    "metadata": "deepObject",
                },
                explode={
                    "bank_account": True,
                    "default_for_currency": True,
                    "expand": True,
                    "external_account": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/bank_accounts",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        account: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.AccountBankAccountUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.BankAccount, models.Card]:
        """
        <p>Updates the metadata, account holder name, account holder type of a bank account belonging to
        a connected account and optionally sets it as the default for its currency. Other bank account
        details are not editable by design.</p>

        <p>You can only update bank accounts when <a href="/api/accounts/object#account_object-controller-requirement_collection">account.controller.requirement_collection</a> is <code>application</code>, which includes <a href="/connect/custom-accounts">Custom accounts</a>.</p>

        <p>You can re-enable a disabled bank account by performing an update call without providing any
        arguments or changes.</p>

        POST /v1/accounts/{account}/bank_accounts/{id}

        Args:
            data: AccountBankAccountUpdateBody
            account: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.bank_account.update(account="string", id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountBankAccountUpdateBody,
                style={
                    "account_holder_name": "form",
                    "account_holder_type": "form",
                    "account_type": "form",
                    "address_city": "form",
                    "address_country": "form",
                    "address_line1": "form",
                    "address_line2": "form",
                    "address_state": "form",
                    "address_zip": "form",
                    "default_for_currency": "form",
                    "documents": "deepObject",
                    "exp_month": "form",
                    "exp_year": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={
                    "account_holder_name": True,
                    "account_holder_type": True,
                    "account_type": True,
                    "address_city": True,
                    "address_country": True,
                    "address_line1": True,
                    "address_line2": True,
                    "address_state": True,
                    "address_zip": True,
                    "default_for_currency": True,
                    "documents": True,
                    "exp_month": True,
                    "exp_year": True,
                    "expand": True,
                    "metadata": True,
                    "name": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/bank_accounts/{id}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )


class AsyncBankAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        account: str,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.DeletedBankAccount, models.DeletedCard]:
        """
        Delete an external account

        <p>Delete a specified external account for a given account.</p>

        DELETE /v1/accounts/{account}/bank_accounts/{id}

        Args:
            account: str
            id: Unique identifier for the external account to be deleted.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.bank_account.delete(account="string", id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/accounts/{account}/bank_accounts/{id}",
            auth_names=["bearerAuth"],
            cast_to=typing.Union[models.DeletedBankAccount, models.DeletedCard],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account: str,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.BankAccount, models.Card]:
        """
        Retrieve an external account

        <p>Retrieve a specified external account for a given account.</p>

        GET /v1/accounts/{account}/bank_accounts/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            id: Unique identifier for the external account to be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.bank_account.get(account="string", id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}/bank_accounts/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.AccountBankAccountCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.BankAccount, models.Card]:
        """
        Create an external account

        <p>Create an external account for a given account.</p>

        POST /v1/accounts/{account}/bank_accounts

        Args:
            data: AccountBankAccountCreateBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.bank_account.create(account="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountBankAccountCreateBody,
                style={
                    "bank_account": "deepObject",
                    "default_for_currency": "form",
                    "expand": "deepObject",
                    "external_account": "form",
                    "metadata": "deepObject",
                },
                explode={
                    "bank_account": True,
                    "default_for_currency": True,
                    "expand": True,
                    "external_account": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/bank_accounts",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        account: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.AccountBankAccountUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.BankAccount, models.Card]:
        """
        <p>Updates the metadata, account holder name, account holder type of a bank account belonging to
        a connected account and optionally sets it as the default for its currency. Other bank account
        details are not editable by design.</p>

        <p>You can only update bank accounts when <a href="/api/accounts/object#account_object-controller-requirement_collection">account.controller.requirement_collection</a> is <code>application</code>, which includes <a href="/connect/custom-accounts">Custom accounts</a>.</p>

        <p>You can re-enable a disabled bank account by performing an update call without providing any
        arguments or changes.</p>

        POST /v1/accounts/{account}/bank_accounts/{id}

        Args:
            data: AccountBankAccountUpdateBody
            account: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.bank_account.update(account="string", id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountBankAccountUpdateBody,
                style={
                    "account_holder_name": "form",
                    "account_holder_type": "form",
                    "account_type": "form",
                    "address_city": "form",
                    "address_country": "form",
                    "address_line1": "form",
                    "address_line2": "form",
                    "address_state": "form",
                    "address_zip": "form",
                    "default_for_currency": "form",
                    "documents": "deepObject",
                    "exp_month": "form",
                    "exp_year": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={
                    "account_holder_name": True,
                    "account_holder_type": True,
                    "account_type": True,
                    "address_city": True,
                    "address_country": True,
                    "address_line1": True,
                    "address_line2": True,
                    "address_state": True,
                    "address_zip": True,
                    "default_for_currency": True,
                    "documents": True,
                    "exp_month": True,
                    "exp_year": True,
                    "expand": True,
                    "metadata": True,
                    "name": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/bank_accounts/{id}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )
