import pydantic
import typing


class BillingCreditGrantsResourceApplicablePrice(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the object.
    """
