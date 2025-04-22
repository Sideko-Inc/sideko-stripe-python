import pydantic
import typing
import typing_extensions


class AccountCreateBodyGroups(typing_extensions.TypedDict):
    """
    A hash of account group type to tokens. These are account groups this account should be added to.
    """

    payments_pricing: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerAccountCreateBodyGroups(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyGroups handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payments_pricing: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="payments_pricing", default=None
    )
