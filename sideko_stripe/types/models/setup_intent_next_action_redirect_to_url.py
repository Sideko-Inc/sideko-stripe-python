import pydantic
import typing


class SetupIntentNextActionRedirectToUrl(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    """
    If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    The URL you must redirect your customer to in order to authenticate.
    """
