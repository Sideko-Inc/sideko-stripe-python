import pydantic
import typing

from .address import Address


class PaymentMethodCardWalletMasterpass(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_address: typing.Optional[Address] = pydantic.Field(
        alias="billing_address", default=None
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
    """
    shipping_address: typing.Optional[Address] = pydantic.Field(
        alias="shipping_address", default=None
    )
