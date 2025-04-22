import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesKonbiniPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesKonbiniPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesKonbiniPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesKonbiniPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
