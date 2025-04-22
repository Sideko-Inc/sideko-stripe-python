import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesSatispayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesSatispayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesSatispayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesSatispayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
