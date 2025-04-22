import pydantic
import typing
import typing_extensions


class TreasuryFinancialAccountCreateBodyPlatformRestrictions(
    typing_extensions.TypedDict
):
    """
    The set of functionalities that the platform can restrict on the FinancialAccount.
    """

    inbound_flows: typing_extensions.NotRequired[
        typing_extensions.Literal["restricted", "unrestricted"]
    ]

    outbound_flows: typing_extensions.NotRequired[
        typing_extensions.Literal["restricted", "unrestricted"]
    ]


class _SerializerTreasuryFinancialAccountCreateBodyPlatformRestrictions(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyPlatformRestrictions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    inbound_flows: typing.Optional[
        typing_extensions.Literal["restricted", "unrestricted"]
    ] = pydantic.Field(alias="inbound_flows", default=None)
    outbound_flows: typing.Optional[
        typing_extensions.Literal["restricted", "unrestricted"]
    ] = pydantic.Field(alias="outbound_flows", default=None)
