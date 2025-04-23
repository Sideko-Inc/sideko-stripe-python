import httpx
import typing

from sideko_stripe.core import AsyncBaseClient, AuthBearer, SyncBaseClient
from sideko_stripe.environment import Environment
from sideko_stripe.resources.account import AccountClient, AsyncAccountClient
from sideko_stripe.resources.account_link import (
    AccountLinkClient,
    AsyncAccountLinkClient,
)
from sideko_stripe.resources.account_sessions import (
    AccountSessionsClient,
    AsyncAccountSessionsClient,
)
from sideko_stripe.resources.apple_pay import ApplePayClient, AsyncApplePayClient
from sideko_stripe.resources.application_fee import (
    ApplicationFeeClient,
    AsyncApplicationFeeClient,
)
from sideko_stripe.resources.apps import AppsClient, AsyncAppsClient
from sideko_stripe.resources.balance import AsyncBalanceClient, BalanceClient
from sideko_stripe.resources.balance_transaction import (
    AsyncBalanceTransactionClient,
    BalanceTransactionClient,
)
from sideko_stripe.resources.billing import AsyncBillingClient, BillingClient
from sideko_stripe.resources.billing_portal import (
    AsyncBillingPortalClient,
    BillingPortalClient,
)
from sideko_stripe.resources.charge import AsyncChargeClient, ChargeClient
from sideko_stripe.resources.checkout import AsyncCheckoutClient, CheckoutClient
from sideko_stripe.resources.climate import AsyncClimateClient, ClimateClient
from sideko_stripe.resources.confirmation_token import (
    AsyncConfirmationTokenClient,
    ConfirmationTokenClient,
)
from sideko_stripe.resources.country_spec import (
    AsyncCountrySpecClient,
    CountrySpecClient,
)
from sideko_stripe.resources.coupon import AsyncCouponClient, CouponClient
from sideko_stripe.resources.credit_note import AsyncCreditNoteClient, CreditNoteClient
from sideko_stripe.resources.customer import AsyncCustomerClient, CustomerClient
from sideko_stripe.resources.customer_session import (
    AsyncCustomerSessionClient,
    CustomerSessionClient,
)
from sideko_stripe.resources.dispute import AsyncDisputeClient, DisputeClient
from sideko_stripe.resources.entitlement import (
    AsyncEntitlementClient,
    EntitlementClient,
)
from sideko_stripe.resources.ephemeral_key import (
    AsyncEphemeralKeyClient,
    EphemeralKeyClient,
)
from sideko_stripe.resources.event import AsyncEventClient, EventClient
from sideko_stripe.resources.exchange_rate import (
    AsyncExchangeRateClient,
    ExchangeRateClient,
)
from sideko_stripe.resources.external_account import (
    AsyncExternalAccountClient,
    ExternalAccountClient,
)
from sideko_stripe.resources.file import AsyncFileClient, FileClient
from sideko_stripe.resources.file_link import AsyncFileLinkClient, FileLinkClient
from sideko_stripe.resources.financial_connections import (
    AsyncFinancialConnectionsClient,
    FinancialConnectionsClient,
)
from sideko_stripe.resources.forwarding import AsyncForwardingClient, ForwardingClient
from sideko_stripe.resources.identity import AsyncIdentityClient, IdentityClient
from sideko_stripe.resources.invoice import AsyncInvoiceClient, InvoiceClient
from sideko_stripe.resources.invoice_item import (
    AsyncInvoiceItemClient,
    InvoiceItemClient,
)
from sideko_stripe.resources.invoice_payment import (
    AsyncInvoicePaymentClient,
    InvoicePaymentClient,
)
from sideko_stripe.resources.invoice_rendering_template import (
    AsyncInvoiceRenderingTemplateClient,
    InvoiceRenderingTemplateClient,
)
from sideko_stripe.resources.issuing import AsyncIssuingClient, IssuingClient
from sideko_stripe.resources.link_account_session import (
    AsyncLinkAccountSessionClient,
    LinkAccountSessionClient,
)
from sideko_stripe.resources.linked_account import (
    AsyncLinkedAccountClient,
    LinkedAccountClient,
)
from sideko_stripe.resources.mandates import AsyncMandatesClient, MandatesClient
from sideko_stripe.resources.payment_intent import (
    AsyncPaymentIntentClient,
    PaymentIntentClient,
)
from sideko_stripe.resources.payment_link import (
    AsyncPaymentLinkClient,
    PaymentLinkClient,
)
from sideko_stripe.resources.payment_links import (
    AsyncPaymentLinksClient,
    PaymentLinksClient,
)
from sideko_stripe.resources.payment_method import (
    AsyncPaymentMethodClient,
    PaymentMethodClient,
)
from sideko_stripe.resources.payment_method_configuration import (
    AsyncPaymentMethodConfigurationClient,
    PaymentMethodConfigurationClient,
)
from sideko_stripe.resources.payment_method_domain import (
    AsyncPaymentMethodDomainClient,
    PaymentMethodDomainClient,
)
from sideko_stripe.resources.payout import AsyncPayoutClient, PayoutClient
from sideko_stripe.resources.plan import AsyncPlanClient, PlanClient
from sideko_stripe.resources.price import AsyncPriceClient, PriceClient
from sideko_stripe.resources.product import AsyncProductClient, ProductClient
from sideko_stripe.resources.promotion_code import (
    AsyncPromotionCodeClient,
    PromotionCodeClient,
)
from sideko_stripe.resources.quote import AsyncQuoteClient, QuoteClient
from sideko_stripe.resources.quotes import AsyncQuotesClient, QuotesClient
from sideko_stripe.resources.radar import AsyncRadarClient, RadarClient
from sideko_stripe.resources.refund import AsyncRefundClient, RefundClient
from sideko_stripe.resources.reporting import AsyncReportingClient, ReportingClient
from sideko_stripe.resources.review import AsyncReviewClient, ReviewClient
from sideko_stripe.resources.setup_attempt import (
    AsyncSetupAttemptClient,
    SetupAttemptClient,
)
from sideko_stripe.resources.setup_intent import (
    AsyncSetupIntentClient,
    SetupIntentClient,
)
from sideko_stripe.resources.shipping_rate import (
    AsyncShippingRateClient,
    ShippingRateClient,
)
from sideko_stripe.resources.sigma import AsyncSigmaClient, SigmaClient
from sideko_stripe.resources.source import AsyncSourceClient, SourceClient
from sideko_stripe.resources.subscription import (
    AsyncSubscriptionClient,
    SubscriptionClient,
)
from sideko_stripe.resources.subscription_item import (
    AsyncSubscriptionItemClient,
    SubscriptionItemClient,
)
from sideko_stripe.resources.subscription_schedule import (
    AsyncSubscriptionScheduleClient,
    SubscriptionScheduleClient,
)
from sideko_stripe.resources.subscriptions import (
    AsyncSubscriptionsClient,
    SubscriptionsClient,
)
from sideko_stripe.resources.tax import AsyncTaxClient, TaxClient
from sideko_stripe.resources.tax_code import AsyncTaxCodeClient, TaxCodeClient
from sideko_stripe.resources.tax_id import AsyncTaxIdClient, TaxIdClient
from sideko_stripe.resources.tax_rate import AsyncTaxRateClient, TaxRateClient
from sideko_stripe.resources.terminal import AsyncTerminalClient, TerminalClient
from sideko_stripe.resources.test_helper import AsyncTestHelperClient, TestHelperClient
from sideko_stripe.resources.token import AsyncTokenClient, TokenClient
from sideko_stripe.resources.topups import AsyncTopupsClient, TopupsClient
from sideko_stripe.resources.transfer import AsyncTransferClient, TransferClient
from sideko_stripe.resources.transfers import AsyncTransfersClient, TransfersClient
from sideko_stripe.resources.treasury import AsyncTreasuryClient, TreasuryClient
from sideko_stripe.resources.v1 import AsyncV1Client, V1Client
from sideko_stripe.resources.webhook_endpoints import (
    AsyncWebhookEndpointsClient,
    WebhookEndpointsClient,
)


