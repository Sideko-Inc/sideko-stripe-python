import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesOxxoPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesOxxoPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesOxxoPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesOxxoPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
