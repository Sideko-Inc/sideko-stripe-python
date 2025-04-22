import pydantic
import typing
import typing_extensions


class CustomerCreateBodyCashBalanceSettings(typing_extensions.TypedDict):
    """
    CustomerCreateBodyCashBalanceSettings
    """

    reconciliation_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "manual", "merchant_default"]
    ]


class _SerializerCustomerCreateBodyCashBalanceSettings(pydantic.BaseModel):
    """
    Serializer for CustomerCreateBodyCashBalanceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reconciliation_mode: typing.Optional[
        typing_extensions.Literal["automatic", "manual", "merchant_default"]
    ] = pydantic.Field(alias="reconciliation_mode", default=None)
