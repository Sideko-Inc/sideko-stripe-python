import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesPaynowPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesPaynowPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesPaynowPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesPaynowPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
