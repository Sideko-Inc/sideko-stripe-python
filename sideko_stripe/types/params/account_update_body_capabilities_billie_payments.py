import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesBilliePayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesBilliePayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesBilliePayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesBilliePayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
