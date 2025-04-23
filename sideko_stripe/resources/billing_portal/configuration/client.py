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


class ConfigurationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_default: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfigurationListResponse:
        """
        List portal configurations

        <p>Returns a list of configurations that describe the functionality of the customer portal.</p>

        GET /v1/billing_portal/configurations

        Args:
            active: Only return configurations that are active or inactive (e.g., pass `true` to only list active configurations).
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            is_default: Only return the default or non-default configurations (e.g., pass `true` to only list the default configuration).
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
        client.billing_portal.configuration.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(active, type_utils.NotGiven):
            encode_query_param(
                _query,
                "active",
                to_encodable(item=active, dump_with=bool),
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
        if not isinstance(is_default, type_utils.NotGiven):
            encode_query_param(
                _query,
                "is_default",
                to_encodable(item=is_default, dump_with=bool),
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
            path="/v1/billing_portal/configurations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingPortalConfigurationListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        configuration: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfiguration:
        """
        Retrieve a portal configuration

        <p>Retrieves a configuration that describes the functionality of the customer portal.</p>

        GET /v1/billing_portal/configurations/{configuration}

        Args:
            expand: Specifies which fields in the response should be expanded.
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing_portal.configuration.get(configuration="string")
        ```
        """
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
            path=f"/v1/billing_portal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingPortalConfiguration,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        features: params.BillingPortalConfigurationCreateBodyFeatures,
        business_profile: typing.Union[
            typing.Optional[params.BillingPortalConfigurationCreateBodyBusinessProfile],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        default_return_url: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        login_page: typing.Union[
            typing.Optional[params.BillingPortalConfigurationCreateBodyLoginPage],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.BillingPortalConfigurationCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfiguration:
        """
        Create a portal configuration

        <p>Creates a configuration that describes the functionality and behavior of a PortalSession</p>

        POST /v1/billing_portal/configurations

        Args:
            business_profile: The business information shown to customers in the portal.
            default_return_url: The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session.
            expand: Specifies which fields in the response should be expanded.
            login_page: The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            features: Information about the features available in the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing_portal.configuration.create(features={})
        ```
        """
        _data = to_form_urlencoded(
            item={
                "business_profile": business_profile,
                "default_return_url": default_return_url,
                "expand": expand,
                "login_page": login_page,
                "metadata": metadata,
                "features": features,
            },
            dump_with=params._SerializerBillingPortalConfigurationCreateBody,
            style={
                "business_profile": "deepObject",
                "default_return_url": "deepObject",
                "expand": "deepObject",
                "features": "deepObject",
                "login_page": "deepObject",
                "metadata": "deepObject",
            },
            explode={
                "business_profile": True,
                "default_return_url": True,
                "expand": True,
                "features": True,
                "login_page": True,
                "metadata": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/billing_portal/configurations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingPortalConfiguration,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        configuration: str,
        data: typing.Union[
            typing.Optional[params.BillingPortalConfigurationUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfiguration:
        """
        Update a portal configuration

        <p>Updates a configuration that describes the functionality of the customer portal.</p>

        POST /v1/billing_portal/configurations/{configuration}

        Args:
            data: BillingPortalConfigurationUpdateBody
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing_portal.configuration.update(configuration="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingPortalConfigurationUpdateBody,
                style={
                    "active": "form",
                    "business_profile": "deepObject",
                    "default_return_url": "deepObject",
                    "expand": "deepObject",
                    "features": "deepObject",
                    "login_page": "deepObject",
                    "metadata": "deepObject",
                },
                explode={
                    "active": True,
                    "business_profile": True,
                    "default_return_url": True,
                    "expand": True,
                    "features": True,
                    "login_page": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing_portal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingPortalConfiguration,
            request_options=request_options or default_request_options(),
        )


class AsyncConfigurationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_default: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfigurationListResponse:
        """
        List portal configurations

        <p>Returns a list of configurations that describe the functionality of the customer portal.</p>

        GET /v1/billing_portal/configurations

        Args:
            active: Only return configurations that are active or inactive (e.g., pass `true` to only list active configurations).
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            is_default: Only return the default or non-default configurations (e.g., pass `true` to only list the default configuration).
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
        await client.billing_portal.configuration.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(active, type_utils.NotGiven):
            encode_query_param(
                _query,
                "active",
                to_encodable(item=active, dump_with=bool),
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
        if not isinstance(is_default, type_utils.NotGiven):
            encode_query_param(
                _query,
                "is_default",
                to_encodable(item=is_default, dump_with=bool),
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
            path="/v1/billing_portal/configurations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingPortalConfigurationListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        configuration: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfiguration:
        """
        Retrieve a portal configuration

        <p>Retrieves a configuration that describes the functionality of the customer portal.</p>

        GET /v1/billing_portal/configurations/{configuration}

        Args:
            expand: Specifies which fields in the response should be expanded.
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing_portal.configuration.get(configuration="string")
        ```
        """
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
            path=f"/v1/billing_portal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingPortalConfiguration,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        features: params.BillingPortalConfigurationCreateBodyFeatures,
        business_profile: typing.Union[
            typing.Optional[params.BillingPortalConfigurationCreateBodyBusinessProfile],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        default_return_url: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        login_page: typing.Union[
            typing.Optional[params.BillingPortalConfigurationCreateBodyLoginPage],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.BillingPortalConfigurationCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfiguration:
        """
        Create a portal configuration

        <p>Creates a configuration that describes the functionality and behavior of a PortalSession</p>

        POST /v1/billing_portal/configurations

        Args:
            business_profile: The business information shown to customers in the portal.
            default_return_url: The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session.
            expand: Specifies which fields in the response should be expanded.
            login_page: The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            features: Information about the features available in the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing_portal.configuration.create(features={})
        ```
        """
        _data = to_form_urlencoded(
            item={
                "business_profile": business_profile,
                "default_return_url": default_return_url,
                "expand": expand,
                "login_page": login_page,
                "metadata": metadata,
                "features": features,
            },
            dump_with=params._SerializerBillingPortalConfigurationCreateBody,
            style={
                "business_profile": "deepObject",
                "default_return_url": "deepObject",
                "expand": "deepObject",
                "features": "deepObject",
                "login_page": "deepObject",
                "metadata": "deepObject",
            },
            explode={
                "business_profile": True,
                "default_return_url": True,
                "expand": True,
                "features": True,
                "login_page": True,
                "metadata": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/billing_portal/configurations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingPortalConfiguration,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        configuration: str,
        data: typing.Union[
            typing.Optional[params.BillingPortalConfigurationUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalConfiguration:
        """
        Update a portal configuration

        <p>Updates a configuration that describes the functionality of the customer portal.</p>

        POST /v1/billing_portal/configurations/{configuration}

        Args:
            data: BillingPortalConfigurationUpdateBody
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing_portal.configuration.update(configuration="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingPortalConfigurationUpdateBody,
                style={
                    "active": "form",
                    "business_profile": "deepObject",
                    "default_return_url": "deepObject",
                    "expand": "deepObject",
                    "features": "deepObject",
                    "login_page": "deepObject",
                    "metadata": "deepObject",
                },
                explode={
                    "active": True,
                    "business_profile": True,
                    "default_return_url": True,
                    "expand": True,
                    "features": True,
                    "login_page": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing_portal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingPortalConfiguration,
            request_options=request_options or default_request_options(),
        )
