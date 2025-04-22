import pydantic
import typing
import typing_extensions


class AccountLinkCreateBodyCollectionOptions(typing_extensions.TypedDict):
    """
    Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow.
    """

    fields: typing_extensions.NotRequired[
        typing_extensions.Literal["currently_due", "eventually_due"]
    ]

    future_requirements: typing_extensions.NotRequired[
        typing_extensions.Literal["include", "omit"]
    ]


class _SerializerAccountLinkCreateBodyCollectionOptions(pydantic.BaseModel):
    """
    Serializer for AccountLinkCreateBodyCollectionOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fields: typing.Optional[
        typing_extensions.Literal["currently_due", "eventually_due"]
    ] = pydantic.Field(alias="fields", default=None)
    future_requirements: typing.Optional[
        typing_extensions.Literal["include", "omit"]
    ] = pydantic.Field(alias="future_requirements", default=None)
