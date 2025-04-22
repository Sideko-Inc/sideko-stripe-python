import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .charge import Charge
    from .setup_attempt import SetupAttempt


class SepaDebitGeneratedFrom(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge: typing.Optional[typing.Union[str, "Charge"]] = pydantic.Field(
        alias="charge", default=None
    )
    """
    The ID of the Charge that generated this PaymentMethod, if any.
    """
    setup_attempt: typing.Optional[typing.Union[str, "SetupAttempt"]] = pydantic.Field(
        alias="setup_attempt", default=None
    )
    """
    The ID of the SetupAttempt that generated this PaymentMethod, if any.
    """
