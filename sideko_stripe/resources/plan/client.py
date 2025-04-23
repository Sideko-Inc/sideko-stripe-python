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


class PlanClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, plan: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedPlan:
        """
        Delete a plan

        <p>Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.</p>

        DELETE /v1/plans/{plan}

        Args:
            plan: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.plan.delete(plan="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/plans/{plan}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedPlan,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PlanListCreatedObj0, int]],
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
        product: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PlanListResponse:
        """
        List all plans

        <p>Returns a list of your plans.</p>

        GET /v1/plans

        Args:
            active: Only return plans that are active or inactive (e.g., pass `false` to list all inactive plans).
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            product: Only return plans for the given product.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.plan.list()
        ```
        """
        models.PlanListResponse.model_rebuild(_types_namespace=models._types_namespace)
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
                    dump_with=typing.Union[params._SerializerPlanListCreatedObj0, int],
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
        if not isinstance(product, type_utils.NotGiven):
            encode_query_param(
                _query,
                "product",
                to_encodable(item=product, dump_with=str),
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
            path="/v1/plans",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PlanListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        plan: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Plan:
        """
        Retrieve a plan

        <p>Retrieves the plan with the given ID.</p>

        GET /v1/plans/{plan}

        Args:
            expand: Specifies which fields in the response should be expanded.
            plan: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.plan.get(plan="string")
        ```
        """
        models.Plan.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/plans/{plan}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Plan,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        currency: str,
        interval: typing_extensions.Literal["day", "month", "week", "year"],
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount_decimal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_scheme: typing.Union[
            typing.Optional[typing_extensions.Literal["per_unit", "tiered"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Union[params.PlanCreateBodyMetadataObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        meter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        nickname: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product: typing.Union[
            typing.Optional[typing.Union[params.PlanCreateBodyProductObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers: typing.Union[
            typing.Optional[typing.List[params.PlanCreateBodyTiersItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers_mode: typing.Union[
            typing.Optional[typing_extensions.Literal["graduated", "volume"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transform_usage: typing.Union[
            typing.Optional[params.PlanCreateBodyTransformUsage], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        trial_period_days: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        usage_type: typing.Union[
            typing.Optional[typing_extensions.Literal["licensed", "metered"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Plan:
        """
        Create a plan

        <p>You can now model subscriptions more flexibly using the <a href="#prices">Prices API</a>. It replaces the Plans API and is backwards compatible to simplify your migration.</p>

        POST /v1/plans

        Args:
            active: Whether the plan is currently available for new subscriptions. Defaults to `true`.
            amount: A positive integer in cents (or local equivalent) (or 0 for a free plan) representing how much to charge on a recurring basis.
            amount_decimal: Same as `amount`, but accepts a decimal value with at most 12 decimal places. Only one of `amount` and `amount_decimal` can be set.
            billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
            expand: Specifies which fields in the response should be expanded.
            id: An identifier randomly generated by Stripe. Used to identify this plan when subscribing a customer. You can optionally override this ID, but the ID must be unique across all plans in your Stripe account. You can, however, use the same plan ID in both live and test modes.
            interval_count: The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            meter: The meter tracking the usage of a metered price
            nickname: A brief description of the plan, hidden from customers.
            product: typing.Union[PlanCreateBodyProductObj0, str]
            tiers: Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
            tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
            transform_usage: Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
            trial_period_days: Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
            usage_type: Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            interval: Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.plan.create(currency="string", interval="day")
        ```
        """
        models.Plan.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "amount": amount,
                "amount_decimal": amount_decimal,
                "billing_scheme": billing_scheme,
                "expand": expand,
                "id": id,
                "interval_count": interval_count,
                "metadata": metadata,
                "meter": meter,
                "nickname": nickname,
                "product": product,
                "tiers": tiers,
                "tiers_mode": tiers_mode,
                "transform_usage": transform_usage,
                "trial_period_days": trial_period_days,
                "usage_type": usage_type,
                "currency": currency,
                "interval": interval,
            },
            dump_with=params._SerializerPlanCreateBody,
            style={
                "active": "form",
                "amount": "form",
                "amount_decimal": "form",
                "billing_scheme": "form",
                "currency": "form",
                "expand": "deepObject",
                "id": "form",
                "interval": "form",
                "interval_count": "form",
                "metadata": "deepObject",
                "meter": "form",
                "nickname": "form",
                "product": "deepObject",
                "tiers": "deepObject",
                "tiers_mode": "form",
                "transform_usage": "deepObject",
                "trial_period_days": "form",
                "usage_type": "form",
            },
            explode={
                "active": True,
                "amount": True,
                "amount_decimal": True,
                "billing_scheme": True,
                "currency": True,
                "expand": True,
                "id": True,
                "interval": True,
                "interval_count": True,
                "metadata": True,
                "meter": True,
                "nickname": True,
                "product": True,
                "tiers": True,
                "tiers_mode": True,
                "transform_usage": True,
                "trial_period_days": True,
                "usage_type": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/plans",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Plan,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        plan: str,
        data: typing.Union[
            typing.Optional[params.PlanUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Plan:
        """
        Update a plan

        <p>Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.</p>

        POST /v1/plans/{plan}

        Args:
            data: PlanUpdateBody
            plan: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.plan.update(plan="string")
        ```
        """
        models.Plan.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPlanUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "nickname": "form",
                    "product": "form",
                    "trial_period_days": "form",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "metadata": True,
                    "nickname": True,
                    "product": True,
                    "trial_period_days": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/plans/{plan}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Plan,
            request_options=request_options or default_request_options(),
        )


class AsyncPlanClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, plan: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedPlan:
        """
        Delete a plan

        <p>Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.</p>

        DELETE /v1/plans/{plan}

        Args:
            plan: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.plan.delete(plan="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/plans/{plan}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedPlan,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PlanListCreatedObj0, int]],
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
        product: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PlanListResponse:
        """
        List all plans

        <p>Returns a list of your plans.</p>

        GET /v1/plans

        Args:
            active: Only return plans that are active or inactive (e.g., pass `false` to list all inactive plans).
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            product: Only return plans for the given product.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.plan.list()
        ```
        """
        models.PlanListResponse.model_rebuild(_types_namespace=models._types_namespace)
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
                    dump_with=typing.Union[params._SerializerPlanListCreatedObj0, int],
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
        if not isinstance(product, type_utils.NotGiven):
            encode_query_param(
                _query,
                "product",
                to_encodable(item=product, dump_with=str),
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
            path="/v1/plans",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PlanListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        plan: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Plan:
        """
        Retrieve a plan

        <p>Retrieves the plan with the given ID.</p>

        GET /v1/plans/{plan}

        Args:
            expand: Specifies which fields in the response should be expanded.
            plan: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.plan.get(plan="string")
        ```
        """
        models.Plan.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/plans/{plan}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Plan,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        currency: str,
        interval: typing_extensions.Literal["day", "month", "week", "year"],
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount_decimal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_scheme: typing.Union[
            typing.Optional[typing_extensions.Literal["per_unit", "tiered"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        interval_count: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Union[params.PlanCreateBodyMetadataObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        meter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        nickname: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product: typing.Union[
            typing.Optional[typing.Union[params.PlanCreateBodyProductObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers: typing.Union[
            typing.Optional[typing.List[params.PlanCreateBodyTiersItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers_mode: typing.Union[
            typing.Optional[typing_extensions.Literal["graduated", "volume"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transform_usage: typing.Union[
            typing.Optional[params.PlanCreateBodyTransformUsage], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        trial_period_days: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        usage_type: typing.Union[
            typing.Optional[typing_extensions.Literal["licensed", "metered"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Plan:
        """
        Create a plan

        <p>You can now model subscriptions more flexibly using the <a href="#prices">Prices API</a>. It replaces the Plans API and is backwards compatible to simplify your migration.</p>

        POST /v1/plans

        Args:
            active: Whether the plan is currently available for new subscriptions. Defaults to `true`.
            amount: A positive integer in cents (or local equivalent) (or 0 for a free plan) representing how much to charge on a recurring basis.
            amount_decimal: Same as `amount`, but accepts a decimal value with at most 12 decimal places. Only one of `amount` and `amount_decimal` can be set.
            billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
            expand: Specifies which fields in the response should be expanded.
            id: An identifier randomly generated by Stripe. Used to identify this plan when subscribing a customer. You can optionally override this ID, but the ID must be unique across all plans in your Stripe account. You can, however, use the same plan ID in both live and test modes.
            interval_count: The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            meter: The meter tracking the usage of a metered price
            nickname: A brief description of the plan, hidden from customers.
            product: typing.Union[PlanCreateBodyProductObj0, str]
            tiers: Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
            tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
            transform_usage: Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
            trial_period_days: Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
            usage_type: Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            interval: Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.plan.create(currency="string", interval="day")
        ```
        """
        models.Plan.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "amount": amount,
                "amount_decimal": amount_decimal,
                "billing_scheme": billing_scheme,
                "expand": expand,
                "id": id,
                "interval_count": interval_count,
                "metadata": metadata,
                "meter": meter,
                "nickname": nickname,
                "product": product,
                "tiers": tiers,
                "tiers_mode": tiers_mode,
                "transform_usage": transform_usage,
                "trial_period_days": trial_period_days,
                "usage_type": usage_type,
                "currency": currency,
                "interval": interval,
            },
            dump_with=params._SerializerPlanCreateBody,
            style={
                "active": "form",
                "amount": "form",
                "amount_decimal": "form",
                "billing_scheme": "form",
                "currency": "form",
                "expand": "deepObject",
                "id": "form",
                "interval": "form",
                "interval_count": "form",
                "metadata": "deepObject",
                "meter": "form",
                "nickname": "form",
                "product": "deepObject",
                "tiers": "deepObject",
                "tiers_mode": "form",
                "transform_usage": "deepObject",
                "trial_period_days": "form",
                "usage_type": "form",
            },
            explode={
                "active": True,
                "amount": True,
                "amount_decimal": True,
                "billing_scheme": True,
                "currency": True,
                "expand": True,
                "id": True,
                "interval": True,
                "interval_count": True,
                "metadata": True,
                "meter": True,
                "nickname": True,
                "product": True,
                "tiers": True,
                "tiers_mode": True,
                "transform_usage": True,
                "trial_period_days": True,
                "usage_type": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/plans",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Plan,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        plan: str,
        data: typing.Union[
            typing.Optional[params.PlanUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Plan:
        """
        Update a plan

        <p>Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.</p>

        POST /v1/plans/{plan}

        Args:
            data: PlanUpdateBody
            plan: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.plan.update(plan="string")
        ```
        """
        models.Plan.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPlanUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "nickname": "form",
                    "product": "form",
                    "trial_period_days": "form",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "metadata": True,
                    "nickname": True,
                    "product": True,
                    "trial_period_days": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/plans/{plan}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Plan,
            request_options=request_options or default_request_options(),
        )
