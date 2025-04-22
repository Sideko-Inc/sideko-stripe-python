import pydantic
import typing
import typing_extensions


class AccountCreateBodySettingsBacsDebitPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodySettingsBacsDebitPayments
    """

    display_name: typing_extensions.NotRequired[str]


class _SerializerAccountCreateBodySettingsBacsDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettingsBacsDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
