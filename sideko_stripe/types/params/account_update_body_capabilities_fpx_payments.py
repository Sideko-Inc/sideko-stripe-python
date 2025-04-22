import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesFpxPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesFpxPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesFpxPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesFpxPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
