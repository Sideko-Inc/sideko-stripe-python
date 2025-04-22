import pydantic
import typing_extensions

from .setup_intent_confirm_body_mandate_data_obj0_customer_acceptance import (
    SetupIntentConfirmBodyMandateDataObj0CustomerAcceptance,
    _SerializerSetupIntentConfirmBodyMandateDataObj0CustomerAcceptance,
)


class SetupIntentConfirmBodyMandateDataObj0(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyMandateDataObj0
    """

    customer_acceptance: typing_extensions.Required[
        SetupIntentConfirmBodyMandateDataObj0CustomerAcceptance
    ]


class _SerializerSetupIntentConfirmBodyMandateDataObj0(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyMandateDataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_acceptance: _SerializerSetupIntentConfirmBodyMandateDataObj0CustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
