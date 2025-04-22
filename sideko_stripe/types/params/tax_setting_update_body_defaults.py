import pydantic
import typing
import typing_extensions


class TaxSettingUpdateBodyDefaults(typing_extensions.TypedDict):
    """
    Default configuration to be used on Stripe Tax calculations.
    """

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "inferred_by_currency"]
    ]

    tax_code: typing_extensions.NotRequired[str]


class _SerializerTaxSettingUpdateBodyDefaults(pydantic.BaseModel):
    """
    Serializer for TaxSettingUpdateBodyDefaults handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "inferred_by_currency"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
