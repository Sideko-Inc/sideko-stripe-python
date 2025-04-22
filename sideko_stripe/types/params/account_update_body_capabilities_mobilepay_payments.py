import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesMobilepayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesMobilepayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesMobilepayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesMobilepayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
