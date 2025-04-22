import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesAffirmPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesAffirmPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesAffirmPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesAffirmPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
