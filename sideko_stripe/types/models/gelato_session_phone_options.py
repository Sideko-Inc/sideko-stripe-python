import pydantic
import typing


class GelatoSessionPhoneOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    require_verification: typing.Optional[bool] = pydantic.Field(
        alias="require_verification", default=None
    )
    """
    Request one time password verification of `provided_details.phone`.
    """
