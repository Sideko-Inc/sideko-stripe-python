import pydantic
import typing_extensions


class OutboundTransfersPaymentMethodDetailsFinancialAccount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    """
    Token of the FinancialAccount.
    """
    network: typing_extensions.Literal["stripe"] = pydantic.Field(
        alias="network",
    )
    """
    The rails used to send funds.
    """
