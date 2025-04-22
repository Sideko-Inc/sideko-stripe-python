import pydantic
import typing_extensions

from .setup_intent_create_body_mandate_data_obj0_customer_acceptance import (
    SetupIntentCreateBodyMandateDataObj0CustomerAcceptance,
    _SerializerSetupIntentCreateBodyMandateDataObj0CustomerAcceptance,
)


class SetupIntentCreateBodyMandateDataObj0(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyMandateDataObj0
    """

    customer_acceptance: typing_extensions.Required[
        SetupIntentCreateBodyMandateDataObj0CustomerAcceptance
    ]


class _SerializerSetupIntentCreateBodyMandateDataObj0(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyMandateDataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_acceptance: _SerializerSetupIntentCreateBodyMandateDataObj0CustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
