import pydantic
import typing
import typing_extensions


class SetupIntentCreateBodyPaymentMethodDataNaverPay(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataNaverPay
    """

    funding: typing_extensions.NotRequired[typing_extensions.Literal["card", "points"]]


class _SerializerSetupIntentCreateBodyPaymentMethodDataNaverPay(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataNaverPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    funding: typing.Optional[typing_extensions.Literal["card", "points"]] = (
        pydantic.Field(alias="funding", default=None)
    )
