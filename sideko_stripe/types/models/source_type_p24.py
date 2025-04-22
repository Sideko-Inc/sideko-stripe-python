import pydantic
import typing


class SourceTypeP24(pydantic.BaseModel):
    """
    SourceTypeP24
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
