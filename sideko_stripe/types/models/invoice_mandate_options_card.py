import pydantic
import typing
import typing_extensions


class InvoiceMandateOptionsCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    Amount to be charged for future payments.
    """
    amount_type: typing.Optional[typing_extensions.Literal["fixed", "maximum"]] = (
        pydantic.Field(alias="amount_type", default=None)
    )
    """
    One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    A description of the mandate or subscription that is meant to be displayed to the customer.
    """
