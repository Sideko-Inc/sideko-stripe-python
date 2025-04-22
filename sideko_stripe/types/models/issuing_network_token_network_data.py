import pydantic
import typing
import typing_extensions

from .issuing_network_token_device import IssuingNetworkTokenDevice
from .issuing_network_token_mastercard import IssuingNetworkTokenMastercard
from .issuing_network_token_visa import IssuingNetworkTokenVisa
from .issuing_network_token_wallet_provider import IssuingNetworkTokenWalletProvider


class IssuingNetworkTokenNetworkData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    device: typing.Optional[IssuingNetworkTokenDevice] = pydantic.Field(
        alias="device", default=None
    )
    mastercard: typing.Optional[IssuingNetworkTokenMastercard] = pydantic.Field(
        alias="mastercard", default=None
    )
    type_: typing_extensions.Literal["mastercard", "visa"] = pydantic.Field(
        alias="type",
    )
    """
    The network that the token is associated with. An additional hash is included with a name matching this value, containing tokenization data specific to the card network.
    """
    visa: typing.Optional[IssuingNetworkTokenVisa] = pydantic.Field(
        alias="visa", default=None
    )
    wallet_provider: typing.Optional[IssuingNetworkTokenWalletProvider] = (
        pydantic.Field(alias="wallet_provider", default=None)
    )
