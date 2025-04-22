import pydantic
import typing


class TreasuryOutboundPaymentsResourceOutboundPaymentResourceEndUserDetails(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked.
    """
    present: bool = pydantic.Field(
        alias="present",
    )
    """
    `true` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.
    """
