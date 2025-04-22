import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires
    """

    cb_avalgo: typing_extensions.Required[
        typing_extensions.Literal["0", "1", "2", "3", "4", "A"]
    ]

    cb_exemption: typing_extensions.NotRequired[str]

    cb_score: typing_extensions.NotRequired[int]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0ThreeDSecureNetworkOptionsCartesBancaires handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cb_avalgo: typing_extensions.Literal["0", "1", "2", "3", "4", "A"] = pydantic.Field(
        alias="cb_avalgo",
    )
    cb_exemption: typing.Optional[str] = pydantic.Field(
        alias="cb_exemption", default=None
    )
    cb_score: typing.Optional[int] = pydantic.Field(alias="cb_score", default=None)
