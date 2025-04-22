import pydantic
import typing
import typing_extensions


class AccountCreateBodyControllerLosses(typing_extensions.TypedDict):
    """
    AccountCreateBodyControllerLosses
    """

    payments: typing_extensions.NotRequired[
        typing_extensions.Literal["application", "stripe"]
    ]


class _SerializerAccountCreateBodyControllerLosses(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyControllerLosses handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payments: typing.Optional[typing_extensions.Literal["application", "stripe"]] = (
        pydantic.Field(alias="payments", default=None)
    )
