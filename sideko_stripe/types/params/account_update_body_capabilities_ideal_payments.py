import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesIdealPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesIdealPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesIdealPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesIdealPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
