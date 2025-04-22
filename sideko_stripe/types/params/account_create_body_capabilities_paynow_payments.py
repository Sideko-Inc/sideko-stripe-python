import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesPaynowPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesPaynowPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesPaynowPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesPaynowPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
