import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesKonbiniPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesKonbiniPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesKonbiniPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesKonbiniPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
