import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesKlarnaPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesKlarnaPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesKlarnaPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesKlarnaPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
