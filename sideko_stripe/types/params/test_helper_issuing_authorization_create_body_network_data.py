import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationCreateBodyNetworkData(typing_extensions.TypedDict):
    """
    Details about the authorization, such as identifiers, set by the card network.
    """

    acquiring_institution_id: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingAuthorizationCreateBodyNetworkData(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyNetworkData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acquiring_institution_id: typing.Optional[str] = pydantic.Field(
        alias="acquiring_institution_id", default=None
    )
