import pydantic
import typing


class SourceMandateNotificationBacsDebitData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last 4 digits of the account number associated with the debit.
    """
