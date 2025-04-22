import pydantic
import typing


class PaymentMethodDetailsMultibanco(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    entity: typing.Optional[str] = pydantic.Field(alias="entity", default=None)
    """
    Entity number associated with this Multibanco payment.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Reference number associated with this Multibanco payment.
    """
