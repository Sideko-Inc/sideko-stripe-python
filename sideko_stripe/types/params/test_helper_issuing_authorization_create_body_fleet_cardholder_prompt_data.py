import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData
    """

    driver_id: typing_extensions.NotRequired[str]

    odometer: typing_extensions.NotRequired[int]

    unspecified_id: typing_extensions.NotRequired[str]

    user_id: typing_extensions.NotRequired[str]

    vehicle_number: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    driver_id: typing.Optional[str] = pydantic.Field(alias="driver_id", default=None)
    odometer: typing.Optional[int] = pydantic.Field(alias="odometer", default=None)
    unspecified_id: typing.Optional[str] = pydantic.Field(
        alias="unspecified_id", default=None
    )
    user_id: typing.Optional[str] = pydantic.Field(alias="user_id", default=None)
    vehicle_number: typing.Optional[str] = pydantic.Field(
        alias="vehicle_number", default=None
    )
