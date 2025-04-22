import pydantic
import typing


class IssuingTransactionLodgingData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    check_in_at: typing.Optional[int] = pydantic.Field(
        alias="check_in_at", default=None
    )
    """
    The time of checking into the lodging.
    """
    nights: typing.Optional[int] = pydantic.Field(alias="nights", default=None)
    """
    The number of nights stayed at the lodging.
    """