class Stripe:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("bearerAuth", AuthBearer(val=token))
        self.account = AccountClient(base_client=self._base_client)
        self.apple_pay = ApplePayClient(base_client=self._base_client)
        self.coupon = CouponClient(base_client=self._base_client)
        self.customer = CustomerClient(base_client=self._base_client)
        self.ephemeral_key = EphemeralKeyClient(base_client=self._base_client)
        self.invoice_item = InvoiceItemClient(base_client=self._base_client)
        self.invoice = InvoiceClient(base_client=self._base_client)
        self.plan = PlanClient(base_client=self._base_client)
        self.product = ProductClient(base_client=self._base_client)
        self.radar = RadarClient(base_client=self._base_client)
        self.subscription_item = SubscriptionItemClient(base_client=self._base_client)
        self.subscription = SubscriptionClient(base_client=self._base_client)
        self.subscriptions = SubscriptionsClient(base_client=self._base_client)
        self.tax_id = TaxIdClient(base_client=self._base_client)
        self.terminal = TerminalClient(base_client=self._base_client)
        self.test_helper = TestHelperClient(base_client=self._base_client)
        self.webhook_endpoints = WebhookEndpointsClient(base_client=self._base_client)
        self.application_fee = ApplicationFeeClient(base_client=self._base_client)
        self.apps = AppsClient(base_client=self._base_client)
        self.balance = BalanceClient(base_client=self._base_client)
        self.balance_transaction = BalanceTransactionClient(
            base_client=self._base_client
        )
        self.billing = BillingClient(base_client=self._base_client)
        self.billing_portal = BillingPortalClient(base_client=self._base_client)
        self.charge = ChargeClient(base_client=self._base_client)
        self.checkout = CheckoutClient(base_client=self._base_client)
        self.climate = ClimateClient(base_client=self._base_client)
        self.v1 = V1Client(base_client=self._base_client)
        self.confirmation_token = ConfirmationTokenClient(base_client=self._base_client)
        self.country_spec = CountrySpecClient(base_client=self._base_client)
        self.credit_note = CreditNoteClient(base_client=self._base_client)
        self.dispute = DisputeClient(base_client=self._base_client)
        self.entitlement = EntitlementClient(base_client=self._base_client)
        self.event = EventClient(base_client=self._base_client)
        self.exchange_rate = ExchangeRateClient(base_client=self._base_client)
        self.file_link = FileLinkClient(base_client=self._base_client)
        self.file = FileClient(base_client=self._base_client)
        self.financial_connections = FinancialConnectionsClient(
            base_client=self._base_client
        )
        self.forwarding = ForwardingClient(base_client=self._base_client)
        self.identity = IdentityClient(base_client=self._base_client)
        self.invoice_payment = InvoicePaymentClient(base_client=self._base_client)
        self.invoice_rendering_template = InvoiceRenderingTemplateClient(
            base_client=self._base_client
        )
        self.issuing = IssuingClient(base_client=self._base_client)
        self.link_account_session = LinkAccountSessionClient(
            base_client=self._base_client
        )
        self.linked_account = LinkedAccountClient(base_client=self._base_client)
        self.mandates = MandatesClient(base_client=self._base_client)
        self.payment_intent = PaymentIntentClient(base_client=self._base_client)
        self.payment_link = PaymentLinkClient(base_client=self._base_client)
        self.payment_links = PaymentLinksClient(base_client=self._base_client)
        self.payment_method_configuration = PaymentMethodConfigurationClient(
            base_client=self._base_client
        )
        self.payment_method_domain = PaymentMethodDomainClient(
            base_client=self._base_client
        )
        self.payment_method = PaymentMethodClient(base_client=self._base_client)
        self.payout = PayoutClient(base_client=self._base_client)
        self.price = PriceClient(base_client=self._base_client)
        self.promotion_code = PromotionCodeClient(base_client=self._base_client)
        self.quote = QuoteClient(base_client=self._base_client)
        self.quotes = QuotesClient(base_client=self._base_client)
        self.refund = RefundClient(base_client=self._base_client)
        self.reporting = ReportingClient(base_client=self._base_client)
        self.review = ReviewClient(base_client=self._base_client)
        self.setup_attempt = SetupAttemptClient(base_client=self._base_client)
        self.setup_intent = SetupIntentClient(base_client=self._base_client)
        self.shipping_rate = ShippingRateClient(base_client=self._base_client)
        self.sigma = SigmaClient(base_client=self._base_client)
        self.source = SourceClient(base_client=self._base_client)
        self.subscription_schedule = SubscriptionScheduleClient(
            base_client=self._base_client
        )
        self.tax = TaxClient(base_client=self._base_client)
        self.tax_code = TaxCodeClient(base_client=self._base_client)
        self.tax_rate = TaxRateClient(base_client=self._base_client)
        self.token = TokenClient(base_client=self._base_client)
        self.topups = TopupsClient(base_client=self._base_client)
        self.transfer = TransferClient(base_client=self._base_client)
        self.transfers = TransfersClient(base_client=self._base_client)
        self.treasury = TreasuryClient(base_client=self._base_client)
        self.account_link = AccountLinkClient(base_client=self._base_client)
        self.account_sessions = AccountSessionsClient(base_client=self._base_client)
        self.customer_session = CustomerSessionClient(base_client=self._base_client)
        self.external_account = ExternalAccountClient(base_client=self._base_client)


