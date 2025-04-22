import pydantic
import typing
import typing_extensions


class BillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate
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

    enabled: typing_extensions.NotRequired[bool]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate handling case conversions
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
    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
