import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]

    preferred_locale: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "cs-CZ",
            "da-DK",
            "de-AT",
            "de-DE",
            "de-LU",
            "el-GR",
            "en-GB",
            "en-US",
            "es-ES",
            "fi-FI",
            "fr-BE",
            "fr-FR",
            "fr-LU",
            "hu-HU",
            "it-IT",
            "nl-BE",
            "nl-NL",
            "pl-PL",
            "pt-PT",
            "sk-SK",
            "sv-SE",
        ]
    ]

    reference: typing_extensions.NotRequired[str]

    risk_correlation_id: typing_extensions.NotRequired[str]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsPaypalObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[typing_extensions.Literal["manual"]] = (
        pydantic.Field(alias="capture_method", default=None)
    )
    preferred_locale: typing.Optional[
        typing_extensions.Literal[
            "cs-CZ",
            "da-DK",
            "de-AT",
            "de-DE",
            "de-LU",
            "el-GR",
            "en-GB",
            "en-US",
            "es-ES",
            "fi-FI",
            "fr-BE",
            "fr-FR",
            "fr-LU",
            "hu-HU",
            "it-IT",
            "nl-BE",
            "nl-NL",
            "pl-PL",
            "pt-PT",
            "sk-SK",
            "sv-SE",
        ]
    ] = pydantic.Field(alias="preferred_locale", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    risk_correlation_id: typing.Optional[str] = pydantic.Field(
        alias="risk_correlation_id", default=None
    )
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
