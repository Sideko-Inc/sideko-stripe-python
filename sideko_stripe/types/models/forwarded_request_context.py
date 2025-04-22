import pydantic


class ForwardedRequestContext(pydantic.BaseModel):
    """
    Metadata about the forwarded request.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    destination_duration: int = pydantic.Field(
        alias="destination_duration",
    )
    """
    The time it took in milliseconds for the destination endpoint to respond.
    """
    destination_ip_address: str = pydantic.Field(
        alias="destination_ip_address",
    )
    """
    The IP address of the destination.
    """
