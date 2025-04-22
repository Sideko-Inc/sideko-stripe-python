import pydantic
import typing
import typing_extensions

from .token_create_body_account import (
    TokenCreateBodyAccount,
    _SerializerTokenCreateBodyAccount,
)
from .token_create_body_bank_account import (
    TokenCreateBodyBankAccount,
    _SerializerTokenCreateBodyBankAccount,
)
from .token_create_body_card_obj0 import (
    TokenCreateBodyCardObj0,
    _SerializerTokenCreateBodyCardObj0,
)
from .token_create_body_cvc_update import (
    TokenCreateBodyCvcUpdate,
    _SerializerTokenCreateBodyCvcUpdate,
)
from .token_create_body_person import (
    TokenCreateBodyPerson,
    _SerializerTokenCreateBodyPerson,
)
from .token_create_body_pii import TokenCreateBodyPii, _SerializerTokenCreateBodyPii


class TokenCreateBody(typing_extensions.TypedDict, total=False):
    """
    TokenCreateBody
    """

    account: typing_extensions.NotRequired[TokenCreateBodyAccount]
    """
    Information for the account this token represents.
    """

    bank_account: typing_extensions.NotRequired[TokenCreateBodyBankAccount]
    """
    The bank account this token will represent.
    """

    card: typing_extensions.NotRequired[typing.Union[TokenCreateBodyCardObj0, str]]
    """
    The card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user's credit card details, with the options described below.
    """

    customer: typing_extensions.NotRequired[str]
    """
    Create a token for the customer, which is owned by the application's account. You can only use this with an [OAuth access token](https://stripe.com/docs/connect/standard-accounts) or [Stripe-Account header](https://stripe.com/docs/connect/authentication). Learn more about [cloning saved payment methods](https://stripe.com/docs/connect/cloning-saved-payment-methods).
    """

    cvc_update: typing_extensions.NotRequired[TokenCreateBodyCvcUpdate]
    """
    The updated CVC value this token represents.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    person: typing_extensions.NotRequired[TokenCreateBodyPerson]
    """
    Information for the person this token represents.
    """

    pii: typing_extensions.NotRequired[TokenCreateBodyPii]
    """
    The PII this token represents.
    """


class _SerializerTokenCreateBody(pydantic.BaseModel):
    """
    Serializer for TokenCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account: typing.Optional[_SerializerTokenCreateBodyAccount] = pydantic.Field(
        alias="account", default=None
    )
    bank_account: typing.Optional[_SerializerTokenCreateBodyBankAccount] = (
        pydantic.Field(alias="bank_account", default=None)
    )
    card: typing.Optional[typing.Union[_SerializerTokenCreateBodyCardObj0, str]] = (
        pydantic.Field(alias="card", default=None)
    )
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    cvc_update: typing.Optional[_SerializerTokenCreateBodyCvcUpdate] = pydantic.Field(
        alias="cvc_update", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    person: typing.Optional[_SerializerTokenCreateBodyPerson] = pydantic.Field(
        alias="person", default=None
    )
    pii: typing.Optional[_SerializerTokenCreateBodyPii] = pydantic.Field(
        alias="pii", default=None
    )
