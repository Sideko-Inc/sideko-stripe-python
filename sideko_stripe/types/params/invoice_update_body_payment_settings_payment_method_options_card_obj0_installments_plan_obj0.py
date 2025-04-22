import pydantic
import typing
import typing_extensions


class InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0
    """

    count: typing_extensions.NotRequired[int]

    interval: typing_extensions.NotRequired[typing_extensions.Literal["month"]]

    type_: typing_extensions.Required[typing_extensions.Literal["fixed_count"]]


class _SerializerInvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyPaymentSettingsPaymentMethodOptionsCardObj0InstallmentsPlanObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    count: typing.Optional[int] = pydantic.Field(alias="count", default=None)
    interval: typing.Optional[typing_extensions.Literal["month"]] = pydantic.Field(
        alias="interval", default=None
    )
    type_: typing_extensions.Literal["fixed_count"] = pydantic.Field(
        alias="type",
    )
