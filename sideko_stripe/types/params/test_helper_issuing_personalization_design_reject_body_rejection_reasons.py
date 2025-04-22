import pydantic
import typing
import typing_extensions


class TestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons(
    typing_extensions.TypedDict
):
    """
    The reason(s) the personalization design was rejected.
    """

    card_logo: typing_extensions.NotRequired[
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
    ]

    carrier_text: typing_extensions.NotRequired[
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
    ]


class _SerializerTestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
