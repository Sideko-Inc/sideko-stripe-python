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


class InvoiceRenderingTemplateClient:
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "archived"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplateListResponse:
        """
        List all invoice rendering templates

        <p>List all templates, ordered by creation date, with the most recently created template appearing first.</p>

        GET /v1/invoice_rendering_templates

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: typing_extensions.Literal["active", "archived"]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_rendering_template.list()
        ```
        """
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
                    dump_with=typing_extensions.Literal["active", "archived"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/invoice_rendering_templates",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceRenderingTemplateListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        template: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        version: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplate:
        """
        Retrieve an invoice rendering template

        <p>Retrieves an invoice rendering template with the given ID. It by default returns the latest version of the template. Optionally, specify a version to see previous versions.</p>

        GET /v1/invoice_rendering_templates/{template}

        Args:
            expand: Specifies which fields in the response should be expanded.
            version: int
            template: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_rendering_template.get(template="string")
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
        if not isinstance(version, type_utils.NotGiven):
            encode_query_param(
                _query,
                "version",
                to_encodable(item=version, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v1/invoice_rendering_templates/{template}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceRenderingTemplate,
            request_options=request_options or default_request_options(),
        )

    def archive(
        self,
        *,
        template: str,
        data: typing.Union[
            typing.Optional[params.InvoiceRenderingTemplateArchiveBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplate:
        """
        Archive an invoice rendering template

        <p>Updates the status of an invoice rendering template to ‘archived’ so no new Stripe objects (customers, invoices, etc.) can reference it. The template can also no longer be updated. However, if the template is already set on a Stripe object, it will continue to be applied on invoices generated by it.</p>

        POST /v1/invoice_rendering_templates/{template}/archive

        Args:
            data: InvoiceRenderingTemplateArchiveBody
            template: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_rendering_template.archive(template="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceRenderingTemplateArchiveBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoice_rendering_templates/{template}/archive",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.InvoiceRenderingTemplate,
            request_options=request_options or default_request_options(),
        )

    def unarchive(
        self,
        *,
        template: str,
        data: typing.Union[
            typing.Optional[params.InvoiceRenderingTemplateUnarchiveBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplate:
        """
        Unarchive an invoice rendering template

        <p>Unarchive an invoice rendering template so it can be used on new Stripe objects again.</p>

        POST /v1/invoice_rendering_templates/{template}/unarchive

        Args:
            data: InvoiceRenderingTemplateUnarchiveBody
            template: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_rendering_template.unarchive(template="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceRenderingTemplateUnarchiveBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/invoice_rendering_templates/{template}/unarchive",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.InvoiceRenderingTemplate,
            request_options=request_options or default_request_options(),
        )


class AsyncInvoiceRenderingTemplateClient:
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "archived"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplateListResponse:
        """
        List all invoice rendering templates

        <p>List all templates, ordered by creation date, with the most recently created template appearing first.</p>

        GET /v1/invoice_rendering_templates

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: typing_extensions.Literal["active", "archived"]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_rendering_template.list()
        ```
        """
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
                    dump_with=typing_extensions.Literal["active", "archived"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/invoice_rendering_templates",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceRenderingTemplateListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        template: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        version: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplate:
        """
        Retrieve an invoice rendering template

        <p>Retrieves an invoice rendering template with the given ID. It by default returns the latest version of the template. Optionally, specify a version to see previous versions.</p>

        GET /v1/invoice_rendering_templates/{template}

        Args:
            expand: Specifies which fields in the response should be expanded.
            version: int
            template: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_rendering_template.get(template="string")
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
        if not isinstance(version, type_utils.NotGiven):
            encode_query_param(
                _query,
                "version",
                to_encodable(item=version, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v1/invoice_rendering_templates/{template}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.InvoiceRenderingTemplate,
            request_options=request_options or default_request_options(),
        )

    async def archive(
        self,
        *,
        template: str,
        data: typing.Union[
            typing.Optional[params.InvoiceRenderingTemplateArchiveBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplate:
        """
        Archive an invoice rendering template

        <p>Updates the status of an invoice rendering template to ‘archived’ so no new Stripe objects (customers, invoices, etc.) can reference it. The template can also no longer be updated. However, if the template is already set on a Stripe object, it will continue to be applied on invoices generated by it.</p>

        POST /v1/invoice_rendering_templates/{template}/archive

        Args:
            data: InvoiceRenderingTemplateArchiveBody
            template: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_rendering_template.archive(template="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceRenderingTemplateArchiveBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoice_rendering_templates/{template}/archive",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.InvoiceRenderingTemplate,
            request_options=request_options or default_request_options(),
        )

    async def unarchive(
        self,
        *,
        template: str,
        data: typing.Union[
            typing.Optional[params.InvoiceRenderingTemplateUnarchiveBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceRenderingTemplate:
        """
        Unarchive an invoice rendering template

        <p>Unarchive an invoice rendering template so it can be used on new Stripe objects again.</p>

        POST /v1/invoice_rendering_templates/{template}/unarchive

        Args:
            data: InvoiceRenderingTemplateUnarchiveBody
            template: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_rendering_template.unarchive(template="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerInvoiceRenderingTemplateUnarchiveBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/invoice_rendering_templates/{template}/unarchive",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.InvoiceRenderingTemplate,
            request_options=request_options or default_request_options(),
        )
