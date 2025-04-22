import pydantic
import typing
import typing_extensions


class TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire(
    typing_extensions.TypedDict
):
    """
    TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire
    """

    chips: typing_extensions.NotRequired[str]

    imad: typing_extensions.NotRequired[str]

    omad: typing_extensions.NotRequired[str]


class _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    chips: typing.Optional[str] = pydantic.Field(alias="chips", default=None)
    imad: typing.Optional[str] = pydantic.Field(alias="imad", default=None)
    omad: typing.Optional[str] = pydantic.Field(alias="omad", default=None)
