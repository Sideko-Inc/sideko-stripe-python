import pydantic
import typing


class BankConnectionsResourceTransactionResourceStatusTransitions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    posted_at: typing.Optional[int] = pydantic.Field(alias="posted_at", default=None)
    """
    Time at which this transaction posted. Measured in seconds since the Unix epoch.
    """
    void_at: typing.Optional[int] = pydantic.Field(alias="void_at", default=None)
    """
    Time at which this transaction was voided. Measured in seconds since the Unix epoch.
    """
