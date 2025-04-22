import pydantic
import typing
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodOptionsPaypal(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsPaypal
    """

    billing_agreement_id: typing_extensions.NotRequired[str]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsPaypal(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsPaypal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    billing_agreement_id: typing.Optional[str] = pydantic.Field(
        alias="billing_agreement_id", default=None
    )
