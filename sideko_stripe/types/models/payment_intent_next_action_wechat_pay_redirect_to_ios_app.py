import pydantic


class PaymentIntentNextActionWechatPayRedirectToIosApp(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    native_url: str = pydantic.Field(
        alias="native_url",
    )
    """
    An universal link that redirect to WeChat Pay app
    """
