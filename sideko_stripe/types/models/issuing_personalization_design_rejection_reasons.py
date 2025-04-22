import pydantic
import typing
import typing_extensions


class IssuingPersonalizationDesignRejectionReasons(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_logo: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "geographic_location",
                "inappropriate",
                "network_name",
                "non_binary_image",
                "non_fiat_currency",
                "other",
                "other_entity",
                "promotional_material",
            ]
        ]
    ] = pydantic.Field(alias="card_logo", default=None)
    """
    The reason(s) the card logo was rejected.
    """
    carrier_text: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "geographic_location",
                "inappropriate",
                "network_name",
                "non_fiat_currency",
                "other",
                "other_entity",
                "promotional_material",
            ]
        ]
    ] = pydantic.Field(alias="carrier_text", default=None)
    """
    The reason(s) the carrier text was rejected.
    """
