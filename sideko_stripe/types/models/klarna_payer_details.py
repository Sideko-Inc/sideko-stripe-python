import pydantic
import typing

from .klarna_address import KlarnaAddress


class KlarnaPayerDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[KlarnaAddress] = pydantic.Field(
        alias="address", default=None
    )
