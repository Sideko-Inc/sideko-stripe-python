import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesSatispayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesSatispayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesSatispayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesSatispayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
