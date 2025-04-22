import pydantic

from .confirmation_tokens_resource_mandate_data_resource_customer_acceptance import (
    ConfirmationTokensResourceMandateDataResourceCustomerAcceptance,
)


class ConfirmationTokensResourceMandateData(pydantic.BaseModel):
    """
    Data used for generating a Mandate.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_acceptance: ConfirmationTokensResourceMandateDataResourceCustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
    """
    This hash contains details about the customer acceptance of the Mandate.
    """
