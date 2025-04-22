import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks
    """

    requested: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["ach", "us_domestic_wire"]]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[
        typing.List[typing_extensions.Literal["ach", "us_domestic_wire"]]
    ] = pydantic.Field(alias="requested", default=None)
