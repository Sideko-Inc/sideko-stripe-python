import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesTwintPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesTwintPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesTwintPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesTwintPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
