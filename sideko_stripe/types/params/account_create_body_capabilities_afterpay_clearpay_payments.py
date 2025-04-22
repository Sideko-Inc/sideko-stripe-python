import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesAfterpayClearpayPayments(
    typing_extensions.TypedDict
):
    """
    AccountCreateBodyCapabilitiesAfterpayClearpayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesAfterpayClearpayPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesAfterpayClearpayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
