import pydantic
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodDataSofort(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodDataSofort
    """

    country: typing_extensions.Required[
        typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodDataSofort(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataSofort handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"] = (
        pydantic.Field(
            alias="country",
        )
    )
