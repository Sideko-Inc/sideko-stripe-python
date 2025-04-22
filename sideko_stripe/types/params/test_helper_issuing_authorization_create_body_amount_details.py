import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationCreateBodyAmountDetails(
    typing_extensions.TypedDict
):
    """
    Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    atm_fee: typing_extensions.NotRequired[int]

    cashback_amount: typing_extensions.NotRequired[int]


class _SerializerTestHelperIssuingAuthorizationCreateBodyAmountDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyAmountDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    atm_fee: typing.Optional[int] = pydantic.Field(alias="atm_fee", default=None)
    cashback_amount: typing.Optional[int] = pydantic.Field(
        alias="cashback_amount", default=None
    )
