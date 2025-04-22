import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesSepaDebitPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesSepaDebitPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesSepaDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesSepaDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
