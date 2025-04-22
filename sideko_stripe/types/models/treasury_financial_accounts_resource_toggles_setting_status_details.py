import pydantic
import typing
import typing_extensions


class TreasuryFinancialAccountsResourceTogglesSettingStatusDetails(pydantic.BaseModel):
    """
    Additional details on the FinancialAccount Features information.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: typing_extensions.Literal[
        "activating",
        "capability_not_requested",
        "financial_account_closed",
        "rejected_other",
        "rejected_unsupported_business",
        "requirements_past_due",
        "requirements_pending_verification",
        "restricted_by_platform",
        "restricted_other",
    ] = pydantic.Field(
        alias="code",
    )
    """
    Represents the reason why the status is `pending` or `restricted`.
    """
    resolution: typing.Optional[
        typing_extensions.Literal[
            "contact_stripe", "provide_information", "remove_restriction"
        ]
    ] = pydantic.Field(alias="resolution", default=None)
    """
    Represents what the user should do, if anything, to activate the Feature.
    """
    restriction: typing.Optional[
        typing_extensions.Literal["inbound_flows", "outbound_flows"]
    ] = pydantic.Field(alias="restriction", default=None)
    """
    The `platform_restrictions` that are restricting this Feature.
    """
