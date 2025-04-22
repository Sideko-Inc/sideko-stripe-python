import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .connect_account_reference import ConnectAccountReference


class QuotesResourceAutomaticTax(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Automatically calculate taxes
    """
    liability: typing.Optional["ConnectAccountReference"] = pydantic.Field(
        alias="liability", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["complete", "failed", "requires_location_inputs"]
    ] = pydantic.Field(alias="status", default=None)
    """
    The status of the most recent automated tax calculation for this quote.
    """
