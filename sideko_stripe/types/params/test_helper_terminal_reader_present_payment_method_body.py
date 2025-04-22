import pydantic
import typing
import typing_extensions

from .test_helper_terminal_reader_present_payment_method_body_card_present import (
    TestHelperTerminalReaderPresentPaymentMethodBodyCardPresent,
    _SerializerTestHelperTerminalReaderPresentPaymentMethodBodyCardPresent,
)
from .test_helper_terminal_reader_present_payment_method_body_interac_present import (
    TestHelperTerminalReaderPresentPaymentMethodBodyInteracPresent,
    _SerializerTestHelperTerminalReaderPresentPaymentMethodBodyInteracPresent,
)


class TestHelperTerminalReaderPresentPaymentMethodBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperTerminalReaderPresentPaymentMethodBody
    """

    amount_tip: typing_extensions.NotRequired[int]
    """
    Simulated on-reader tip amount.
    """

    card_present: typing_extensions.NotRequired[
        TestHelperTerminalReaderPresentPaymentMethodBodyCardPresent
    ]
    """
    Simulated data for the card_present payment method.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    interac_present: typing_extensions.NotRequired[
        TestHelperTerminalReaderPresentPaymentMethodBodyInteracPresent
    ]
    """
    Simulated data for the interac_present payment method.
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["card_present", "interac_present"]
    ]
    """
    Simulated payment type.
    """


class _SerializerTestHelperTerminalReaderPresentPaymentMethodBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTerminalReaderPresentPaymentMethodBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount_tip: typing.Optional[int] = pydantic.Field(alias="amount_tip", default=None)
    card_present: typing.Optional[
        _SerializerTestHelperTerminalReaderPresentPaymentMethodBodyCardPresent
    ] = pydantic.Field(alias="card_present", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    interac_present: typing.Optional[
        _SerializerTestHelperTerminalReaderPresentPaymentMethodBodyInteracPresent
    ] = pydantic.Field(alias="interac_present", default=None)
    type_: typing.Optional[
        typing_extensions.Literal["card_present", "interac_present"]
    ] = pydantic.Field(alias="type", default=None)
