import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesGrabpayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesGrabpayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesGrabpayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesGrabpayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
