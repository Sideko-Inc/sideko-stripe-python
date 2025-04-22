import pydantic
import typing
import typing_extensions


class SetupIntentCreateBodyAutomaticPaymentMethods(typing_extensions.TypedDict):
    """
    When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.
    """

    allow_redirects: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "never"]
    ]

    enabled: typing_extensions.Required[bool]


class _SerializerSetupIntentCreateBodyAutomaticPaymentMethods(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyAutomaticPaymentMethods handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_redirects: typing.Optional[typing_extensions.Literal["always", "never"]] = (
        pydantic.Field(alias="allow_redirects", default=None)
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
