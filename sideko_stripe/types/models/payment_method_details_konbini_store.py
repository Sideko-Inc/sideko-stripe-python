import pydantic
import typing
import typing_extensions


class PaymentMethodDetailsKonbiniStore(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    chain: typing.Optional[
        typing_extensions.Literal["familymart", "lawson", "ministop", "seicomart"]
    ] = pydantic.Field(alias="chain", default=None)
    """
    The name of the convenience store chain where the payment was completed.
    """
