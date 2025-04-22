import pydantic
import typing


class CountrySpecVerificationFieldDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    additional: typing.List[str] = pydantic.Field(
        alias="additional",
    )
    """
    Additional fields which are only required for some users.
    """
    minimum: typing.List[str] = pydantic.Field(
        alias="minimum",
    )
    """
    Fields which every account must eventually provide.
    """
