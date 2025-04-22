import pydantic
import typing
import typing_extensions


class SetupIntentTypeSpecificPaymentMethodOptionsClient(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
    """
    Bank account verification method.
    """
