import pydantic
import typing
import typing_extensions


class AccountCreateBodyControllerStripeDashboard(typing_extensions.TypedDict):
    """
    AccountCreateBodyControllerStripeDashboard
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["express", "full", "none"]
    ]


class _SerializerAccountCreateBodyControllerStripeDashboard(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyControllerStripeDashboard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing.Optional[typing_extensions.Literal["express", "full", "none"]] = (
        pydantic.Field(alias="type", default=None)
    )
