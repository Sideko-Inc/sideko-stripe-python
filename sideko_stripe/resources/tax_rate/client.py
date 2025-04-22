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


class TaxRateClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.TaxRateListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inclusive: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRateListResponse:
        """
        List all tax rates

        <p>Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.</p>

        GET /v1/tax_rates

        Args:
            active: Optional flag to filter by tax rates that are either active or inactive (archived).
            created: Optional range for filtering created date.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            inclusive: Optional flag to filter by tax rates that are inclusive (or those that are not inclusive).
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
        client.tax_rate.list()
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
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerTaxRateListCreatedObj0, int
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
        if not isinstance(inclusive, type_utils.NotGiven):
            encode_query_param(
                _query,
                "inclusive",
                to_encodable(item=inclusive, dump_with=bool),
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
            path="/v1/tax_rates",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRateListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        tax_rate: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRate:
        """
        Retrieve a tax rate

        <p>Retrieves a tax rate with the given ID</p>

        GET /v1/tax_rates/{tax_rate}

        Args:
            expand: Specifies which fields in the response should be expanded.
            tax_rate: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax_rate.get(tax_rate="string")
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
            path=f"/v1/tax_rates/{tax_rate}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRate,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        display_name: str,
        inclusive: bool,
        percentage: float,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        country: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        jurisdiction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TaxRateCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "amusement_tax",
                    "communications_tax",
                    "gst",
                    "hst",
                    "igst",
                    "jct",
                    "lease_tax",
                    "pst",
                    "qst",
                    "retail_delivery_fee",
                    "rst",
                    "sales_tax",
                    "service_tax",
                    "vat",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRate:
        """
        Create a tax rate

        <p>Creates a new tax rate.</p>

        POST /v1/tax_rates

        Args:
            active: Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
            country: Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            description: An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
            expand: Specifies which fields in the response should be expanded.
            jurisdiction: The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            state: [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, "NY" for New York, United States.
            tax_type: The high-level tax type, such as `vat` or `sales_tax`.
            display_name: The display name of the tax rate, which will be shown to users.
            inclusive: This specifies if the tax rate is inclusive or exclusive.
            percentage: This represents the tax rate percent out of 100.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax_rate.create(display_name="string", inclusive=True, percentage=123.45)
        ```
        """
        _data = to_form_urlencoded(
            item={
                "active": active,
                "country": country,
                "description": description,
                "expand": expand,
                "jurisdiction": jurisdiction,
                "metadata": metadata,
                "state": state,
                "tax_type": tax_type,
                "display_name": display_name,
                "inclusive": inclusive,
                "percentage": percentage,
            },
            dump_with=params._SerializerTaxRateCreateBody,
            style={
                "active": "form",
                "country": "form",
                "description": "form",
                "display_name": "form",
                "expand": "deepObject",
                "inclusive": "form",
                "jurisdiction": "form",
                "metadata": "deepObject",
                "percentage": "form",
                "state": "form",
                "tax_type": "form",
            },
            explode={
                "active": True,
                "country": True,
                "description": True,
                "display_name": True,
                "expand": True,
                "inclusive": True,
                "jurisdiction": True,
                "metadata": True,
                "percentage": True,
                "state": True,
                "tax_type": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/tax_rates",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxRate,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        tax_rate: str,
        data: typing.Union[
            typing.Optional[params.TaxRateUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRate:
        """
        Update a tax rate

        <p>Updates an existing tax rate.</p>

        POST /v1/tax_rates/{tax_rate}

        Args:
            data: TaxRateUpdateBody
            tax_rate: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax_rate.update(tax_rate="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTaxRateUpdateBody,
                style={
                    "active": "form",
                    "country": "form",
                    "description": "form",
                    "display_name": "form",
                    "expand": "deepObject",
                    "jurisdiction": "form",
                    "metadata": "deepObject",
                    "state": "form",
                    "tax_type": "form",
                },
                explode={
                    "active": True,
                    "country": True,
                    "description": True,
                    "display_name": True,
                    "expand": True,
                    "jurisdiction": True,
                    "metadata": True,
                    "state": True,
                    "tax_type": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/tax_rates/{tax_rate}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxRate,
            request_options=request_options or default_request_options(),
        )


class AsyncTaxRateClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.TaxRateListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inclusive: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRateListResponse:
        """
        List all tax rates

        <p>Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.</p>

        GET /v1/tax_rates

        Args:
            active: Optional flag to filter by tax rates that are either active or inactive (archived).
            created: Optional range for filtering created date.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            inclusive: Optional flag to filter by tax rates that are inclusive (or those that are not inclusive).
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
        await client.tax_rate.list()
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
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerTaxRateListCreatedObj0, int
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
        if not isinstance(inclusive, type_utils.NotGiven):
            encode_query_param(
                _query,
                "inclusive",
                to_encodable(item=inclusive, dump_with=bool),
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
            path="/v1/tax_rates",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRateListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        tax_rate: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRate:
        """
        Retrieve a tax rate

        <p>Retrieves a tax rate with the given ID</p>

        GET /v1/tax_rates/{tax_rate}

        Args:
            expand: Specifies which fields in the response should be expanded.
            tax_rate: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax_rate.get(tax_rate="string")
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
            path=f"/v1/tax_rates/{tax_rate}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRate,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        display_name: str,
        inclusive: bool,
        percentage: float,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        country: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        jurisdiction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TaxRateCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "amusement_tax",
                    "communications_tax",
                    "gst",
                    "hst",
                    "igst",
                    "jct",
                    "lease_tax",
                    "pst",
                    "qst",
                    "retail_delivery_fee",
                    "rst",
                    "sales_tax",
                    "service_tax",
                    "vat",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRate:
        """
        Create a tax rate

        <p>Creates a new tax rate.</p>

        POST /v1/tax_rates

        Args:
            active: Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
            country: Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            description: An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
            expand: Specifies which fields in the response should be expanded.
            jurisdiction: The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            state: [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, "NY" for New York, United States.
            tax_type: The high-level tax type, such as `vat` or `sales_tax`.
            display_name: The display name of the tax rate, which will be shown to users.
            inclusive: This specifies if the tax rate is inclusive or exclusive.
            percentage: This represents the tax rate percent out of 100.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax_rate.create(
            display_name="string", inclusive=True, percentage=123.45
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "active": active,
                "country": country,
                "description": description,
                "expand": expand,
                "jurisdiction": jurisdiction,
                "metadata": metadata,
                "state": state,
                "tax_type": tax_type,
                "display_name": display_name,
                "inclusive": inclusive,
                "percentage": percentage,
            },
            dump_with=params._SerializerTaxRateCreateBody,
            style={
                "active": "form",
                "country": "form",
                "description": "form",
                "display_name": "form",
                "expand": "deepObject",
                "inclusive": "form",
                "jurisdiction": "form",
                "metadata": "deepObject",
                "percentage": "form",
                "state": "form",
                "tax_type": "form",
            },
            explode={
                "active": True,
                "country": True,
                "description": True,
                "display_name": True,
                "expand": True,
                "inclusive": True,
                "jurisdiction": True,
                "metadata": True,
                "percentage": True,
                "state": True,
                "tax_type": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/tax_rates",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxRate,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        tax_rate: str,
        data: typing.Union[
            typing.Optional[params.TaxRateUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRate:
        """
        Update a tax rate

        <p>Updates an existing tax rate.</p>

        POST /v1/tax_rates/{tax_rate}

        Args:
            data: TaxRateUpdateBody
            tax_rate: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax_rate.update(tax_rate="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTaxRateUpdateBody,
                style={
                    "active": "form",
                    "country": "form",
                    "description": "form",
                    "display_name": "form",
                    "expand": "deepObject",
                    "jurisdiction": "form",
                    "metadata": "deepObject",
                    "state": "form",
                    "tax_type": "form",
                },
                explode={
                    "active": True,
                    "country": True,
                    "description": True,
                    "display_name": True,
                    "expand": True,
                    "jurisdiction": True,
                    "metadata": True,
                    "state": True,
                    "tax_type": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/tax_rates/{tax_rate}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxRate,
            request_options=request_options or default_request_options(),
        )
