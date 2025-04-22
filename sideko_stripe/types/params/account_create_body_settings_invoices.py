import pydantic
import typing
import typing_extensions


class AccountCreateBodySettingsInvoices(typing_extensions.TypedDict):
    """
    AccountCreateBodySettingsInvoices
    """

    hosted_payment_method_save: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "never", "offer"]
    ]


class _SerializerAccountCreateBodySettingsInvoices(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettingsInvoices handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    hosted_payment_method_save: typing.Optional[
        typing_extensions.Literal["always", "never", "offer"]
    ] = pydantic.Field(alias="hosted_payment_method_save", default=None)
