import pydantic
import typing
import typing_extensions


class BillingPortalConfigurationCreateBodyFeaturesCustomerUpdate(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesCustomerUpdate
    """

    allowed_updates: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                typing_extensions.Literal[
                    "address", "email", "name", "phone", "shipping", "tax_id"
                ]
            ],
            str,
        ]
    ]

    enabled: typing_extensions.Required[bool]


class _SerializerBillingPortalConfigurationCreateBodyFeaturesCustomerUpdate(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesCustomerUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allowed_updates: typing.Optional[
        typing.Union[
            typing.List[
                typing_extensions.Literal[
                    "address", "email", "name", "phone", "shipping", "tax_id"
                ]
            ],
            str,
        ]
    ] = pydantic.Field(alias="allowed_updates", default=None)
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
