import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsPaymentsFeatures(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsPaymentsFeatures
    """

    capture_payments: typing_extensions.NotRequired[bool]

    destination_on_behalf_of_charge_management: typing_extensions.NotRequired[bool]

    dispute_management: typing_extensions.NotRequired[bool]

    refund_management: typing_extensions.NotRequired[bool]


class _SerializerAccountSessionsCreateBodyComponentsPaymentsFeatures(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsPaymentsFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_payments: typing.Optional[bool] = pydantic.Field(
        alias="capture_payments", default=None
    )
    destination_on_behalf_of_charge_management: typing.Optional[bool] = pydantic.Field(
        alias="destination_on_behalf_of_charge_management", default=None
    )
    dispute_management: typing.Optional[bool] = pydantic.Field(
        alias="dispute_management", default=None
    )
    refund_management: typing.Optional[bool] = pydantic.Field(
        alias="refund_management", default=None
    )
