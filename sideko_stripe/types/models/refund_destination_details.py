import pydantic
import typing

from .refund_destination_details_blik import RefundDestinationDetailsBlik
from .refund_destination_details_br_bank_transfer import (
    RefundDestinationDetailsBrBankTransfer,
)
from .refund_destination_details_card import RefundDestinationDetailsCard
from .refund_destination_details_eu_bank_transfer import (
    RefundDestinationDetailsEuBankTransfer,
)
from .refund_destination_details_gb_bank_transfer import (
    RefundDestinationDetailsGbBankTransfer,
)
from .refund_destination_details_jp_bank_transfer import (
    RefundDestinationDetailsJpBankTransfer,
)
from .refund_destination_details_multibanco import RefundDestinationDetailsMultibanco
from .refund_destination_details_mx_bank_transfer import (
    RefundDestinationDetailsMxBankTransfer,
)
from .refund_destination_details_p24 import RefundDestinationDetailsP24
from .refund_destination_details_swish import RefundDestinationDetailsSwish
from .refund_destination_details_th_bank_transfer import (
    RefundDestinationDetailsThBankTransfer,
)
from .refund_destination_details_us_bank_transfer import (
    RefundDestinationDetailsUsBankTransfer,
)


class RefundDestinationDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    affirm: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="affirm", default=None
    )
    afterpay_clearpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="afterpay_clearpay", default=None
    )
    alipay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="alipay", default=None
    )
    alma: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="alma", default=None
    )
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    au_bank_transfer: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="au_bank_transfer", default=None
    )
    blik: typing.Optional[RefundDestinationDetailsBlik] = pydantic.Field(
        alias="blik", default=None
    )
    br_bank_transfer: typing.Optional[RefundDestinationDetailsBrBankTransfer] = (
        pydantic.Field(alias="br_bank_transfer", default=None)
    )
    card: typing.Optional[RefundDestinationDetailsCard] = pydantic.Field(
        alias="card", default=None
    )
    cashapp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="cashapp", default=None
    )
    customer_cash_balance: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(alias="customer_cash_balance", default=None)
    )
    eps: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="eps", default=None
    )
    eu_bank_transfer: typing.Optional[RefundDestinationDetailsEuBankTransfer] = (
        pydantic.Field(alias="eu_bank_transfer", default=None)
    )
    gb_bank_transfer: typing.Optional[RefundDestinationDetailsGbBankTransfer] = (
        pydantic.Field(alias="gb_bank_transfer", default=None)
    )
    giropay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="giropay", default=None
    )
    grabpay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="grabpay", default=None
    )
    jp_bank_transfer: typing.Optional[RefundDestinationDetailsJpBankTransfer] = (
        pydantic.Field(alias="jp_bank_transfer", default=None)
    )
    klarna: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="klarna", default=None
    )
    multibanco: typing.Optional[RefundDestinationDetailsMultibanco] = pydantic.Field(
        alias="multibanco", default=None
    )
    mx_bank_transfer: typing.Optional[RefundDestinationDetailsMxBankTransfer] = (
        pydantic.Field(alias="mx_bank_transfer", default=None)
    )
    nz_bank_transfer: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="nz_bank_transfer", default=None
    )
    p24: typing.Optional[RefundDestinationDetailsP24] = pydantic.Field(
        alias="p24", default=None
    )
    paynow: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="paynow", default=None
    )
    paypal: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="paypal", default=None
    )
    pix: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pix", default=None
    )
    revolut: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="revolut", default=None
    )
    sofort: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="sofort", default=None
    )
    swish: typing.Optional[RefundDestinationDetailsSwish] = pydantic.Field(
        alias="swish", default=None
    )
    th_bank_transfer: typing.Optional[RefundDestinationDetailsThBankTransfer] = (
        pydantic.Field(alias="th_bank_transfer", default=None)
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of transaction-specific details of the payment method used in the refund (e.g., `card`). An additional hash is included on `destination_details` with a name matching this value. It contains information specific to the refund transaction.
    """
    us_bank_transfer: typing.Optional[RefundDestinationDetailsUsBankTransfer] = (
        pydantic.Field(alias="us_bank_transfer", default=None)
    )
    wechat_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="wechat_pay", default=None
    )
    zip: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="zip", default=None
    )
