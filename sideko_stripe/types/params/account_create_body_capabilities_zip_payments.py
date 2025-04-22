import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesZipPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesZipPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesZipPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesZipPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
