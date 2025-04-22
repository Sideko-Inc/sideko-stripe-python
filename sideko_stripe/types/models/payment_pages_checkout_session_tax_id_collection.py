import pydantic
import typing_extensions


class PaymentPagesCheckoutSessionTaxIdCollection(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Indicates whether tax ID collection is enabled for the session
    """
    required: typing_extensions.Literal["if_supported", "never"] = pydantic.Field(
        alias="required",
    )
    """
    Indicates whether a tax ID is required on the payment page
    """
