import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesMobilepayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesMobilepayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesMobilepayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesMobilepayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
