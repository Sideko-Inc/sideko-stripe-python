import pydantic
import typing
import typing_extensions


class AccountUpdateBodyTosAcceptance(typing_extensions.TypedDict):
    """
    Details on the account's acceptance of the [Stripe Services Agreement](/connect/updating-accounts#tos-acceptance). This property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. This property defaults to a `full` service agreement when empty.
    """

    date: typing_extensions.NotRequired[int]

    ip: typing_extensions.NotRequired[str]

    service_agreement: typing_extensions.NotRequired[str]

    user_agent: typing_extensions.NotRequired[str]


class _SerializerAccountUpdateBodyTosAcceptance(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyTosAcceptance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    service_agreement: typing.Optional[str] = pydantic.Field(
        alias="service_agreement", default=None
    )
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
