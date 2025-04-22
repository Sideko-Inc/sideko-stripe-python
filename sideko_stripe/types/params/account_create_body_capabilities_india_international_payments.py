import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesIndiaInternationalPayments(
    typing_extensions.TypedDict
):
    """
    AccountCreateBodyCapabilitiesIndiaInternationalPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesIndiaInternationalPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesIndiaInternationalPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
