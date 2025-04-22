import pydantic
import typing_extensions


class PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesExtendedAuthorizationExtendedAuthorization(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal["disabled", "enabled"] = pydantic.Field(
        alias="status",
    )
    """
    Indicates whether or not the capture window is extended beyond the standard authorization.
    """
