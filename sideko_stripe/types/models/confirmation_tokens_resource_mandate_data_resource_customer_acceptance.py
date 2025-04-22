import pydantic
import typing

from .confirmation_tokens_resource_mandate_data_resource_customer_acceptance_resource_online import (
    ConfirmationTokensResourceMandateDataResourceCustomerAcceptanceResourceOnline,
)


class ConfirmationTokensResourceMandateDataResourceCustomerAcceptance(
    pydantic.BaseModel
):
    """
    This hash contains details about the customer acceptance of the Mandate.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    online: typing.Optional[
        ConfirmationTokensResourceMandateDataResourceCustomerAcceptanceResourceOnline
    ] = pydantic.Field(alias="online", default=None)
    """
    This hash contains details about the online acceptance.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of customer acceptance information included with the Mandate.
    """
