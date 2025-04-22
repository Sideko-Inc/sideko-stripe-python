import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsDocuments(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsDocuments
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]


class _SerializerAccountSessionsCreateBodyComponentsDocuments(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponentsDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="features", default=None
    )
