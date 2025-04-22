import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesKlarnaPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesKlarnaPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesKlarnaPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesKlarnaPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
