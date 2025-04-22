import typing
import typing_extensions

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.resources.test_helper.issuing.authorization.fraud_challenges import (
    AsyncFraudChallengesClient,
    FraudChallengesClient,
)
from sideko_stripe.types import models, params


class AuthorizationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.fraud_challenges = FraudChallengesClient(base_client=self._base_client)

    def create(
        self,
        *,
        card: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount_details: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationCreateBodyAmountDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        authorization_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "chip", "contactless", "keyed_in", "online", "swipe"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fleet: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCreateBodyFleet],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        fuel: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCreateBodyFuel],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        is_amount_controllable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationCreateBodyMerchantData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        network_data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCreateBodyNetworkData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        verification_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationCreateBodyVerificationData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wallet: typing.Union[
            typing.Optional[
                typing_extensions.Literal["apple_pay", "google_pay", "samsung_pay"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Create a test-mode authorization

        <p>Create a test-mode authorization.</p>

        POST /v1/test_helpers/issuing/authorizations

        Args:
            amount: The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card's currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            amount_details: Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            authorization_method: How the card details were provided. Defaults to online.
            currency: The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            expand: Specifies which fields in the response should be expanded.
            fleet: Fleet-specific information for authorizations using Fleet cards.
            fuel: Information about fuel that was purchased with this transaction.
            is_amount_controllable: If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
            merchant_amount: The total amount to attempt to authorize. This amount is in the provided merchant currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            merchant_currency: The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
            network_data: Details about the authorization, such as identifiers, set by the card network.
            verification_data: Verifications that Stripe performed on information that the cardholder provided to the merchant.
            wallet: The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.
            card: Card associated with this authorization.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.authorization.create(card="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "amount_details": amount_details,
                "authorization_method": authorization_method,
                "currency": currency,
                "expand": expand,
                "fleet": fleet,
                "fuel": fuel,
                "is_amount_controllable": is_amount_controllable,
                "merchant_amount": merchant_amount,
                "merchant_currency": merchant_currency,
                "merchant_data": merchant_data,
                "network_data": network_data,
                "verification_data": verification_data,
                "wallet": wallet,
                "card": card,
            },
            dump_with=params._SerializerTestHelperIssuingAuthorizationCreateBody,
            style={
                "amount": "form",
                "amount_details": "deepObject",
                "authorization_method": "form",
                "card": "form",
                "currency": "form",
                "expand": "deepObject",
                "fleet": "deepObject",
                "fuel": "deepObject",
                "is_amount_controllable": "form",
                "merchant_amount": "form",
                "merchant_currency": "form",
                "merchant_data": "deepObject",
                "network_data": "deepObject",
                "verification_data": "deepObject",
                "wallet": "form",
            },
            explode={
                "amount": True,
                "amount_details": True,
                "authorization_method": True,
                "card": True,
                "currency": True,
                "expand": True,
                "fleet": True,
                "fuel": True,
                "is_amount_controllable": True,
                "merchant_amount": True,
                "merchant_currency": True,
                "merchant_data": True,
                "network_data": True,
                "verification_data": True,
                "wallet": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/authorizations",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def capture(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCaptureBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Capture a test-mode authorization

        <p>Capture a test-mode authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/capture

        Args:
            data: TestHelperIssuingAuthorizationCaptureBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.authorization.capture(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingAuthorizationCaptureBody,
                style={
                    "capture_amount": "form",
                    "close_authorization": "form",
                    "expand": "deepObject",
                    "purchase_details": "deepObject",
                },
                explode={
                    "capture_amount": True,
                    "close_authorization": True,
                    "expand": True,
                    "purchase_details": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/capture",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def expire(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationExpireBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Expire a test-mode authorization

        <p>Expire a test-mode Authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/expire

        Args:
            data: TestHelperIssuingAuthorizationExpireBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.authorization.expire(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingAuthorizationExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def finalize_amount(
        self,
        *,
        authorization: str,
        final_amount: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fleet: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationFinalizeAmountBodyFleet
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        fuel: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationFinalizeAmountBodyFuel
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Finalize a test-mode authorization's amount

        <p>Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount

        Args:
            expand: Specifies which fields in the response should be expanded.
            fleet: Fleet-specific information for authorizations using Fleet cards.
            fuel: Information about fuel that was purchased with this transaction.
            authorization: str
            final_amount: The final authorization amount that will be captured by the merchant. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.authorization.finalize_amount(
            authorization="string", final_amount=123
        )
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "fleet": fleet,
                "fuel": fuel,
                "final_amount": final_amount,
            },
            dump_with=params._SerializerTestHelperIssuingAuthorizationFinalizeAmountBody,
            style={
                "expand": "deepObject",
                "final_amount": "form",
                "fleet": "deepObject",
                "fuel": "deepObject",
            },
            explode={"expand": True, "final_amount": True, "fleet": True, "fuel": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def increment(
        self,
        *,
        authorization: str,
        increment_amount: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_amount_controllable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Increment a test-mode authorization

        <p>Increment a test-mode Authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/increment

        Args:
            expand: Specifies which fields in the response should be expanded.
            is_amount_controllable: If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
            authorization: str
            increment_amount: The amount to increment the authorization by. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.authorization.increment(
            authorization="string", increment_amount=123
        )
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "is_amount_controllable": is_amount_controllable,
                "increment_amount": increment_amount,
            },
            dump_with=params._SerializerTestHelperIssuingAuthorizationIncrementBody,
            style={
                "expand": "deepObject",
                "increment_amount": "form",
                "is_amount_controllable": "form",
            },
            explode={
                "expand": True,
                "increment_amount": True,
                "is_amount_controllable": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/increment",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def reverse(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationReverseBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Reverse a test-mode authorization

        <p>Reverse a test-mode Authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/reverse

        Args:
            data: TestHelperIssuingAuthorizationReverseBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.authorization.reverse(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingAuthorizationReverseBody,
                style={"expand": "deepObject", "reverse_amount": "form"},
                explode={"expand": True, "reverse_amount": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/reverse",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )


class AsyncAuthorizationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.fraud_challenges = AsyncFraudChallengesClient(
            base_client=self._base_client
        )

    async def create(
        self,
        *,
        card: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount_details: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationCreateBodyAmountDetails
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        authorization_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "chip", "contactless", "keyed_in", "online", "swipe"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fleet: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCreateBodyFleet],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        fuel: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCreateBodyFuel],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        is_amount_controllable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        merchant_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationCreateBodyMerchantData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        network_data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCreateBodyNetworkData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        verification_data: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationCreateBodyVerificationData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        wallet: typing.Union[
            typing.Optional[
                typing_extensions.Literal["apple_pay", "google_pay", "samsung_pay"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Create a test-mode authorization

        <p>Create a test-mode authorization.</p>

        POST /v1/test_helpers/issuing/authorizations

        Args:
            amount: The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card's currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            amount_details: Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            authorization_method: How the card details were provided. Defaults to online.
            currency: The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            expand: Specifies which fields in the response should be expanded.
            fleet: Fleet-specific information for authorizations using Fleet cards.
            fuel: Information about fuel that was purchased with this transaction.
            is_amount_controllable: If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
            merchant_amount: The total amount to attempt to authorize. This amount is in the provided merchant currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            merchant_currency: The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
            network_data: Details about the authorization, such as identifiers, set by the card network.
            verification_data: Verifications that Stripe performed on information that the cardholder provided to the merchant.
            wallet: The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.
            card: Card associated with this authorization.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.authorization.create(card="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "amount_details": amount_details,
                "authorization_method": authorization_method,
                "currency": currency,
                "expand": expand,
                "fleet": fleet,
                "fuel": fuel,
                "is_amount_controllable": is_amount_controllable,
                "merchant_amount": merchant_amount,
                "merchant_currency": merchant_currency,
                "merchant_data": merchant_data,
                "network_data": network_data,
                "verification_data": verification_data,
                "wallet": wallet,
                "card": card,
            },
            dump_with=params._SerializerTestHelperIssuingAuthorizationCreateBody,
            style={
                "amount": "form",
                "amount_details": "deepObject",
                "authorization_method": "form",
                "card": "form",
                "currency": "form",
                "expand": "deepObject",
                "fleet": "deepObject",
                "fuel": "deepObject",
                "is_amount_controllable": "form",
                "merchant_amount": "form",
                "merchant_currency": "form",
                "merchant_data": "deepObject",
                "network_data": "deepObject",
                "verification_data": "deepObject",
                "wallet": "form",
            },
            explode={
                "amount": True,
                "amount_details": True,
                "authorization_method": True,
                "card": True,
                "currency": True,
                "expand": True,
                "fleet": True,
                "fuel": True,
                "is_amount_controllable": True,
                "merchant_amount": True,
                "merchant_currency": True,
                "merchant_data": True,
                "network_data": True,
                "verification_data": True,
                "wallet": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/test_helpers/issuing/authorizations",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def capture(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationCaptureBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Capture a test-mode authorization

        <p>Capture a test-mode authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/capture

        Args:
            data: TestHelperIssuingAuthorizationCaptureBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.authorization.capture(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingAuthorizationCaptureBody,
                style={
                    "capture_amount": "form",
                    "close_authorization": "form",
                    "expand": "deepObject",
                    "purchase_details": "deepObject",
                },
                explode={
                    "capture_amount": True,
                    "close_authorization": True,
                    "expand": True,
                    "purchase_details": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/capture",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def expire(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationExpireBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Expire a test-mode authorization

        <p>Expire a test-mode Authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/expire

        Args:
            data: TestHelperIssuingAuthorizationExpireBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.authorization.expire(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingAuthorizationExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def finalize_amount(
        self,
        *,
        authorization: str,
        final_amount: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fleet: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationFinalizeAmountBodyFleet
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        fuel: typing.Union[
            typing.Optional[
                params.TestHelperIssuingAuthorizationFinalizeAmountBodyFuel
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Finalize a test-mode authorization's amount

        <p>Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount

        Args:
            expand: Specifies which fields in the response should be expanded.
            fleet: Fleet-specific information for authorizations using Fleet cards.
            fuel: Information about fuel that was purchased with this transaction.
            authorization: str
            final_amount: The final authorization amount that will be captured by the merchant. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.authorization.finalize_amount(
            authorization="string", final_amount=123
        )
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "fleet": fleet,
                "fuel": fuel,
                "final_amount": final_amount,
            },
            dump_with=params._SerializerTestHelperIssuingAuthorizationFinalizeAmountBody,
            style={
                "expand": "deepObject",
                "final_amount": "form",
                "fleet": "deepObject",
                "fuel": "deepObject",
            },
            explode={"expand": True, "final_amount": True, "fleet": True, "fuel": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def increment(
        self,
        *,
        authorization: str,
        increment_amount: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_amount_controllable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Increment a test-mode authorization

        <p>Increment a test-mode Authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/increment

        Args:
            expand: Specifies which fields in the response should be expanded.
            is_amount_controllable: If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
            authorization: str
            increment_amount: The amount to increment the authorization by. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.authorization.increment(
            authorization="string", increment_amount=123
        )
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "is_amount_controllable": is_amount_controllable,
                "increment_amount": increment_amount,
            },
            dump_with=params._SerializerTestHelperIssuingAuthorizationIncrementBody,
            style={
                "expand": "deepObject",
                "increment_amount": "form",
                "is_amount_controllable": "form",
            },
            explode={
                "expand": True,
                "increment_amount": True,
                "is_amount_controllable": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/increment",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def reverse(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingAuthorizationReverseBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Reverse a test-mode authorization

        <p>Reverse a test-mode Authorization.</p>

        POST /v1/test_helpers/issuing/authorizations/{authorization}/reverse

        Args:
            data: TestHelperIssuingAuthorizationReverseBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.authorization.reverse(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingAuthorizationReverseBody,
                style={"expand": "deepObject", "reverse_amount": "form"},
                explode={"expand": True, "reverse_amount": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/authorizations/{authorization}/reverse",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )
