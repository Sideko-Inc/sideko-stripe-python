import pydantic
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .connect_account_reference import ConnectAccountReference


class PaymentLinksResourceSubscriptionDataInvoiceSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    issuer: "ConnectAccountReference" = pydantic.Field(
        alias="issuer",
    )
