import pydantic
import typing


class SourceMandateNotificationSepaDebitData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    creditor_identifier: typing.Optional[str] = pydantic.Field(
        alias="creditor_identifier", default=None
    )
    """
    SEPA creditor ID.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last 4 digits of the account number associated with the debit.
    """
    mandate_reference: typing.Optional[str] = pydantic.Field(
        alias="mandate_reference", default=None
    )
    """
    Mandate reference associated with the debit.
    """
