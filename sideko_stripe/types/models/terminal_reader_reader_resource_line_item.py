import pydantic


class TerminalReaderReaderResourceLineItem(pydantic.BaseModel):
    """
    Represents a line item to be displayed on the reader
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount of the line item. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    description: str = pydantic.Field(
        alias="description",
    )
    """
    Description of the line item.
    """
    quantity: int = pydantic.Field(
        alias="quantity",
    )
    """
    The quantity of the line item.
    """
