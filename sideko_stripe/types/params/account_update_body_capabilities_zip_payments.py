import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesZipPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesZipPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesZipPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesZipPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
