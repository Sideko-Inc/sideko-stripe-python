import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesCardPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesCardPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesCardPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesCardPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
