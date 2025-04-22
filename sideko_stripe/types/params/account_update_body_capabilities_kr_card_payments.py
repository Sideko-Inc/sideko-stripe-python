import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesKrCardPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesKrCardPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesKrCardPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesKrCardPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
