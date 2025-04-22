import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0
    """

    reference: typing_extensions.NotRequired[typing.Union[str, str]]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsSwishObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="reference", default=None
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
