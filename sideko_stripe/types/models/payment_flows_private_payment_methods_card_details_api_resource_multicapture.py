import pydantic
import typing_extensions


class PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceMulticapture(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal["available", "unavailable"] = pydantic.Field(
        alias="status",
    )
    """
    Indicates whether or not multiple captures are supported.
    """
