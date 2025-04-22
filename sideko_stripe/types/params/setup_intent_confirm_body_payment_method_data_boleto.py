import pydantic
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodDataBoleto(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodDataBoleto
    """

    tax_id: typing_extensions.Required[str]


class _SerializerSetupIntentConfirmBodyPaymentMethodDataBoleto(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
