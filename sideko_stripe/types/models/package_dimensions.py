import pydantic


class PackageDimensions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    height: float = pydantic.Field(
        alias="height",
    )
    """
    Height, in inches.
    """
    length: float = pydantic.Field(
        alias="length",
    )
    """
    Length, in inches.
    """
    weight: float = pydantic.Field(
        alias="weight",
    )
    """
    Weight, in ounces.
    """
    width: float = pydantic.Field(
        alias="width",
    )
    """
    Width, in inches.
    """
