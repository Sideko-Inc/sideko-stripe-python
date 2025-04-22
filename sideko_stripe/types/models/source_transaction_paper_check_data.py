import pydantic
import typing


class SourceTransactionPaperCheckData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available_at: typing.Optional[str] = pydantic.Field(
        alias="available_at", default=None
    )
    """
    Time at which the deposited funds will be available for use. Measured in seconds since the Unix epoch.
    """
    invoices: typing.Optional[str] = pydantic.Field(alias="invoices", default=None)
    """
    Comma-separated list of invoice IDs associated with the paper check.
    """
