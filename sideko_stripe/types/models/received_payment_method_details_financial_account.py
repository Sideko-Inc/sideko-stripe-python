import pydantic
import typing_extensions


class ReceivedPaymentMethodDetailsFinancialAccount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    """
    The FinancialAccount ID.
    """
    network: typing_extensions.Literal["stripe"] = pydantic.Field(
        alias="network",
    )
    """
    The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`.
    """
