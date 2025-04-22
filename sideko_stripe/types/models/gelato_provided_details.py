import pydantic
import typing


class GelatoProvidedDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Email of user being verified
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Phone number of user being verified
    """
