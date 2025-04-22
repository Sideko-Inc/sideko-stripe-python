import pydantic
import typing
import typing_extensions


class TreasuryOutboundPaymentCreateBodyEndUserDetails(typing_extensions.TypedDict):
    """
    End user details.
    """

    ip_address: typing_extensions.NotRequired[str]

    present: typing_extensions.Required[bool]


class _SerializerTreasuryOutboundPaymentCreateBodyEndUserDetails(pydantic.BaseModel):
    """
    Serializer for TreasuryOutboundPaymentCreateBodyEndUserDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    present: bool = pydantic.Field(
        alias="present",
    )
