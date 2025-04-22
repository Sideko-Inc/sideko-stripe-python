import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlightSegmentsItem(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlightSegmentsItem
    """

    arrival_airport_code: typing_extensions.NotRequired[str]

    carrier: typing_extensions.NotRequired[str]

    departure_airport_code: typing_extensions.NotRequired[str]

    flight_number: typing_extensions.NotRequired[str]

    service_class: typing_extensions.NotRequired[str]

    stopover_allowed: typing_extensions.NotRequired[bool]


class _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlightSegmentsItem(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlightSegmentsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    arrival_airport_code: typing.Optional[str] = pydantic.Field(
        alias="arrival_airport_code", default=None
    )
    carrier: typing.Optional[str] = pydantic.Field(alias="carrier", default=None)
    departure_airport_code: typing.Optional[str] = pydantic.Field(
        alias="departure_airport_code", default=None
    )
    flight_number: typing.Optional[str] = pydantic.Field(
        alias="flight_number", default=None
    )
    service_class: typing.Optional[str] = pydantic.Field(
        alias="service_class", default=None
    )
    stopover_allowed: typing.Optional[bool] = pydantic.Field(
        alias="stopover_allowed", default=None
    )
