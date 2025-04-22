import pydantic
import typing
import typing_extensions


class PaymentIntentNextActionVerifyWithMicrodeposits(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    arrival_date: int = pydantic.Field(
        alias="arrival_date",
    )
    """
    The timestamp when the microdeposits are expected to land.
    """
    hosted_verification_url: str = pydantic.Field(
        alias="hosted_verification_url",
    )
    """
    The URL for the hosted verification page, which allows customers to verify their bank account.
    """
    microdeposit_type: typing.Optional[
        typing_extensions.Literal["amounts", "descriptor_code"]
    ] = pydantic.Field(alias="microdeposit_type", default=None)
    """
    The type of the microdeposit sent to the customer. Used to distinguish between different verification methods.
    """
