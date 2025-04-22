import pydantic
import typing_extensions


class PaymentIntentConfirmBodyMandateDataObj0CustomerAcceptanceOnline(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyMandateDataObj0CustomerAcceptanceOnline
    """

    ip_address: typing_extensions.Required[str]

    user_agent: typing_extensions.Required[str]


class _SerializerPaymentIntentConfirmBodyMandateDataObj0CustomerAcceptanceOnline(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyMandateDataObj0CustomerAcceptanceOnline handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ip_address: str = pydantic.Field(
        alias="ip_address",
    )
    user_agent: str = pydantic.Field(
        alias="user_agent",
    )
