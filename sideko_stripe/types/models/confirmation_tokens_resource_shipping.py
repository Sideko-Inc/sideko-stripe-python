import pydantic
import typing

from .address import Address


class ConfirmationTokensResourceShipping(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: Address = pydantic.Field(
        alias="address",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Recipient name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Recipient phone (including extension).
    """
