import pydantic


class PaymentIntentNextActionWechatPayRedirectToAndroidApp(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_id: str = pydantic.Field(
        alias="app_id",
    )
    """
    app_id is the APP ID registered on WeChat open platform
    """
    nonce_str: str = pydantic.Field(
        alias="nonce_str",
    )
    """
    nonce_str is a random string
    """
    package: str = pydantic.Field(
        alias="package",
    )
    """
    package is static value
    """
    partner_id: str = pydantic.Field(
        alias="partner_id",
    )
    """
    an unique merchant ID assigned by WeChat Pay
    """
    prepay_id: str = pydantic.Field(
        alias="prepay_id",
    )
    """
    an unique trading ID assigned by WeChat Pay
    """
    sign: str = pydantic.Field(
        alias="sign",
    )
    """
    A signature
    """
    timestamp: str = pydantic.Field(
        alias="timestamp",
    )
    """
    Specifies the current time in epoch format
    """
