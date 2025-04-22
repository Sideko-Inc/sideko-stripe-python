import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0
    """

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]

    tos_shown_and_accepted: typing_extensions.NotRequired[bool]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsP24Obj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
    tos_shown_and_accepted: typing.Optional[bool] = pydantic.Field(
        alias="tos_shown_and_accepted", default=None
    )
