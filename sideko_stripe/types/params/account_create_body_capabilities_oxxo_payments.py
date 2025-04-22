import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesOxxoPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesOxxoPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesOxxoPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesOxxoPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
