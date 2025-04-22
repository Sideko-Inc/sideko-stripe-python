import pydantic
import typing
import typing_extensions

from .payment_method_update_body_card_networks import (
    PaymentMethodUpdateBodyCardNetworks,
    _SerializerPaymentMethodUpdateBodyCardNetworks,
)


class PaymentMethodUpdateBodyCard(typing_extensions.TypedDict):
    """
    If this is a `card` PaymentMethod, this hash contains the user's card details.
    """

    exp_month: typing_extensions.NotRequired[int]

    exp_year: typing_extensions.NotRequired[int]

    networks: typing_extensions.NotRequired[PaymentMethodUpdateBodyCardNetworks]


class _SerializerPaymentMethodUpdateBodyCard(pydantic.BaseModel):
    """
    Serializer for PaymentMethodUpdateBodyCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    exp_month: typing.Optional[int] = pydantic.Field(alias="exp_month", default=None)
    exp_year: typing.Optional[int] = pydantic.Field(alias="exp_year", default=None)
    networks: typing.Optional[_SerializerPaymentMethodUpdateBodyCardNetworks] = (
        pydantic.Field(alias="networks", default=None)
    )
