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


class CalculationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        calculation: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxCalculation:
        """
        Retrieve a Tax Calculation

        <p>Retrieves a Tax <code>Calculation</code> object, if the calculation hasn’t expired.</p>

        GET /v1/tax/calculations/{calculation}

        Args:
            expand: Specifies which fields in the response should be expanded.
            calculation: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.calculation.get(calculation="string")
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
            path=f"/v1/tax/calculations/{calculation}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TaxCalculation,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        currency: str,
        line_items: typing.List[params.TaxCalculationCreateBodyLineItemsItem],
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_details: typing.Union[
            typing.Optional[params.TaxCalculationCreateBodyCustomerDetails],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ship_from_details: typing.Union[
            typing.Optional[params.TaxCalculationCreateBodyShipFromDetails],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.TaxCalculationCreateBodyShippingCost],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_date: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxCalculation:
        """
        Create a Tax Calculation

        <p>Calculates tax based on the input and returns a Tax <code>Calculation</code> object.</p>

        POST /v1/tax/calculations

        Args:
            customer: The ID of an existing customer to use for this calculation. If provided, the customer's address and tax IDs are copied to `customer_details`.
            customer_details: Details about the customer, including address and tax IDs.
            expand: Specifies which fields in the response should be expanded.
            ship_from_details: Details about the address from which the goods are being shipped.
            shipping_cost: Shipping cost details to be used for the calculation.
            tax_date: Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            line_items: A list of items the customer is purchasing.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.calculation.create(currency="string", line_items=[{"amount": 123}])
        ```
        """
        _data = to_form_urlencoded(
            item={
                "customer": customer,
                "customer_details": customer_details,
                "expand": expand,
                "ship_from_details": ship_from_details,
                "shipping_cost": shipping_cost,
                "tax_date": tax_date,
                "currency": currency,
                "line_items": line_items,
            },
            dump_with=params._SerializerTaxCalculationCreateBody,
            style={
                "currency": "form",
                "customer": "form",
                "customer_details": "deepObject",
                "expand": "deepObject",
                "line_items": "deepObject",
                "ship_from_details": "deepObject",
                "shipping_cost": "deepObject",
                "tax_date": "form",
            },
            explode={
                "currency": True,
                "customer": True,
                "customer_details": True,
                "expand": True,
                "line_items": True,
                "ship_from_details": True,
                "shipping_cost": True,
                "tax_date": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/tax/calculations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TaxCalculation,
            request_options=request_options or default_request_options(),
        )


class AsyncCalculationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        calculation: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxCalculation:
        """
        Retrieve a Tax Calculation

        <p>Retrieves a Tax <code>Calculation</code> object, if the calculation hasn’t expired.</p>

        GET /v1/tax/calculations/{calculation}

        Args:
            expand: Specifies which fields in the response should be expanded.
            calculation: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.calculation.get(calculation="string")
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
            path=f"/v1/tax/calculations/{calculation}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TaxCalculation,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        currency: str,
        line_items: typing.List[params.TaxCalculationCreateBodyLineItemsItem],
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_details: typing.Union[
            typing.Optional[params.TaxCalculationCreateBodyCustomerDetails],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ship_from_details: typing.Union[
            typing.Optional[params.TaxCalculationCreateBodyShipFromDetails],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_cost: typing.Union[
            typing.Optional[params.TaxCalculationCreateBodyShippingCost],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_date: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxCalculation:
        """
        Create a Tax Calculation

        <p>Calculates tax based on the input and returns a Tax <code>Calculation</code> object.</p>

        POST /v1/tax/calculations

        Args:
            customer: The ID of an existing customer to use for this calculation. If provided, the customer's address and tax IDs are copied to `customer_details`.
            customer_details: Details about the customer, including address and tax IDs.
            expand: Specifies which fields in the response should be expanded.
            ship_from_details: Details about the address from which the goods are being shipped.
            shipping_cost: Shipping cost details to be used for the calculation.
            tax_date: Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            line_items: A list of items the customer is purchasing.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.calculation.create(
            currency="string", line_items=[{"amount": 123}]
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "customer": customer,
                "customer_details": customer_details,
                "expand": expand,
                "ship_from_details": ship_from_details,
                "shipping_cost": shipping_cost,
                "tax_date": tax_date,
                "currency": currency,
                "line_items": line_items,
            },
            dump_with=params._SerializerTaxCalculationCreateBody,
            style={
                "currency": "form",
                "customer": "form",
                "customer_details": "deepObject",
                "expand": "deepObject",
                "line_items": "deepObject",
                "ship_from_details": "deepObject",
                "shipping_cost": "deepObject",
                "tax_date": "form",
            },
            explode={
                "currency": True,
                "customer": True,
                "customer_details": True,
                "expand": True,
                "line_items": True,
                "ship_from_details": True,
                "shipping_cost": True,
                "tax_date": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/tax/calculations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TaxCalculation,
            request_options=request_options or default_request_options(),
        )
