import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesAffirmPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesAffirmPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesAffirmPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesAffirmPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
