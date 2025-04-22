import pydantic
import typing_extensions


class IssuingCardCreateBodyShippingAddressValidation(typing_extensions.TypedDict):
    """
    IssuingCardCreateBodyShippingAddressValidation
    """

    mode: typing_extensions.Required[
        typing_extensions.Literal[
            "disabled", "normalization_only", "validation_and_normalization"
        ]
    ]


class _SerializerIssuingCardCreateBodyShippingAddressValidation(pydantic.BaseModel):
    """
    Serializer for IssuingCardCreateBodyShippingAddressValidation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mode: typing_extensions.Literal[
        "disabled", "normalization_only", "validation_and_normalization"
    ] = pydantic.Field(
        alias="mode",
    )
