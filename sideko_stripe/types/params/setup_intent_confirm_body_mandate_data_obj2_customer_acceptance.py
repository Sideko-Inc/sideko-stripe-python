import pydantic
import typing_extensions

from .setup_intent_confirm_body_mandate_data_obj2_customer_acceptance_online import (
    SetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline,
    _SerializerSetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline,
)


class SetupIntentConfirmBodyMandateDataObj2CustomerAcceptance(
    typing_extensions.TypedDict
):
    """
    SetupIntentConfirmBodyMandateDataObj2CustomerAcceptance
    """

    online: typing_extensions.Required[
        SetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline
    ]

    type_: typing_extensions.Required[typing_extensions.Literal["online"]]


class _SerializerSetupIntentConfirmBodyMandateDataObj2CustomerAcceptance(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyMandateDataObj2CustomerAcceptance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    online: _SerializerSetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline = (
        pydantic.Field(
            alias="online",
        )
    )
    type_: typing_extensions.Literal["online"] = pydantic.Field(
        alias="type",
    )
