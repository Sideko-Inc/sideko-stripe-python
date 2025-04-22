import pydantic
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodDataBoleto(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodDataBoleto
    """

    tax_id: typing_extensions.Required[str]


class _SerializerSetupIntentUpdateBodyPaymentMethodDataBoleto(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
