import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class ExternalAccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ExternalAccountCreateBody], type_utils.NotGiven
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

        POST /v1/external_accounts/{id}

        Args:
            data: ExternalAccountCreateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.external_account.create(id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerExternalAccountCreateBody,
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
            path=f"/v1/external_accounts/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )


class AsyncExternalAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ExternalAccountCreateBody], type_utils.NotGiven
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

        POST /v1/external_accounts/{id}

        Args:
            data: ExternalAccountCreateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.external_account.create(id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerExternalAccountCreateBody,
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
            path=f"/v1/external_accounts/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.BankAccount, models.Card],
            request_options=request_options or default_request_options(),
        )
