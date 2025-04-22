import pydantic
import typing_extensions

from .setup_intent_confirm_body_mandate_data_obj2_customer_acceptance import (
    SetupIntentConfirmBodyMandateDataObj2CustomerAcceptance,
    _SerializerSetupIntentConfirmBodyMandateDataObj2CustomerAcceptance,
)


class SetupIntentConfirmBodyMandateDataObj2(typing_extensions.TypedDict):
    """
    This hash contains details about the Mandate to create
    """

    customer_acceptance: typing_extensions.Required[
        SetupIntentConfirmBodyMandateDataObj2CustomerAcceptance
    ]


class _SerializerSetupIntentConfirmBodyMandateDataObj2(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyMandateDataObj2 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_acceptance: _SerializerSetupIntentConfirmBodyMandateDataObj2CustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
