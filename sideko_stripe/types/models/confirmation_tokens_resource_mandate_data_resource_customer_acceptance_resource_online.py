import pydantic
import typing


class ConfirmationTokensResourceMandateDataResourceCustomerAcceptanceResourceOnline(
    pydantic.BaseModel
):
    """
    This hash contains details about the online acceptance.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    The IP address from which the Mandate was accepted by the customer.
    """
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
    """
    The user agent of the browser from which the Mandate was accepted by the customer.
    """
