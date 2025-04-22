import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesGrabpayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesGrabpayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesGrabpayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesGrabpayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
