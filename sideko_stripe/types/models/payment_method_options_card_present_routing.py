import pydantic
import typing
import typing_extensions


class PaymentMethodOptionsCardPresentRouting(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    requested_priority: typing.Optional[
        typing_extensions.Literal["domestic", "international"]
    ] = pydantic.Field(alias="requested_priority", default=None)
    """
    Requested routing priority
    """
