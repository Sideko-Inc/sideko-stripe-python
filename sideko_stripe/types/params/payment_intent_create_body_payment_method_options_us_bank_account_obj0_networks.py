import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0Networks(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0Networks
    """

    requested: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["ach", "us_domestic_wire"]]
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0Networks(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0Networks handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[
        typing.List[typing_extensions.Literal["ach", "us_domestic_wire"]]
    ] = pydantic.Field(alias="requested", default=None)
