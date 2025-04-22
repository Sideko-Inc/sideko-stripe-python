import pydantic
import typing
import typing_extensions

from .token_create_body_account_company import (
    TokenCreateBodyAccountCompany,
    _SerializerTokenCreateBodyAccountCompany,
)
from .token_create_body_account_individual import (
    TokenCreateBodyAccountIndividual,
    _SerializerTokenCreateBodyAccountIndividual,
)


class TokenCreateBodyAccount(typing_extensions.TypedDict):
    """
    Information for the account this token represents.
    """

    business_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "company", "government_entity", "individual", "non_profit"
        ]
    ]

    company: typing_extensions.NotRequired[TokenCreateBodyAccountCompany]

    individual: typing_extensions.NotRequired[TokenCreateBodyAccountIndividual]

    tos_shown_and_accepted: typing_extensions.NotRequired[bool]


class _SerializerTokenCreateBodyAccount(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    business_type: typing.Optional[
        typing_extensions.Literal[
            "company", "government_entity", "individual", "non_profit"
        ]
    ] = pydantic.Field(alias="business_type", default=None)
    company: typing.Optional[_SerializerTokenCreateBodyAccountCompany] = pydantic.Field(
        alias="company", default=None
    )
    individual: typing.Optional[_SerializerTokenCreateBodyAccountIndividual] = (
        pydantic.Field(alias="individual", default=None)
    )
    tos_shown_and_accepted: typing.Optional[bool] = pydantic.Field(
        alias="tos_shown_and_accepted", default=None
    )
