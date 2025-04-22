import pydantic
import typing
import typing_extensions

from .payment_method_create_body_card_obj0_networks import (
    PaymentMethodCreateBodyCardObj0Networks,
    _SerializerPaymentMethodCreateBodyCardObj0Networks,
)


class PaymentMethodCreateBodyCardObj0(typing_extensions.TypedDict):
    """
    PaymentMethodCreateBodyCardObj0
    """

    cvc: typing_extensions.NotRequired[str]

    exp_month: typing_extensions.Required[int]

    exp_year: typing_extensions.Required[int]

    networks: typing_extensions.NotRequired[PaymentMethodCreateBodyCardObj0Networks]

    number: typing_extensions.Required[str]


class _SerializerPaymentMethodCreateBodyCardObj0(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cvc: typing.Optional[str] = pydantic.Field(alias="cvc", default=None)
    exp_month: int = pydantic.Field(
        alias="exp_month",
    )
    exp_year: int = pydantic.Field(
        alias="exp_year",
    )
    networks: typing.Optional[_SerializerPaymentMethodCreateBodyCardObj0Networks] = (
        pydantic.Field(alias="networks", default=None)
    )
    number: str = pydantic.Field(
        alias="number",
    )
