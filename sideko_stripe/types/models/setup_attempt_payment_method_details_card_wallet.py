import pydantic
import typing
import typing_extensions


class SetupAttemptPaymentMethodDetailsCardWallet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    apple_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="apple_pay", default=None
    )
    google_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="google_pay", default=None
    )
    type_: typing_extensions.Literal["apple_pay", "google_pay", "link"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The type of the card wallet, one of `apple_pay`, `google_pay`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
    """
