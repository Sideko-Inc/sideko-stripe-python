import pydantic
import typing


class PaymentMethodConfigBizPaymentMethodConfigurationDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    """
    ID of the payment method configuration used.
    """
    parent: typing.Optional[str] = pydantic.Field(alias="parent", default=None)
    """
    ID of the parent payment method configuration used.
    """
