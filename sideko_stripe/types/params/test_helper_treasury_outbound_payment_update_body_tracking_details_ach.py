import pydantic
import typing_extensions


class TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch(
    typing_extensions.TypedDict
):
    """
    TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch
    """

    trace_id: typing_extensions.Required[str]


class _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    trace_id: str = pydantic.Field(
        alias="trace_id",
    )
