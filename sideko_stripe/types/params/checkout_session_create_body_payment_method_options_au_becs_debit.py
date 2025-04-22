import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit
    """

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]

    target_date: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsAuBecsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
