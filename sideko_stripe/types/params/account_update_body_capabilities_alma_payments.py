import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesAlmaPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesAlmaPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesAlmaPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesAlmaPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