class AsyncStripe:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("bearerAuth", AuthBearer(val=token))
        self.account = AsyncAccountClient(base_client=self._base_client)
        self.apple_pay = AsyncApplePayClient(base_client=self._base_client)
        self.coupon = AsyncCouponClient(base_client=self._base_client)
        self.customer = AsyncCustomerClient(base_client=self._base_client)
        self.ephemeral_key = AsyncEphemeralKeyClient(base_client=self._base_client)
        self.invoice_item = AsyncInvoiceItemClient(base_client=self._base_client)
        self.invoice = AsyncInvoiceClient(base_client=self._base_client)
        self.plan = AsyncPlanClient(base_client=self._base_client)
        self.product = AsyncProductClient(base_client=self._base_client)
        self.radar = AsyncRadarClient(base_client=self._base_client)
        self.subscription_item = AsyncSubscriptionItemClient(
            base_client=self._base_client
        )
        self.subscription = AsyncSubscriptionClient(base_client=self._base_client)
        self.subscriptions = AsyncSubscriptionsClient(base_client=self._base_client)
        self.tax_id = AsyncTaxIdClient(base_client=self._base_client)
        self.terminal = AsyncTerminalClient(base_client=self._base_client)
        self.test_helper = AsyncTestHelperClient(base_client=self._base_client)
        self.webhook_endpoints = AsyncWebhookEndpointsClient(
            base_client=self._base_client
        )
        self.application_fee = AsyncApplicationFeeClient(base_client=self._base_client)
        self.apps = AsyncAppsClient(base_client=self._base_client)
        self.balance = AsyncBalanceClient(base_client=self._base_client)
        self.balance_transaction = AsyncBalanceTransactionClient(
            base_client=self._base_client
        )
        self.billing = AsyncBillingClient(base_client=self._base_client)
        self.billing_portal = AsyncBillingPortalClient(base_client=self._base_client)
        self.charge = AsyncChargeClient(base_client=self._base_client)
        self.checkout = AsyncCheckoutClient(base_client=self._base_client)
        self.climate = AsyncClimateClient(base_client=self._base_client)
        self.v1 = AsyncV1Client(base_client=self._base_client)
        self.confirmation_token = AsyncConfirmationTokenClient(
            base_client=self._base_client
        )
        self.country_spec = AsyncCountrySpecClient(base_client=self._base_client)
        self.credit_note = AsyncCreditNoteClient(base_client=self._base_client)
        self.dispute = AsyncDisputeClient(base_client=self._base_client)
        self.entitlement = AsyncEntitlementClient(base_client=self._base_client)
        self.event = AsyncEventClient(base_client=self._base_client)
        self.exchange_rate = AsyncExchangeRateClient(base_client=self._base_client)
        self.file_link = AsyncFileLinkClient(base_client=self._base_client)
        self.file = AsyncFileClient(base_client=self._base_client)
        self.financial_connections = AsyncFinancialConnectionsClient(
            base_client=self._base_client
        )
        self.forwarding = AsyncForwardingClient(base_client=self._base_client)
        self.identity = AsyncIdentityClient(base_client=self._base_client)
        self.invoice_payment = AsyncInvoicePaymentClient(base_client=self._base_client)
        self.invoice_rendering_template = AsyncInvoiceRenderingTemplateClient(
            base_client=self._base_client
        )
        self.issuing = AsyncIssuingClient(base_client=self._base_client)
        self.link_account_session = AsyncLinkAccountSessionClient(
            base_client=self._base_client
        )
        self.linked_account = AsyncLinkedAccountClient(base_client=self._base_client)
        self.mandates = AsyncMandatesClient(base_client=self._base_client)
        self.payment_intent = AsyncPaymentIntentClient(base_client=self._base_client)
        self.payment_link = AsyncPaymentLinkClient(base_client=self._base_client)
        self.payment_links = AsyncPaymentLinksClient(base_client=self._base_client)
        self.payment_method_configuration = AsyncPaymentMethodConfigurationClient(
            base_client=self._base_client
        )
        self.payment_method_domain = AsyncPaymentMethodDomainClient(
            base_client=self._base_client
        )
        self.payment_method = AsyncPaymentMethodClient(base_client=self._base_client)
        self.payout = AsyncPayoutClient(base_client=self._base_client)
        self.price = AsyncPriceClient(base_client=self._base_client)
        self.promotion_code = AsyncPromotionCodeClient(base_client=self._base_client)
        self.quote = AsyncQuoteClient(base_client=self._base_client)
        self.quotes = AsyncQuotesClient(base_client=self._base_client)
        self.refund = AsyncRefundClient(base_client=self._base_client)
        self.reporting = AsyncReportingClient(base_client=self._base_client)
        self.review = AsyncReviewClient(base_client=self._base_client)
        self.setup_attempt = AsyncSetupAttemptClient(base_client=self._base_client)
        self.setup_intent = AsyncSetupIntentClient(base_client=self._base_client)
        self.shipping_rate = AsyncShippingRateClient(base_client=self._base_client)
        self.sigma = AsyncSigmaClient(base_client=self._base_client)
        self.source = AsyncSourceClient(base_client=self._base_client)
        self.subscription_schedule = AsyncSubscriptionScheduleClient(
            base_client=self._base_client
        )
        self.tax = AsyncTaxClient(base_client=self._base_client)
        self.tax_code = AsyncTaxCodeClient(base_client=self._base_client)
        self.tax_rate = AsyncTaxRateClient(base_client=self._base_client)
        self.token = AsyncTokenClient(base_client=self._base_client)
        self.topups = AsyncTopupsClient(base_client=self._base_client)
        self.transfer = AsyncTransferClient(base_client=self._base_client)
        self.transfers = AsyncTransfersClient(base_client=self._base_client)
        self.treasury = AsyncTreasuryClient(base_client=self._base_client)
        self.account_link = AsyncAccountLinkClient(base_client=self._base_client)
        self.account_sessions = AsyncAccountSessionsClient(
            base_client=self._base_client
        )
        self.customer_session = AsyncCustomerSessionClient(
            base_client=self._base_client
        )
        self.external_account = AsyncExternalAccountClient(
            base_client=self._base_client
        )


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
