import pydantic
import typing
import typing_extensions

from .account_link_create_body_collection_options import (
    AccountLinkCreateBodyCollectionOptions,
    _SerializerAccountLinkCreateBodyCollectionOptions,
)


class AccountLinkCreateBody(typing_extensions.TypedDict, total=False):
    """
    AccountLinkCreateBody
    """

    account: typing_extensions.Required[str]
    """
    The identifier of the account to create an account link for.
    """

    collect: typing_extensions.NotRequired[
        typing_extensions.Literal["currently_due", "eventually_due"]
    ]
    """
    The collect parameter is deprecated. Use `collection_options` instead.
    """

    collection_options: typing_extensions.NotRequired[
        AccountLinkCreateBodyCollectionOptions
    ]
    """
    Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    refresh_url: typing_extensions.NotRequired[str]
    """
    The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link's URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user.
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The URL that the user will be redirected to upon leaving or completing the linked flow.
    """

    type_: typing_extensions.Required[
        typing_extensions.Literal["account_onboarding", "account_update"]
    ]
    """
    The type of account link the user is requesting. Possible values are `account_onboarding` or `account_update`.
    """


class _SerializerAccountLinkCreateBody(pydantic.BaseModel):
    """
    Serializer for AccountLinkCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account: str = pydantic.Field(
        alias="account",
    )
    collect: typing.Optional[
        typing_extensions.Literal["currently_due", "eventually_due"]
    ] = pydantic.Field(alias="collect", default=None)
    collection_options: typing.Optional[
        _SerializerAccountLinkCreateBodyCollectionOptions
    ] = pydantic.Field(alias="collection_options", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    refresh_url: typing.Optional[str] = pydantic.Field(
        alias="refresh_url", default=None
    )
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    type_: typing_extensions.Literal["account_onboarding", "account_update"] = (
        pydantic.Field(
            alias="type",
        )
    )
