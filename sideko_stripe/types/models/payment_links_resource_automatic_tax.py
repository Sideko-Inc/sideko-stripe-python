import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .connect_account_reference import ConnectAccountReference


class PaymentLinksResourceAutomaticTax(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    If `true`, tax will be calculated automatically using the customer's location.
    """
    liability: typing.Optional["ConnectAccountReference"] = pydantic.Field(
        alias="liability", default=None
    )
