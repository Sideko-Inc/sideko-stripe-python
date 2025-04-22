import pydantic
import typing
import typing_extensions


class CustomerUpdateBodyCashBalanceSettings(typing_extensions.TypedDict):
    """
    CustomerUpdateBodyCashBalanceSettings
    """

    reconciliation_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "manual", "merchant_default"]
    ]


class _SerializerCustomerUpdateBodyCashBalanceSettings(pydantic.BaseModel):
    """
    Serializer for CustomerUpdateBodyCashBalanceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reconciliation_mode: typing.Optional[
        typing_extensions.Literal["automatic", "manual", "merchant_default"]
    ] = pydantic.Field(alias="reconciliation_mode", default=None)
