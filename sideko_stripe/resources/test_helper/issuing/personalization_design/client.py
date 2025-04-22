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


class PersonalizationDesignClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def activate(
        self,
        *,
        personalization_design: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingPersonalizationDesignActivateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Activate a testmode personalization design

        <p>Updates the <code>status</code> of the specified testmode personalization design object to <code>active</code>.</p>

        POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate

        Args:
            data: TestHelperIssuingPersonalizationDesignActivateBody
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.personalization_design.activate(
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
                dump_with=params._SerializerTestHelperIssuingPersonalizationDesignActivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    def deactivate(
        self,
        *,
        personalization_design: str,
        data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingPersonalizationDesignDeactivateBody
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Deactivate a testmode personalization design

        <p>Updates the <code>status</code> of the specified testmode personalization design object to <code>inactive</code>.</p>

        POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate

        Args:
            data: TestHelperIssuingPersonalizationDesignDeactivateBody
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.personalization_design.deactivate(
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
                dump_with=params._SerializerTestHelperIssuingPersonalizationDesignDeactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    def reject(
        self,
        *,
        personalization_design: str,
        rejection_reasons: params.TestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Reject a testmode personalization design

        <p>Updates the <code>status</code> of the specified testmode personalization design object to <code>rejected</code>.</p>

        POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject

        Args:
            expand: Specifies which fields in the response should be expanded.
            personalization_design: str
            rejection_reasons: The reason(s) the personalization design was rejected.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.personalization_design.reject(
            personalization_design="string", rejection_reasons={}
        )
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "rejection_reasons": rejection_reasons},
            dump_with=params._SerializerTestHelperIssuingPersonalizationDesignRejectBody,
            style={"expand": "deepObject", "rejection_reasons": "deepObject"},
            explode={"expand": True, "rejection_reasons": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )


class AsyncPersonalizationDesignClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def activate(
        self,
        *,
        personalization_design: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingPersonalizationDesignActivateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Activate a testmode personalization design

        <p>Updates the <code>status</code> of the specified testmode personalization design object to <code>active</code>.</p>

        POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate

        Args:
            data: TestHelperIssuingPersonalizationDesignActivateBody
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.personalization_design.activate(
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
                dump_with=params._SerializerTestHelperIssuingPersonalizationDesignActivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    async def deactivate(
        self,
        *,
        personalization_design: str,
        data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingPersonalizationDesignDeactivateBody
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Deactivate a testmode personalization design

        <p>Updates the <code>status</code> of the specified testmode personalization design object to <code>inactive</code>.</p>

        POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate

        Args:
            data: TestHelperIssuingPersonalizationDesignDeactivateBody
            personalization_design: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.personalization_design.deactivate(
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
                dump_with=params._SerializerTestHelperIssuingPersonalizationDesignDeactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )

    async def reject(
        self,
        *,
        personalization_design: str,
        rejection_reasons: params.TestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingPersonalizationDesign:
        """
        Reject a testmode personalization design

        <p>Updates the <code>status</code> of the specified testmode personalization design object to <code>rejected</code>.</p>

        POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject

        Args:
            expand: Specifies which fields in the response should be expanded.
            personalization_design: str
            rejection_reasons: The reason(s) the personalization design was rejected.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.personalization_design.reject(
            personalization_design="string", rejection_reasons={}
        )
        ```
        """
        models.IssuingPersonalizationDesign.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "rejection_reasons": rejection_reasons},
            dump_with=params._SerializerTestHelperIssuingPersonalizationDesignRejectBody,
            style={"expand": "deepObject", "rejection_reasons": "deepObject"},
            explode={"expand": True, "rejection_reasons": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingPersonalizationDesign,
            request_options=request_options or default_request_options(),
        )
