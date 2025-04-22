import pydantic
import typing
import typing_extensions


class AccountCreateBodyControllerFees(typing_extensions.TypedDict):
    """
    AccountCreateBodyControllerFees
    """

    payer: typing_extensions.NotRequired[
        typing_extensions.Literal["account", "application"]
    ]


class _SerializerAccountCreateBodyControllerFees(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyControllerFees handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payer: typing.Optional[typing_extensions.Literal["account", "application"]] = (
        pydantic.Field(alias="payer", default=None)
    )
