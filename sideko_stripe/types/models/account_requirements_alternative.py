import pydantic
import typing


class AccountRequirementsAlternative(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    alternative_fields_due: typing.List[str] = pydantic.Field(
        alias="alternative_fields_due",
    )
    """
    Fields that can be provided to satisfy all fields in `original_fields_due`.
    """
    original_fields_due: typing.List[str] = pydantic.Field(
        alias="original_fields_due",
    )
    """
    Fields that are due and can be satisfied by providing all fields in `alternative_fields_due`.
    """
