
# Stripe API Python SDK

## Overview
The Stripe REST API. Please see https://stripe.com/docs/api for more details.

### Synchronous Client

```python
from os import getenv
from sideko_stripe import Stripe

client = Stripe(
    token=getenv("API_TOKEN"),
)
```

### Asynchronous Client

```python
from os import getenv
from sideko_stripe import AsyncStripe

client = AsyncStripe(
    token=getenv("API_TOKEN"),
)
```

## Module Documentation and Snippets

### [account](sideko_stripe/resources/account/README.md)

* [create](sideko_stripe/resources/account/README.md#create) - POST /v1/accounts
* [create_login_link](sideko_stripe/resources/account/README.md#create_login_link) - Create a login link
* [delete](sideko_stripe/resources/account/README.md#delete) - Delete an account
* [details](sideko_stripe/resources/account/README.md#details) - Retrieve account
* [get](sideko_stripe/resources/account/README.md#get) - Retrieve account
* [list](sideko_stripe/resources/account/README.md#list) - List all connected accounts
* [reject](sideko_stripe/resources/account/README.md#reject) - Reject an account
* [update](sideko_stripe/resources/account/README.md#update) - Update an account

### [account.bank_account](sideko_stripe/resources/account/bank_account/README.md)

* [create](sideko_stripe/resources/account/bank_account/README.md#create) - Create an external account
* [delete](sideko_stripe/resources/account/bank_account/README.md#delete) - Delete an external account
* [get](sideko_stripe/resources/account/bank_account/README.md#get) - Retrieve an external account
* [update](sideko_stripe/resources/account/bank_account/README.md#update) - POST /v1/accounts/{account}/bank_accounts/{id}

### [account.capability](sideko_stripe/resources/account/capability/README.md)

* [create](sideko_stripe/resources/account/capability/README.md#create) - Update an Account Capability
* [get](sideko_stripe/resources/account/capability/README.md#get) - Retrieve an Account Capability
* [list](sideko_stripe/resources/account/capability/README.md#list) - List all account capabilities

### [account.external_account](sideko_stripe/resources/account/external_account/README.md)

* [create](sideko_stripe/resources/account/external_account/README.md#create) - Create an external account
* [delete](sideko_stripe/resources/account/external_account/README.md#delete) - Delete an external account
* [get](sideko_stripe/resources/account/external_account/README.md#get) - Retrieve an external account
* [list](sideko_stripe/resources/account/external_account/README.md#list) - List all external accounts
* [update](sideko_stripe/resources/account/external_account/README.md#update) - POST /v1/accounts/{account}/external_accounts/{id}

### [account.people](sideko_stripe/resources/account/people/README.md)

* [create](sideko_stripe/resources/account/people/README.md#create) - Create a person
* [delete](sideko_stripe/resources/account/people/README.md#delete) - Delete a person
* [get](sideko_stripe/resources/account/people/README.md#get) - Retrieve a person
* [list](sideko_stripe/resources/account/people/README.md#list) - List all persons
* [update](sideko_stripe/resources/account/people/README.md#update) - Update a person

### [account.person](sideko_stripe/resources/account/person/README.md)

* [create](sideko_stripe/resources/account/person/README.md#create) - Create a person
* [delete](sideko_stripe/resources/account/person/README.md#delete) - Delete a person
* [get](sideko_stripe/resources/account/person/README.md#get) - Retrieve a person
* [list](sideko_stripe/resources/account/person/README.md#list) - List all persons
* [update](sideko_stripe/resources/account/person/README.md#update) - Update a person

### [account_link](sideko_stripe/resources/account_link/README.md)

* [create](sideko_stripe/resources/account_link/README.md#create) - Create an account link

### [account_sessions](sideko_stripe/resources/account_sessions/README.md)

* [create](sideko_stripe/resources/account_sessions/README.md#create) - Create an Account Session

### [apple_pay.domain](sideko_stripe/resources/apple_pay/domain/README.md)

* [create](sideko_stripe/resources/apple_pay/domain/README.md#create) - POST /v1/apple_pay/domains
* [delete](sideko_stripe/resources/apple_pay/domain/README.md#delete) - DELETE /v1/apple_pay/domains/{domain}
* [get](sideko_stripe/resources/apple_pay/domain/README.md#get) - GET /v1/apple_pay/domains/{domain}
* [list](sideko_stripe/resources/apple_pay/domain/README.md#list) - GET /v1/apple_pay/domains

### [application_fee](sideko_stripe/resources/application_fee/README.md)

* [get](sideko_stripe/resources/application_fee/README.md#get) - Retrieve an application fee
* [list](sideko_stripe/resources/application_fee/README.md#list) - List all application fees

### [application_fee.refund](sideko_stripe/resources/application_fee/refund/README.md)

* [create](sideko_stripe/resources/application_fee/refund/README.md#create) - POST /v1/application_fees/{id}/refund
* [create_many](sideko_stripe/resources/application_fee/refund/README.md#create_many) - Create an application fee refund
* [get](sideko_stripe/resources/application_fee/refund/README.md#get) - Retrieve an application fee refund
* [list](sideko_stripe/resources/application_fee/refund/README.md#list) - List all application fee refunds
* [update](sideko_stripe/resources/application_fee/refund/README.md#update) - Update an application fee refund

### [apps.secret](sideko_stripe/resources/apps/secret/README.md)

* [create](sideko_stripe/resources/apps/secret/README.md#create) - Set a Secret
* [delete](sideko_stripe/resources/apps/secret/README.md#delete) - Delete a Secret
* [find](sideko_stripe/resources/apps/secret/README.md#find) - Find a Secret
* [list](sideko_stripe/resources/apps/secret/README.md#list) - List secrets

### [balance](sideko_stripe/resources/balance/README.md)

* [list](sideko_stripe/resources/balance/README.md#list) - Retrieve balance

### [balance.history](sideko_stripe/resources/balance/history/README.md)

* [get](sideko_stripe/resources/balance/history/README.md#get) - Retrieve a balance transaction
* [list](sideko_stripe/resources/balance/history/README.md#list) - List all balance transactions

### [balance_transaction](sideko_stripe/resources/balance_transaction/README.md)

* [get](sideko_stripe/resources/balance_transaction/README.md#get) - Retrieve a balance transaction
* [list](sideko_stripe/resources/balance_transaction/README.md#list) - List all balance transactions

### [billing.alert](sideko_stripe/resources/billing/alert/README.md)

* [activate](sideko_stripe/resources/billing/alert/README.md#activate) - Activate a billing alert
* [archive](sideko_stripe/resources/billing/alert/README.md#archive) - Archive a billing alert
* [create](sideko_stripe/resources/billing/alert/README.md#create) - Create a billing alert
* [deactivate](sideko_stripe/resources/billing/alert/README.md#deactivate) - Deactivate a billing alert
* [get](sideko_stripe/resources/billing/alert/README.md#get) - Retrieve a billing alert
* [list](sideko_stripe/resources/billing/alert/README.md#list) - List billing alerts

### [billing.credit_balance_summary](sideko_stripe/resources/billing/credit_balance_summary/README.md)

* [get](sideko_stripe/resources/billing/credit_balance_summary/README.md#get) - Retrieve the credit balance summary for a customer

### [billing.credit_balance_transaction](sideko_stripe/resources/billing/credit_balance_transaction/README.md)

* [get](sideko_stripe/resources/billing/credit_balance_transaction/README.md#get) - Retrieve a credit balance transaction
* [list](sideko_stripe/resources/billing/credit_balance_transaction/README.md#list) - List credit balance transactions

### [billing.credit_grant](sideko_stripe/resources/billing/credit_grant/README.md)

* [create](sideko_stripe/resources/billing/credit_grant/README.md#create) - Create a credit grant
* [expire](sideko_stripe/resources/billing/credit_grant/README.md#expire) - Expire a credit grant
* [get](sideko_stripe/resources/billing/credit_grant/README.md#get) - Retrieve a credit grant
* [list](sideko_stripe/resources/billing/credit_grant/README.md#list) - List credit grants
* [update](sideko_stripe/resources/billing/credit_grant/README.md#update) - Update a credit grant
* [void](sideko_stripe/resources/billing/credit_grant/README.md#void) - Void a credit grant

### [billing.meter](sideko_stripe/resources/billing/meter/README.md)

* [create](sideko_stripe/resources/billing/meter/README.md#create) - Create a billing meter
* [deactivate](sideko_stripe/resources/billing/meter/README.md#deactivate) - Deactivate a billing meter
* [get](sideko_stripe/resources/billing/meter/README.md#get) - Retrieve a billing meter
* [list](sideko_stripe/resources/billing/meter/README.md#list) - List billing meters
* [reactivate](sideko_stripe/resources/billing/meter/README.md#reactivate) - Reactivate a billing meter
* [update](sideko_stripe/resources/billing/meter/README.md#update) - Update a billing meter

### [billing.meter.event_summaries](sideko_stripe/resources/billing/meter/event_summaries/README.md)

* [list](sideko_stripe/resources/billing/meter/event_summaries/README.md#list) - List billing meter event summaries

### [billing.meter_event](sideko_stripe/resources/billing/meter_event/README.md)

* [create](sideko_stripe/resources/billing/meter_event/README.md#create) - Create a billing meter event

### [billing.meter_event_adjustment](sideko_stripe/resources/billing/meter_event_adjustment/README.md)

* [create](sideko_stripe/resources/billing/meter_event_adjustment/README.md#create) - Create a billing meter event adjustment

### [billing_portal.configuration](sideko_stripe/resources/billing_portal/configuration/README.md)

* [create](sideko_stripe/resources/billing_portal/configuration/README.md#create) - Create a portal configuration
* [get](sideko_stripe/resources/billing_portal/configuration/README.md#get) - Retrieve a portal configuration
* [list](sideko_stripe/resources/billing_portal/configuration/README.md#list) - List portal configurations
* [update](sideko_stripe/resources/billing_portal/configuration/README.md#update) - Update a portal configuration

### [billing_portal.session](sideko_stripe/resources/billing_portal/session/README.md)

* [create](sideko_stripe/resources/billing_portal/session/README.md#create) - Create a portal session

### [charge](sideko_stripe/resources/charge/README.md)

* [capture](sideko_stripe/resources/charge/README.md#capture) - Capture a payment
* [create](sideko_stripe/resources/charge/README.md#create) - POST /v1/charges
* [get](sideko_stripe/resources/charge/README.md#get) - Retrieve a charge
* [list](sideko_stripe/resources/charge/README.md#list) - List all charges
* [search](sideko_stripe/resources/charge/README.md#search) - Search charges
* [update](sideko_stripe/resources/charge/README.md#update) - Update a charge

### [charge.dispute](sideko_stripe/resources/charge/dispute/README.md)

* [close](sideko_stripe/resources/charge/dispute/README.md#close) - POST /v1/charges/{charge}/dispute/close
* [create](sideko_stripe/resources/charge/dispute/README.md#create) - POST /v1/charges/{charge}/dispute
* [get](sideko_stripe/resources/charge/dispute/README.md#get) - GET /v1/charges/{charge}/dispute

### [charge.refund](sideko_stripe/resources/charge/refund/README.md)

* [create](sideko_stripe/resources/charge/refund/README.md#create) - Create a refund
* [create_1](sideko_stripe/resources/charge/refund/README.md#create_1) - Create customer balance refund
* [get](sideko_stripe/resources/charge/refund/README.md#get) - GET /v1/charges/{charge}/refunds/{refund}
* [list](sideko_stripe/resources/charge/refund/README.md#list) - List all refunds
* [update](sideko_stripe/resources/charge/refund/README.md#update) - POST /v1/charges/{charge}/refunds/{refund}

### [checkout.session](sideko_stripe/resources/checkout/session/README.md)

* [create](sideko_stripe/resources/checkout/session/README.md#create) - Create a Checkout Session
* [expire](sideko_stripe/resources/checkout/session/README.md#expire) - Expire a Checkout Session
* [get](sideko_stripe/resources/checkout/session/README.md#get) - Retrieve a Checkout Session
* [list](sideko_stripe/resources/checkout/session/README.md#list) - List all Checkout Sessions
* [update](sideko_stripe/resources/checkout/session/README.md#update) - Update a Checkout Session

### [checkout.session.line_items](sideko_stripe/resources/checkout/session/line_items/README.md)

* [list](sideko_stripe/resources/checkout/session/line_items/README.md#list) - Retrieve a Checkout Session's line items

### [climate.order](sideko_stripe/resources/climate/order/README.md)

* [cancel](sideko_stripe/resources/climate/order/README.md#cancel) - Cancel an order
* [create](sideko_stripe/resources/climate/order/README.md#create) - Create an order
* [get](sideko_stripe/resources/climate/order/README.md#get) - Retrieve an order
* [list](sideko_stripe/resources/climate/order/README.md#list) - List orders
* [update](sideko_stripe/resources/climate/order/README.md#update) - Update an order

### [climate.product](sideko_stripe/resources/climate/product/README.md)

* [get](sideko_stripe/resources/climate/product/README.md#get) - Retrieve a product
* [list](sideko_stripe/resources/climate/product/README.md#list) - List products

### [climate.suppliers](sideko_stripe/resources/climate/suppliers/README.md)

* [get](sideko_stripe/resources/climate/suppliers/README.md#get) - Retrieve a supplier

### [confirmation_token](sideko_stripe/resources/confirmation_token/README.md)

* [get](sideko_stripe/resources/confirmation_token/README.md#get) - Retrieve a ConfirmationToken

### [country_spec](sideko_stripe/resources/country_spec/README.md)

* [get](sideko_stripe/resources/country_spec/README.md#get) - Retrieve a Country Spec
* [list](sideko_stripe/resources/country_spec/README.md#list) - List Country Specs

### [coupon](sideko_stripe/resources/coupon/README.md)

* [create](sideko_stripe/resources/coupon/README.md#create) - Create a coupon
* [delete](sideko_stripe/resources/coupon/README.md#delete) - Delete a coupon
* [get](sideko_stripe/resources/coupon/README.md#get) - Retrieve a coupon
* [list](sideko_stripe/resources/coupon/README.md#list) - List all coupons
* [update](sideko_stripe/resources/coupon/README.md#update) - Update a coupon

### [credit_note](sideko_stripe/resources/credit_note/README.md)

* [create](sideko_stripe/resources/credit_note/README.md#create) - Create a credit note
* [get](sideko_stripe/resources/credit_note/README.md#get) - Retrieve a credit note
* [lines](sideko_stripe/resources/credit_note/README.md#lines) - Retrieve a credit note's line items
* [list](sideko_stripe/resources/credit_note/README.md#list) - List all credit notes
* [preview](sideko_stripe/resources/credit_note/README.md#preview) - Preview a credit note
* [preview_lines](sideko_stripe/resources/credit_note/README.md#preview_lines) - Retrieve a credit note preview's line items
* [update](sideko_stripe/resources/credit_note/README.md#update) - Update a credit note
* [void](sideko_stripe/resources/credit_note/README.md#void) - Void a credit note

### [customer](sideko_stripe/resources/customer/README.md)

* [create](sideko_stripe/resources/customer/README.md#create) - Create a customer
* [delete](sideko_stripe/resources/customer/README.md#delete) - Delete a customer
* [get](sideko_stripe/resources/customer/README.md#get) - Retrieve a customer
* [list](sideko_stripe/resources/customer/README.md#list) - List all customers
* [search](sideko_stripe/resources/customer/README.md#search) - Search customers
* [update](sideko_stripe/resources/customer/README.md#update) - Update a customer

### [customer.balance_transaction](sideko_stripe/resources/customer/balance_transaction/README.md)

* [create](sideko_stripe/resources/customer/balance_transaction/README.md#create) - Create a customer balance transaction
* [get](sideko_stripe/resources/customer/balance_transaction/README.md#get) - Retrieve a customer balance transaction
* [list](sideko_stripe/resources/customer/balance_transaction/README.md#list) - List customer balance transactions
* [update](sideko_stripe/resources/customer/balance_transaction/README.md#update) - Update a customer credit balance transaction

### [customer.bank_account](sideko_stripe/resources/customer/bank_account/README.md)

* [create](sideko_stripe/resources/customer/bank_account/README.md#create) - Create a card
* [delete](sideko_stripe/resources/customer/bank_account/README.md#delete) - Delete a customer source
* [get](sideko_stripe/resources/customer/bank_account/README.md#get) - Retrieve a bank account
* [list](sideko_stripe/resources/customer/bank_account/README.md#list) - List all bank accounts
* [update](sideko_stripe/resources/customer/bank_account/README.md#update) - POST /v1/customers/{customer}/bank_accounts/{id}
* [verify](sideko_stripe/resources/customer/bank_account/README.md#verify) - Verify a bank account

### [customer.card](sideko_stripe/resources/customer/card/README.md)

* [create](sideko_stripe/resources/customer/card/README.md#create) - Create a card
* [delete](sideko_stripe/resources/customer/card/README.md#delete) - Delete a customer source
* [get](sideko_stripe/resources/customer/card/README.md#get) - Retrieve a card
* [list](sideko_stripe/resources/customer/card/README.md#list) - List all cards
* [update](sideko_stripe/resources/customer/card/README.md#update) - POST /v1/customers/{customer}/cards/{id}

### [customer.cash_balance](sideko_stripe/resources/customer/cash_balance/README.md)

* [get](sideko_stripe/resources/customer/cash_balance/README.md#get) - Retrieve a cash balance
* [modify](sideko_stripe/resources/customer/cash_balance/README.md#modify) - Update a cash balance's settings

### [customer.cash_balance_transaction](sideko_stripe/resources/customer/cash_balance_transaction/README.md)

* [get](sideko_stripe/resources/customer/cash_balance_transaction/README.md#get) - Retrieve a cash balance transaction
* [list](sideko_stripe/resources/customer/cash_balance_transaction/README.md#list) - List cash balance transactions

### [customer.discount](sideko_stripe/resources/customer/discount/README.md)

* [delete](sideko_stripe/resources/customer/discount/README.md#delete) - Delete a customer discount
* [list](sideko_stripe/resources/customer/discount/README.md#list) - GET /v1/customers/{customer}/discount

### [customer.funding_instruction](sideko_stripe/resources/customer/funding_instruction/README.md)

* [create](sideko_stripe/resources/customer/funding_instruction/README.md#create) - Create or retrieve funding instructions for a customer cash balance

### [customer.payment_method](sideko_stripe/resources/customer/payment_method/README.md)

* [get](sideko_stripe/resources/customer/payment_method/README.md#get) - Retrieve a Customer's PaymentMethod
* [list](sideko_stripe/resources/customer/payment_method/README.md#list) - List a Customer's PaymentMethods

### [customer.source](sideko_stripe/resources/customer/source/README.md)

* [create](sideko_stripe/resources/customer/source/README.md#create) - Create a card
* [delete](sideko_stripe/resources/customer/source/README.md#delete) - Delete a customer source
* [get](sideko_stripe/resources/customer/source/README.md#get) - GET /v1/customers/{customer}/sources/{id}
* [list](sideko_stripe/resources/customer/source/README.md#list) - GET /v1/customers/{customer}/sources
* [update](sideko_stripe/resources/customer/source/README.md#update) - POST /v1/customers/{customer}/sources/{id}
* [verify](sideko_stripe/resources/customer/source/README.md#verify) - Verify a bank account

### [customer.subscription](sideko_stripe/resources/customer/subscription/README.md)

* [create](sideko_stripe/resources/customer/subscription/README.md#create) - Create a subscription
* [delete](sideko_stripe/resources/customer/subscription/README.md#delete) - Cancel a subscription
* [get](sideko_stripe/resources/customer/subscription/README.md#get) - Retrieve a subscription
* [list](sideko_stripe/resources/customer/subscription/README.md#list) - List active subscriptions
* [modify](sideko_stripe/resources/customer/subscription/README.md#modify) - Update a subscription on a customer

### [customer.subscription.discount](sideko_stripe/resources/customer/subscription/discount/README.md)

* [delete](sideko_stripe/resources/customer/subscription/discount/README.md#delete) - Delete a customer discount
* [list](sideko_stripe/resources/customer/subscription/discount/README.md#list) - GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount

### [customer.tax_id](sideko_stripe/resources/customer/tax_id/README.md)

* [create](sideko_stripe/resources/customer/tax_id/README.md#create) - Create a Customer tax ID
* [delete](sideko_stripe/resources/customer/tax_id/README.md#delete) - Delete a Customer tax ID
* [get](sideko_stripe/resources/customer/tax_id/README.md#get) - Retrieve a Customer tax ID
* [list](sideko_stripe/resources/customer/tax_id/README.md#list) - List all Customer tax IDs

### [customer_session](sideko_stripe/resources/customer_session/README.md)

* [create](sideko_stripe/resources/customer_session/README.md#create) - Create a Customer Session

### [dispute](sideko_stripe/resources/dispute/README.md)

* [close](sideko_stripe/resources/dispute/README.md#close) - Close a dispute
* [get](sideko_stripe/resources/dispute/README.md#get) - Retrieve a dispute
* [list](sideko_stripe/resources/dispute/README.md#list) - List all disputes
* [update](sideko_stripe/resources/dispute/README.md#update) - Update a dispute

### [entitlement.active_entitlement](sideko_stripe/resources/entitlement/active_entitlement/README.md)

* [get](sideko_stripe/resources/entitlement/active_entitlement/README.md#get) - Retrieve an active entitlement
* [list](sideko_stripe/resources/entitlement/active_entitlement/README.md#list) - List all active entitlements

### [entitlement.feature](sideko_stripe/resources/entitlement/feature/README.md)

* [create](sideko_stripe/resources/entitlement/feature/README.md#create) - Create a feature
* [get](sideko_stripe/resources/entitlement/feature/README.md#get) - Retrieve a feature
* [list](sideko_stripe/resources/entitlement/feature/README.md#list) - List all features
* [update](sideko_stripe/resources/entitlement/feature/README.md#update) - Updates a feature

### [ephemeral_key](sideko_stripe/resources/ephemeral_key/README.md)

* [create](sideko_stripe/resources/ephemeral_key/README.md#create) - Create an ephemeral key
* [delete](sideko_stripe/resources/ephemeral_key/README.md#delete) - Immediately invalidate an ephemeral key

### [event](sideko_stripe/resources/event/README.md)

* [get](sideko_stripe/resources/event/README.md#get) - Retrieve an event
* [list](sideko_stripe/resources/event/README.md#list) - List all events

### [exchange_rate](sideko_stripe/resources/exchange_rate/README.md)

* [get](sideko_stripe/resources/exchange_rate/README.md#get) - Retrieve an exchange rate
* [list](sideko_stripe/resources/exchange_rate/README.md#list) - List all exchange rates

### [external_account](sideko_stripe/resources/external_account/README.md)

* [create](sideko_stripe/resources/external_account/README.md#create) - POST /v1/external_accounts/{id}

### [file](sideko_stripe/resources/file/README.md)

* [create](sideko_stripe/resources/file/README.md#create) - Create a file
* [get](sideko_stripe/resources/file/README.md#get) - Retrieve a file
* [list](sideko_stripe/resources/file/README.md#list) - List all files

### [file_link](sideko_stripe/resources/file_link/README.md)

* [create](sideko_stripe/resources/file_link/README.md#create) - Create a file link
* [get](sideko_stripe/resources/file_link/README.md#get) - Retrieve a file link
* [list](sideko_stripe/resources/file_link/README.md#list) - List all file links
* [update](sideko_stripe/resources/file_link/README.md#update) - Update a file link

### [financial_connections.account](sideko_stripe/resources/financial_connections/account/README.md)

* [disconnect](sideko_stripe/resources/financial_connections/account/README.md#disconnect) - Disconnect an Account
* [get](sideko_stripe/resources/financial_connections/account/README.md#get) - Retrieve an Account
* [list](sideko_stripe/resources/financial_connections/account/README.md#list) - List Accounts
* [refresh](sideko_stripe/resources/financial_connections/account/README.md#refresh) - Refresh Account data
* [subscribe](sideko_stripe/resources/financial_connections/account/README.md#subscribe) - Subscribe to data refreshes for an Account
* [unsubscribe](sideko_stripe/resources/financial_connections/account/README.md#unsubscribe) - Unsubscribe from data refreshes for an Account

### [financial_connections.account.owners](sideko_stripe/resources/financial_connections/account/owners/README.md)

* [list](sideko_stripe/resources/financial_connections/account/owners/README.md#list) - List Account Owners

### [financial_connections.session](sideko_stripe/resources/financial_connections/session/README.md)

* [create](sideko_stripe/resources/financial_connections/session/README.md#create) - Create a Session
* [get](sideko_stripe/resources/financial_connections/session/README.md#get) - Retrieve a Session

### [financial_connections.transaction](sideko_stripe/resources/financial_connections/transaction/README.md)

* [get](sideko_stripe/resources/financial_connections/transaction/README.md#get) - Retrieve a Transaction
* [list](sideko_stripe/resources/financial_connections/transaction/README.md#list) - List Transactions

### [forwarding.request](sideko_stripe/resources/forwarding/request/README.md)

* [create](sideko_stripe/resources/forwarding/request/README.md#create) - Create a ForwardingRequest
* [get](sideko_stripe/resources/forwarding/request/README.md#get) - Retrieve a ForwardingRequest
* [list](sideko_stripe/resources/forwarding/request/README.md#list) - List all ForwardingRequests

### [identity.verification_report](sideko_stripe/resources/identity/verification_report/README.md)

* [get](sideko_stripe/resources/identity/verification_report/README.md#get) - Retrieve a VerificationReport
* [list](sideko_stripe/resources/identity/verification_report/README.md#list) - List VerificationReports

### [identity.verification_session](sideko_stripe/resources/identity/verification_session/README.md)

* [cancel](sideko_stripe/resources/identity/verification_session/README.md#cancel) - Cancel a VerificationSession
* [create](sideko_stripe/resources/identity/verification_session/README.md#create) - Create a VerificationSession
* [get](sideko_stripe/resources/identity/verification_session/README.md#get) - Retrieve a VerificationSession
* [list](sideko_stripe/resources/identity/verification_session/README.md#list) - List VerificationSessions
* [redact](sideko_stripe/resources/identity/verification_session/README.md#redact) - Redact a VerificationSession
* [update](sideko_stripe/resources/identity/verification_session/README.md#update) - Update a VerificationSession

### [invoice](sideko_stripe/resources/invoice/README.md)

* [create](sideko_stripe/resources/invoice/README.md#create) - Create an invoice
* [delete](sideko_stripe/resources/invoice/README.md#delete) - Delete a draft invoice
* [finalize](sideko_stripe/resources/invoice/README.md#finalize) - Finalize an invoice
* [get](sideko_stripe/resources/invoice/README.md#get) - Retrieve an invoice
* [list](sideko_stripe/resources/invoice/README.md#list) - List all invoices
* [mark_uncollectible](sideko_stripe/resources/invoice/README.md#mark_uncollectible) - Mark an invoice as uncollectible
* [pay](sideko_stripe/resources/invoice/README.md#pay) - Pay an invoice
* [preview](sideko_stripe/resources/invoice/README.md#preview) - Create a preview invoice
* [search](sideko_stripe/resources/invoice/README.md#search) - Search invoices
* [send](sideko_stripe/resources/invoice/README.md#send) - Send an invoice for manual payment
* [update](sideko_stripe/resources/invoice/README.md#update) - Update an invoice
* [void](sideko_stripe/resources/invoice/README.md#void) - Void an invoice

### [invoice.line](sideko_stripe/resources/invoice/line/README.md)

* [create_many](sideko_stripe/resources/invoice/line/README.md#create_many) - Bulk add invoice line items
* [list](sideko_stripe/resources/invoice/line/README.md#list) - Retrieve an invoice's line items
* [remove_many](sideko_stripe/resources/invoice/line/README.md#remove_many) - Bulk remove invoice line items
* [update](sideko_stripe/resources/invoice/line/README.md#update) - Update an invoice's line item
* [update_many](sideko_stripe/resources/invoice/line/README.md#update_many) - Bulk update invoice line items

### [invoice_item](sideko_stripe/resources/invoice_item/README.md)

* [create](sideko_stripe/resources/invoice_item/README.md#create) - Create an invoice item
* [delete](sideko_stripe/resources/invoice_item/README.md#delete) - Delete an invoice item
* [get](sideko_stripe/resources/invoice_item/README.md#get) - Retrieve an invoice item
* [list](sideko_stripe/resources/invoice_item/README.md#list) - List all invoice items
* [update](sideko_stripe/resources/invoice_item/README.md#update) - Update an invoice item

### [invoice_payment](sideko_stripe/resources/invoice_payment/README.md)

* [get](sideko_stripe/resources/invoice_payment/README.md#get) - Retrieve an InvoicePayment
* [list](sideko_stripe/resources/invoice_payment/README.md#list) - List all payments for an invoice

### [invoice_rendering_template](sideko_stripe/resources/invoice_rendering_template/README.md)

* [archive](sideko_stripe/resources/invoice_rendering_template/README.md#archive) - Archive an invoice rendering template
* [get](sideko_stripe/resources/invoice_rendering_template/README.md#get) - Retrieve an invoice rendering template
* [list](sideko_stripe/resources/invoice_rendering_template/README.md#list) - List all invoice rendering templates
* [unarchive](sideko_stripe/resources/invoice_rendering_template/README.md#unarchive) - Unarchive an invoice rendering template

### [issuing.authorization](sideko_stripe/resources/issuing/authorization/README.md)

* [approve](sideko_stripe/resources/issuing/authorization/README.md#approve) - Approve an authorization
* [decline](sideko_stripe/resources/issuing/authorization/README.md#decline) - Decline an authorization
* [get](sideko_stripe/resources/issuing/authorization/README.md#get) - Retrieve an authorization
* [list](sideko_stripe/resources/issuing/authorization/README.md#list) - List all authorizations
* [update](sideko_stripe/resources/issuing/authorization/README.md#update) - Update an authorization

### [issuing.card](sideko_stripe/resources/issuing/card/README.md)

* [create](sideko_stripe/resources/issuing/card/README.md#create) - Create a card
* [get](sideko_stripe/resources/issuing/card/README.md#get) - Retrieve a card
* [list](sideko_stripe/resources/issuing/card/README.md#list) - List all cards
* [update](sideko_stripe/resources/issuing/card/README.md#update) - Update a card

### [issuing.cardholder](sideko_stripe/resources/issuing/cardholder/README.md)

* [create](sideko_stripe/resources/issuing/cardholder/README.md#create) - Create a cardholder
* [get](sideko_stripe/resources/issuing/cardholder/README.md#get) - Retrieve a cardholder
* [list](sideko_stripe/resources/issuing/cardholder/README.md#list) - List all cardholders
* [update](sideko_stripe/resources/issuing/cardholder/README.md#update) - Update a cardholder

### [issuing.dispute](sideko_stripe/resources/issuing/dispute/README.md)

* [create](sideko_stripe/resources/issuing/dispute/README.md#create) - Create a dispute
* [get](sideko_stripe/resources/issuing/dispute/README.md#get) - Retrieve a dispute
* [list](sideko_stripe/resources/issuing/dispute/README.md#list) - List all disputes
* [submit](sideko_stripe/resources/issuing/dispute/README.md#submit) - Submit a dispute
* [update](sideko_stripe/resources/issuing/dispute/README.md#update) - Update a dispute

### [issuing.personalization_design](sideko_stripe/resources/issuing/personalization_design/README.md)

* [create](sideko_stripe/resources/issuing/personalization_design/README.md#create) - Create a personalization design
* [get](sideko_stripe/resources/issuing/personalization_design/README.md#get) - Retrieve a personalization design
* [list](sideko_stripe/resources/issuing/personalization_design/README.md#list) - List all personalization designs
* [update](sideko_stripe/resources/issuing/personalization_design/README.md#update) - Update a personalization design

### [issuing.physical_bundle](sideko_stripe/resources/issuing/physical_bundle/README.md)

* [get](sideko_stripe/resources/issuing/physical_bundle/README.md#get) - Retrieve a physical bundle
* [list](sideko_stripe/resources/issuing/physical_bundle/README.md#list) - List all physical bundles

### [issuing.settlement](sideko_stripe/resources/issuing/settlement/README.md)

* [get](sideko_stripe/resources/issuing/settlement/README.md#get) - Retrieve a settlement
* [update](sideko_stripe/resources/issuing/settlement/README.md#update) - Update a settlement

### [issuing.token](sideko_stripe/resources/issuing/token/README.md)

* [get](sideko_stripe/resources/issuing/token/README.md#get) - Retrieve an issuing token
* [list](sideko_stripe/resources/issuing/token/README.md#list) - List all issuing tokens for card
* [update](sideko_stripe/resources/issuing/token/README.md#update) - Update a token status

### [issuing.transaction](sideko_stripe/resources/issuing/transaction/README.md)

* [get](sideko_stripe/resources/issuing/transaction/README.md#get) - Retrieve a transaction
* [list](sideko_stripe/resources/issuing/transaction/README.md#list) - List all transactions
* [update](sideko_stripe/resources/issuing/transaction/README.md#update) - Update a transaction

### [link_account_session](sideko_stripe/resources/link_account_session/README.md)

* [create](sideko_stripe/resources/link_account_session/README.md#create) - Create a Session
* [get](sideko_stripe/resources/link_account_session/README.md#get) - Retrieve a Session

### [linked_account](sideko_stripe/resources/linked_account/README.md)

* [disconnect](sideko_stripe/resources/linked_account/README.md#disconnect) - Disconnect an Account
* [get](sideko_stripe/resources/linked_account/README.md#get) - Retrieve an Account
* [list](sideko_stripe/resources/linked_account/README.md#list) - List Accounts
* [refresh](sideko_stripe/resources/linked_account/README.md#refresh) - Refresh Account data

### [linked_account.owners](sideko_stripe/resources/linked_account/owners/README.md)

* [list](sideko_stripe/resources/linked_account/owners/README.md#list) - List Account Owners

### [mandates](sideko_stripe/resources/mandates/README.md)

* [get](sideko_stripe/resources/mandates/README.md#get) - Retrieve a Mandate

### [payment_intent](sideko_stripe/resources/payment_intent/README.md)

* [apply_customer_balance](sideko_stripe/resources/payment_intent/README.md#apply_customer_balance) - Reconcile a customer_balance PaymentIntent
* [cancel](sideko_stripe/resources/payment_intent/README.md#cancel) - Cancel a PaymentIntent
* [capture](sideko_stripe/resources/payment_intent/README.md#capture) - Capture a PaymentIntent
* [confirm](sideko_stripe/resources/payment_intent/README.md#confirm) - Confirm a PaymentIntent
* [create](sideko_stripe/resources/payment_intent/README.md#create) - Create a PaymentIntent
* [get](sideko_stripe/resources/payment_intent/README.md#get) - Retrieve a PaymentIntent
* [increment_authorization](sideko_stripe/resources/payment_intent/README.md#increment_authorization) - Increment an authorization
* [list](sideko_stripe/resources/payment_intent/README.md#list) - List all PaymentIntents
* [search](sideko_stripe/resources/payment_intent/README.md#search) - Search PaymentIntents
* [update](sideko_stripe/resources/payment_intent/README.md#update) - Update a PaymentIntent
* [verify_microdeposits](sideko_stripe/resources/payment_intent/README.md#verify_microdeposits) - Verify microdeposits on a PaymentIntent

### [payment_link](sideko_stripe/resources/payment_link/README.md)

* [create](sideko_stripe/resources/payment_link/README.md#create) - Create a payment link
* [get](sideko_stripe/resources/payment_link/README.md#get) - Retrieve payment link
* [list](sideko_stripe/resources/payment_link/README.md#list) - List all payment links
* [update](sideko_stripe/resources/payment_link/README.md#update) - Update a payment link

### [payment_links.line_item](sideko_stripe/resources/payment_links/line_item/README.md)

* [list](sideko_stripe/resources/payment_links/line_item/README.md#list) - Retrieve a payment link's line items

### [payment_method](sideko_stripe/resources/payment_method/README.md)

* [attach](sideko_stripe/resources/payment_method/README.md#attach) - Attach a PaymentMethod to a Customer
* [create](sideko_stripe/resources/payment_method/README.md#create) - Shares a PaymentMethod
* [detach](sideko_stripe/resources/payment_method/README.md#detach) - Detach a PaymentMethod from a Customer
* [get](sideko_stripe/resources/payment_method/README.md#get) - Retrieve a PaymentMethod
* [list](sideko_stripe/resources/payment_method/README.md#list) - List PaymentMethods
* [update](sideko_stripe/resources/payment_method/README.md#update) - Update a PaymentMethod

### [payment_method_configuration](sideko_stripe/resources/payment_method_configuration/README.md)

* [create](sideko_stripe/resources/payment_method_configuration/README.md#create) - Create a payment method configuration
* [get](sideko_stripe/resources/payment_method_configuration/README.md#get) - Retrieve payment method configuration
* [list](sideko_stripe/resources/payment_method_configuration/README.md#list) - List payment method configurations
* [update](sideko_stripe/resources/payment_method_configuration/README.md#update) - Update payment method configuration

### [payment_method_domain](sideko_stripe/resources/payment_method_domain/README.md)

* [create](sideko_stripe/resources/payment_method_domain/README.md#create) - Create a payment method domain
* [get](sideko_stripe/resources/payment_method_domain/README.md#get) - Retrieve a payment method domain
* [list](sideko_stripe/resources/payment_method_domain/README.md#list) - List payment method domains
* [update](sideko_stripe/resources/payment_method_domain/README.md#update) - Update a payment method domain
* [validate](sideko_stripe/resources/payment_method_domain/README.md#validate) - Validate an existing payment method domain

### [payout](sideko_stripe/resources/payout/README.md)

* [cancel](sideko_stripe/resources/payout/README.md#cancel) - Cancel a payout
* [create](sideko_stripe/resources/payout/README.md#create) - Create a payout
* [get](sideko_stripe/resources/payout/README.md#get) - Retrieve a payout
* [list](sideko_stripe/resources/payout/README.md#list) - List all payouts
* [reverse](sideko_stripe/resources/payout/README.md#reverse) - Reverse a payout
* [update](sideko_stripe/resources/payout/README.md#update) - Update a payout

### [plan](sideko_stripe/resources/plan/README.md)

* [create](sideko_stripe/resources/plan/README.md#create) - Create a plan
* [delete](sideko_stripe/resources/plan/README.md#delete) - Delete a plan
* [get](sideko_stripe/resources/plan/README.md#get) - Retrieve a plan
* [list](sideko_stripe/resources/plan/README.md#list) - List all plans
* [update](sideko_stripe/resources/plan/README.md#update) - Update a plan

### [price](sideko_stripe/resources/price/README.md)

* [create](sideko_stripe/resources/price/README.md#create) - Create a price
* [get](sideko_stripe/resources/price/README.md#get) - Retrieve a price
* [list](sideko_stripe/resources/price/README.md#list) - List all prices
* [search](sideko_stripe/resources/price/README.md#search) - Search prices
* [update](sideko_stripe/resources/price/README.md#update) - Update a price

### [product](sideko_stripe/resources/product/README.md)

* [create](sideko_stripe/resources/product/README.md#create) - Create a product
* [delete](sideko_stripe/resources/product/README.md#delete) - Delete a product
* [get](sideko_stripe/resources/product/README.md#get) - Retrieve a product
* [list](sideko_stripe/resources/product/README.md#list) - List all products
* [search](sideko_stripe/resources/product/README.md#search) - Search products
* [update](sideko_stripe/resources/product/README.md#update) - Update a product

### [product.feature](sideko_stripe/resources/product/feature/README.md)

* [create](sideko_stripe/resources/product/feature/README.md#create) - Attach a feature to a product
* [delete](sideko_stripe/resources/product/feature/README.md#delete) - Remove a feature from a product
* [get](sideko_stripe/resources/product/feature/README.md#get) - Retrieve a product_feature
* [list](sideko_stripe/resources/product/feature/README.md#list) - List all features attached to a product

### [promotion_code](sideko_stripe/resources/promotion_code/README.md)

* [create](sideko_stripe/resources/promotion_code/README.md#create) - Create a promotion code
* [get](sideko_stripe/resources/promotion_code/README.md#get) - Retrieve a promotion code
* [list](sideko_stripe/resources/promotion_code/README.md#list) - List all promotion codes
* [update](sideko_stripe/resources/promotion_code/README.md#update) - Update a promotion code

### [quote](sideko_stripe/resources/quote/README.md)

* [accept](sideko_stripe/resources/quote/README.md#accept) - Accept a quote
* [cancel](sideko_stripe/resources/quote/README.md#cancel) - Cancel a quote
* [computed_upfront_line_items](sideko_stripe/resources/quote/README.md#computed_upfront_line_items) - Retrieve a quote's upfront line items
* [create](sideko_stripe/resources/quote/README.md#create) - Create a quote
* [finalize](sideko_stripe/resources/quote/README.md#finalize) - Finalize a quote
* [get](sideko_stripe/resources/quote/README.md#get) - Retrieve a quote
* [list](sideko_stripe/resources/quote/README.md#list) - List all quotes
* [pdf](sideko_stripe/resources/quote/README.md#pdf) - Download quote PDF
* [update](sideko_stripe/resources/quote/README.md#update) - Update a quote

### [quotes.line_item](sideko_stripe/resources/quotes/line_item/README.md)

* [list](sideko_stripe/resources/quotes/line_item/README.md#list) - Retrieve a quote's line items

### [radar.early_fraud_warning](sideko_stripe/resources/radar/early_fraud_warning/README.md)

* [get](sideko_stripe/resources/radar/early_fraud_warning/README.md#get) - Retrieve an early fraud warning
* [list](sideko_stripe/resources/radar/early_fraud_warning/README.md#list) - List all early fraud warnings

### [radar.value_list](sideko_stripe/resources/radar/value_list/README.md)

* [create](sideko_stripe/resources/radar/value_list/README.md#create) - Create a value list
* [delete](sideko_stripe/resources/radar/value_list/README.md#delete) - Delete a value list
* [get](sideko_stripe/resources/radar/value_list/README.md#get) - Retrieve a value list
* [list](sideko_stripe/resources/radar/value_list/README.md#list) - List all value lists
* [update](sideko_stripe/resources/radar/value_list/README.md#update) - Update a value list

### [radar.value_list_item](sideko_stripe/resources/radar/value_list_item/README.md)

* [create](sideko_stripe/resources/radar/value_list_item/README.md#create) - Create a value list item
* [delete](sideko_stripe/resources/radar/value_list_item/README.md#delete) - Delete a value list item
* [get](sideko_stripe/resources/radar/value_list_item/README.md#get) - Retrieve a value list item
* [list](sideko_stripe/resources/radar/value_list_item/README.md#list) - List all value list items

### [refund](sideko_stripe/resources/refund/README.md)

* [cancel](sideko_stripe/resources/refund/README.md#cancel) - Cancel a refund
* [create](sideko_stripe/resources/refund/README.md#create) - Create customer balance refund
* [get](sideko_stripe/resources/refund/README.md#get) - Retrieve a refund
* [list](sideko_stripe/resources/refund/README.md#list) - List all refunds
* [update](sideko_stripe/resources/refund/README.md#update) - Update a refund

### [reporting.report_run](sideko_stripe/resources/reporting/report_run/README.md)

* [create](sideko_stripe/resources/reporting/report_run/README.md#create) - Create a Report Run
* [get](sideko_stripe/resources/reporting/report_run/README.md#get) - Retrieve a Report Run
* [list](sideko_stripe/resources/reporting/report_run/README.md#list) - List all Report Runs

### [reporting.report_type](sideko_stripe/resources/reporting/report_type/README.md)

* [get](sideko_stripe/resources/reporting/report_type/README.md#get) - Retrieve a Report Type
* [list](sideko_stripe/resources/reporting/report_type/README.md#list) - List all Report Types

### [review](sideko_stripe/resources/review/README.md)

* [approve](sideko_stripe/resources/review/README.md#approve) - Approve a review
* [get](sideko_stripe/resources/review/README.md#get) - Retrieve a review
* [list](sideko_stripe/resources/review/README.md#list) - List all open reviews

### [setup_attempt](sideko_stripe/resources/setup_attempt/README.md)

* [list](sideko_stripe/resources/setup_attempt/README.md#list) - List all SetupAttempts

### [setup_intent](sideko_stripe/resources/setup_intent/README.md)

* [cancel](sideko_stripe/resources/setup_intent/README.md#cancel) - Cancel a SetupIntent
* [confirm](sideko_stripe/resources/setup_intent/README.md#confirm) - Confirm a SetupIntent
* [create](sideko_stripe/resources/setup_intent/README.md#create) - Create a SetupIntent
* [get](sideko_stripe/resources/setup_intent/README.md#get) - Retrieve a SetupIntent
* [list](sideko_stripe/resources/setup_intent/README.md#list) - List all SetupIntents
* [update](sideko_stripe/resources/setup_intent/README.md#update) - Update a SetupIntent
* [verify_microdeposits](sideko_stripe/resources/setup_intent/README.md#verify_microdeposits) - Verify microdeposits on a SetupIntent

### [shipping_rate](sideko_stripe/resources/shipping_rate/README.md)

* [create](sideko_stripe/resources/shipping_rate/README.md#create) - Create a shipping rate
* [get](sideko_stripe/resources/shipping_rate/README.md#get) - Retrieve a shipping rate
* [list](sideko_stripe/resources/shipping_rate/README.md#list) - List all shipping rates
* [update](sideko_stripe/resources/shipping_rate/README.md#update) - Update a shipping rate

### [sigma.scheduled_query_run](sideko_stripe/resources/sigma/scheduled_query_run/README.md)

* [get](sideko_stripe/resources/sigma/scheduled_query_run/README.md#get) - Retrieve a scheduled query run
* [list](sideko_stripe/resources/sigma/scheduled_query_run/README.md#list) - List all scheduled query runs

### [source](sideko_stripe/resources/source/README.md)

* [create](sideko_stripe/resources/source/README.md#create) - Shares a source
* [get](sideko_stripe/resources/source/README.md#get) - Retrieve a source
* [update](sideko_stripe/resources/source/README.md#update) - Update a source
* [verify](sideko_stripe/resources/source/README.md#verify) - POST /v1/sources/{source}/verify

### [source.mandate_notifications](sideko_stripe/resources/source/mandate_notifications/README.md)

* [get](sideko_stripe/resources/source/mandate_notifications/README.md#get) - Retrieve a Source MandateNotification

### [source.source_transactions](sideko_stripe/resources/source/source_transactions/README.md)

* [get](sideko_stripe/resources/source/source_transactions/README.md#get) - Retrieve a source transaction
* [list](sideko_stripe/resources/source/source_transactions/README.md#list) - GET /v1/sources/{source}/source_transactions

### [subscription](sideko_stripe/resources/subscription/README.md)

* [create](sideko_stripe/resources/subscription/README.md#create) - Create a subscription
* [delete](sideko_stripe/resources/subscription/README.md#delete) - Cancel a subscription
* [get](sideko_stripe/resources/subscription/README.md#get) - Retrieve a subscription
* [list](sideko_stripe/resources/subscription/README.md#list) - List subscriptions
* [resume](sideko_stripe/resources/subscription/README.md#resume) - Resume a subscription
* [search](sideko_stripe/resources/subscription/README.md#search) - Search subscriptions
* [update](sideko_stripe/resources/subscription/README.md#update) - Update a subscription

### [subscription_item](sideko_stripe/resources/subscription_item/README.md)

* [create](sideko_stripe/resources/subscription_item/README.md#create) - Create a subscription item
* [delete](sideko_stripe/resources/subscription_item/README.md#delete) - Delete a subscription item
* [get](sideko_stripe/resources/subscription_item/README.md#get) - Retrieve a subscription item
* [list](sideko_stripe/resources/subscription_item/README.md#list) - List all subscription items
* [update](sideko_stripe/resources/subscription_item/README.md#update) - Update a subscription item

### [subscription_schedule](sideko_stripe/resources/subscription_schedule/README.md)

* [cancel](sideko_stripe/resources/subscription_schedule/README.md#cancel) - Cancel a schedule
* [create](sideko_stripe/resources/subscription_schedule/README.md#create) - Create a schedule
* [get](sideko_stripe/resources/subscription_schedule/README.md#get) - Retrieve a schedule
* [list](sideko_stripe/resources/subscription_schedule/README.md#list) - List all schedules
* [release](sideko_stripe/resources/subscription_schedule/README.md#release) - Release a schedule
* [update](sideko_stripe/resources/subscription_schedule/README.md#update) - Update a schedule

### [subscriptions.discount](sideko_stripe/resources/subscriptions/discount/README.md)

* [delete](sideko_stripe/resources/subscriptions/discount/README.md#delete) - Delete a subscription discount

### [tax.calculation](sideko_stripe/resources/tax/calculation/README.md)

* [create](sideko_stripe/resources/tax/calculation/README.md#create) - Create a Tax Calculation
* [get](sideko_stripe/resources/tax/calculation/README.md#get) - Retrieve a Tax Calculation

### [tax.calculations.line_item](sideko_stripe/resources/tax/calculations/line_item/README.md)

* [list](sideko_stripe/resources/tax/calculations/line_item/README.md#list) - Retrieve a calculation's line items

### [tax.registration](sideko_stripe/resources/tax/registration/README.md)

* [create](sideko_stripe/resources/tax/registration/README.md#create) - Create a registration
* [get](sideko_stripe/resources/tax/registration/README.md#get) - Retrieve a registration
* [list](sideko_stripe/resources/tax/registration/README.md#list) - List registrations
* [update](sideko_stripe/resources/tax/registration/README.md#update) - Update a registration

### [tax.setting](sideko_stripe/resources/tax/setting/README.md)

* [list](sideko_stripe/resources/tax/setting/README.md#list) - Retrieve settings
* [update](sideko_stripe/resources/tax/setting/README.md#update) - Update settings

### [tax.transaction](sideko_stripe/resources/tax/transaction/README.md)

* [create_from_calculation](sideko_stripe/resources/tax/transaction/README.md#create_from_calculation) - Create a transaction from a calculation
* [create_reversal](sideko_stripe/resources/tax/transaction/README.md#create_reversal) - Create a reversal transaction
* [get](sideko_stripe/resources/tax/transaction/README.md#get) - Retrieve a transaction

### [tax.transaction.line_items](sideko_stripe/resources/tax/transaction/line_items/README.md)

* [list](sideko_stripe/resources/tax/transaction/line_items/README.md#list) - Retrieve a transaction's line items

### [tax_code](sideko_stripe/resources/tax_code/README.md)

* [get](sideko_stripe/resources/tax_code/README.md#get) - Retrieve a tax code
* [list](sideko_stripe/resources/tax_code/README.md#list) - List all tax codes

### [tax_id](sideko_stripe/resources/tax_id/README.md)

* [create](sideko_stripe/resources/tax_id/README.md#create) - Create a tax ID
* [delete](sideko_stripe/resources/tax_id/README.md#delete) - Delete a tax ID
* [get](sideko_stripe/resources/tax_id/README.md#get) - Retrieve a tax ID
* [list](sideko_stripe/resources/tax_id/README.md#list) - List all tax IDs

### [tax_rate](sideko_stripe/resources/tax_rate/README.md)

* [create](sideko_stripe/resources/tax_rate/README.md#create) - Create a tax rate
* [get](sideko_stripe/resources/tax_rate/README.md#get) - Retrieve a tax rate
* [list](sideko_stripe/resources/tax_rate/README.md#list) - List all tax rates
* [update](sideko_stripe/resources/tax_rate/README.md#update) - Update a tax rate

### [terminal.configuration](sideko_stripe/resources/terminal/configuration/README.md)

* [create](sideko_stripe/resources/terminal/configuration/README.md#create) - Create a Configuration
* [delete](sideko_stripe/resources/terminal/configuration/README.md#delete) - Delete a Configuration
* [get](sideko_stripe/resources/terminal/configuration/README.md#get) - Retrieve a Configuration
* [list](sideko_stripe/resources/terminal/configuration/README.md#list) - List all Configurations
* [update](sideko_stripe/resources/terminal/configuration/README.md#update) - Update a Configuration

### [terminal.connection_token](sideko_stripe/resources/terminal/connection_token/README.md)

* [create](sideko_stripe/resources/terminal/connection_token/README.md#create) - Create a Connection Token

### [terminal.location](sideko_stripe/resources/terminal/location/README.md)

* [create](sideko_stripe/resources/terminal/location/README.md#create) - Create a Location
* [delete](sideko_stripe/resources/terminal/location/README.md#delete) - Delete a Location
* [get](sideko_stripe/resources/terminal/location/README.md#get) - Retrieve a Location
* [list](sideko_stripe/resources/terminal/location/README.md#list) - List all Locations
* [update](sideko_stripe/resources/terminal/location/README.md#update) - Update a Location

### [terminal.reader](sideko_stripe/resources/terminal/reader/README.md)

* [cancel_action](sideko_stripe/resources/terminal/reader/README.md#cancel_action) - Cancel the current reader action
* [create](sideko_stripe/resources/terminal/reader/README.md#create) - Create a Reader
* [delete](sideko_stripe/resources/terminal/reader/README.md#delete) - Delete a Reader
* [get](sideko_stripe/resources/terminal/reader/README.md#get) - Retrieve a Reader
* [list](sideko_stripe/resources/terminal/reader/README.md#list) - List all Readers
* [process_payment_intent](sideko_stripe/resources/terminal/reader/README.md#process_payment_intent) - Hand-off a PaymentIntent to a Reader
* [process_setup_intent](sideko_stripe/resources/terminal/reader/README.md#process_setup_intent) - Hand-off a SetupIntent to a Reader
* [refund_payment](sideko_stripe/resources/terminal/reader/README.md#refund_payment) - Refund a Charge or a PaymentIntent in-person
* [set_reader_display](sideko_stripe/resources/terminal/reader/README.md#set_reader_display) - Set reader display
* [update](sideko_stripe/resources/terminal/reader/README.md#update) - Update a Reader

### [test_helper.confirmation_token](sideko_stripe/resources/test_helper/confirmation_token/README.md)

* [create](sideko_stripe/resources/test_helper/confirmation_token/README.md#create) - Create a test Confirmation Token

### [test_helper.customer](sideko_stripe/resources/test_helper/customer/README.md)

* [fund_cash_balance](sideko_stripe/resources/test_helper/customer/README.md#fund_cash_balance) - Fund a test mode cash balance

### [test_helper.issuing.authorization](sideko_stripe/resources/test_helper/issuing/authorization/README.md)

* [capture](sideko_stripe/resources/test_helper/issuing/authorization/README.md#capture) - Capture a test-mode authorization
* [create](sideko_stripe/resources/test_helper/issuing/authorization/README.md#create) - Create a test-mode authorization
* [expire](sideko_stripe/resources/test_helper/issuing/authorization/README.md#expire) - Expire a test-mode authorization
* [finalize_amount](sideko_stripe/resources/test_helper/issuing/authorization/README.md#finalize_amount) - Finalize a test-mode authorization's amount
* [increment](sideko_stripe/resources/test_helper/issuing/authorization/README.md#increment) - Increment a test-mode authorization
* [reverse](sideko_stripe/resources/test_helper/issuing/authorization/README.md#reverse) - Reverse a test-mode authorization

### [test_helper.issuing.authorization.fraud_challenges](sideko_stripe/resources/test_helper/issuing/authorization/fraud_challenges/README.md)

* [respond](sideko_stripe/resources/test_helper/issuing/authorization/fraud_challenges/README.md#respond) - Respond to fraud challenge

### [test_helper.issuing.card.shipping](sideko_stripe/resources/test_helper/issuing/card/shipping/README.md)

* [deliver](sideko_stripe/resources/test_helper/issuing/card/shipping/README.md#deliver) - Deliver a testmode card
* [fail](sideko_stripe/resources/test_helper/issuing/card/shipping/README.md#fail) - Fail a testmode card
* [returned](sideko_stripe/resources/test_helper/issuing/card/shipping/README.md#returned) - Return a testmode card
* [ship](sideko_stripe/resources/test_helper/issuing/card/shipping/README.md#ship) - Ship a testmode card
* [submit](sideko_stripe/resources/test_helper/issuing/card/shipping/README.md#submit) - Submit a testmode card

### [test_helper.issuing.personalization_design](sideko_stripe/resources/test_helper/issuing/personalization_design/README.md)

* [activate](sideko_stripe/resources/test_helper/issuing/personalization_design/README.md#activate) - Activate a testmode personalization design
* [deactivate](sideko_stripe/resources/test_helper/issuing/personalization_design/README.md#deactivate) - Deactivate a testmode personalization design
* [reject](sideko_stripe/resources/test_helper/issuing/personalization_design/README.md#reject) - Reject a testmode personalization design

### [test_helper.issuing.settlement](sideko_stripe/resources/test_helper/issuing/settlement/README.md)

* [complete](sideko_stripe/resources/test_helper/issuing/settlement/README.md#complete) - Complete a test-mode settlement
* [create](sideko_stripe/resources/test_helper/issuing/settlement/README.md#create) - Create a test-mode settlement

### [test_helper.issuing.transaction](sideko_stripe/resources/test_helper/issuing/transaction/README.md)

* [create_force_capture](sideko_stripe/resources/test_helper/issuing/transaction/README.md#create_force_capture) - Create a test-mode force capture
* [create_unlinked_refund](sideko_stripe/resources/test_helper/issuing/transaction/README.md#create_unlinked_refund) - Create a test-mode unlinked refund
* [refund](sideko_stripe/resources/test_helper/issuing/transaction/README.md#refund) - Refund a test-mode transaction

### [test_helper.refund](sideko_stripe/resources/test_helper/refund/README.md)

* [expire](sideko_stripe/resources/test_helper/refund/README.md#expire) - Expire a pending refund.

### [test_helper.terminal.reader](sideko_stripe/resources/test_helper/terminal/reader/README.md)

* [present_payment_method](sideko_stripe/resources/test_helper/terminal/reader/README.md#present_payment_method) - Simulate presenting a payment method

### [test_helper.test_clock](sideko_stripe/resources/test_helper/test_clock/README.md)

* [advance](sideko_stripe/resources/test_helper/test_clock/README.md#advance) - Advance a test clock
* [create](sideko_stripe/resources/test_helper/test_clock/README.md#create) - Create a test clock
* [delete](sideko_stripe/resources/test_helper/test_clock/README.md#delete) - Delete a test clock
* [get](sideko_stripe/resources/test_helper/test_clock/README.md#get) - Retrieve a test clock
* [list](sideko_stripe/resources/test_helper/test_clock/README.md#list) - List all test clocks

### [test_helper.treasury.inbound_transfers](sideko_stripe/resources/test_helper/treasury/inbound_transfers/README.md)

* [fail](sideko_stripe/resources/test_helper/treasury/inbound_transfers/README.md#fail) - Test mode: Fail an InboundTransfer
* [returned](sideko_stripe/resources/test_helper/treasury/inbound_transfers/README.md#returned) - Test mode: Return an InboundTransfer
* [succeed](sideko_stripe/resources/test_helper/treasury/inbound_transfers/README.md#succeed) - Test mode: Succeed an InboundTransfer

### [test_helper.treasury.outbound_payment](sideko_stripe/resources/test_helper/treasury/outbound_payment/README.md)

* [fail](sideko_stripe/resources/test_helper/treasury/outbound_payment/README.md#fail) - Test mode: Fail an OutboundPayment
* [post](sideko_stripe/resources/test_helper/treasury/outbound_payment/README.md#post) - Test mode: Post an OutboundPayment
* [returned](sideko_stripe/resources/test_helper/treasury/outbound_payment/README.md#returned) - Test mode: Return an OutboundPayment
* [update](sideko_stripe/resources/test_helper/treasury/outbound_payment/README.md#update) - Test mode: Update an OutboundPayment

### [test_helper.treasury.outbound_transfer](sideko_stripe/resources/test_helper/treasury/outbound_transfer/README.md)

* [fail](sideko_stripe/resources/test_helper/treasury/outbound_transfer/README.md#fail) - Test mode: Fail an OutboundTransfer
* [post](sideko_stripe/resources/test_helper/treasury/outbound_transfer/README.md#post) - Test mode: Post an OutboundTransfer
* [returned](sideko_stripe/resources/test_helper/treasury/outbound_transfer/README.md#returned) - Test mode: Return an OutboundTransfer
* [update](sideko_stripe/resources/test_helper/treasury/outbound_transfer/README.md#update) - Test mode: Update an OutboundTransfer

### [test_helper.treasury.received_credit](sideko_stripe/resources/test_helper/treasury/received_credit/README.md)

* [create](sideko_stripe/resources/test_helper/treasury/received_credit/README.md#create) - Test mode: Create a ReceivedCredit

### [test_helper.treasury.received_debit](sideko_stripe/resources/test_helper/treasury/received_debit/README.md)

* [create](sideko_stripe/resources/test_helper/treasury/received_debit/README.md#create) - Test mode: Create a ReceivedDebit

### [token](sideko_stripe/resources/token/README.md)

* [create](sideko_stripe/resources/token/README.md#create) - Create a CVC update token
* [get](sideko_stripe/resources/token/README.md#get) - Retrieve a token

### [topups](sideko_stripe/resources/topups/README.md)

* [cancel](sideko_stripe/resources/topups/README.md#cancel) - Cancel a top-up
* [create](sideko_stripe/resources/topups/README.md#create) - Create a top-up
* [get](sideko_stripe/resources/topups/README.md#get) - Retrieve a top-up
* [list](sideko_stripe/resources/topups/README.md#list) - List all top-ups
* [update](sideko_stripe/resources/topups/README.md#update) - Update a top-up

### [transfer](sideko_stripe/resources/transfer/README.md)

* [create](sideko_stripe/resources/transfer/README.md#create) - Create a transfer
* [get](sideko_stripe/resources/transfer/README.md#get) - Retrieve a transfer
* [list](sideko_stripe/resources/transfer/README.md#list) - List all transfers
* [update](sideko_stripe/resources/transfer/README.md#update) - Update a transfer

### [transfers.reversal](sideko_stripe/resources/transfers/reversal/README.md)

* [create](sideko_stripe/resources/transfers/reversal/README.md#create) - Create a transfer reversal
* [get](sideko_stripe/resources/transfers/reversal/README.md#get) - Retrieve a reversal
* [list](sideko_stripe/resources/transfers/reversal/README.md#list) - List all reversals
* [update](sideko_stripe/resources/transfers/reversal/README.md#update) - Update a reversal

### [treasury.credit_reversal](sideko_stripe/resources/treasury/credit_reversal/README.md)

* [create](sideko_stripe/resources/treasury/credit_reversal/README.md#create) - Create a CreditReversal
* [get](sideko_stripe/resources/treasury/credit_reversal/README.md#get) - Retrieve a CreditReversal
* [list](sideko_stripe/resources/treasury/credit_reversal/README.md#list) - List all CreditReversals

### [treasury.debit_reversal](sideko_stripe/resources/treasury/debit_reversal/README.md)

* [create](sideko_stripe/resources/treasury/debit_reversal/README.md#create) - Create a DebitReversal
* [get](sideko_stripe/resources/treasury/debit_reversal/README.md#get) - Retrieve a DebitReversal
* [list](sideko_stripe/resources/treasury/debit_reversal/README.md#list) - List all DebitReversals

### [treasury.financial_account](sideko_stripe/resources/treasury/financial_account/README.md)

* [close](sideko_stripe/resources/treasury/financial_account/README.md#close) - Close a FinancialAccount
* [create](sideko_stripe/resources/treasury/financial_account/README.md#create) - Create a FinancialAccount
* [get](sideko_stripe/resources/treasury/financial_account/README.md#get) - Retrieve a FinancialAccount
* [list](sideko_stripe/resources/treasury/financial_account/README.md#list) - List all FinancialAccounts
* [update](sideko_stripe/resources/treasury/financial_account/README.md#update) - Update a FinancialAccount

### [treasury.financial_accounts.feature](sideko_stripe/resources/treasury/financial_accounts/feature/README.md)

* [create](sideko_stripe/resources/treasury/financial_accounts/feature/README.md#create) - Update FinancialAccount Features
* [list](sideko_stripe/resources/treasury/financial_accounts/feature/README.md#list) - Retrieve FinancialAccount Features

### [treasury.inbound_transfer](sideko_stripe/resources/treasury/inbound_transfer/README.md)

* [cance](sideko_stripe/resources/treasury/inbound_transfer/README.md#cance) - Cancel an InboundTransfer
* [create](sideko_stripe/resources/treasury/inbound_transfer/README.md#create) - Create an InboundTransfer
* [get](sideko_stripe/resources/treasury/inbound_transfer/README.md#get) - Retrieve an InboundTransfer
* [list](sideko_stripe/resources/treasury/inbound_transfer/README.md#list) - List all InboundTransfers

### [treasury.outbound_payment](sideko_stripe/resources/treasury/outbound_payment/README.md)

* [cancel](sideko_stripe/resources/treasury/outbound_payment/README.md#cancel) - Cancel an OutboundPayment
* [create](sideko_stripe/resources/treasury/outbound_payment/README.md#create) - Create an OutboundPayment
* [get](sideko_stripe/resources/treasury/outbound_payment/README.md#get) - Retrieve an OutboundPayment
* [list](sideko_stripe/resources/treasury/outbound_payment/README.md#list) - List all OutboundPayments

### [treasury.outbound_transfer](sideko_stripe/resources/treasury/outbound_transfer/README.md)

* [cancel](sideko_stripe/resources/treasury/outbound_transfer/README.md#cancel) - Cancel an OutboundTransfer
* [create](sideko_stripe/resources/treasury/outbound_transfer/README.md#create) - Create an OutboundTransfer
* [get](sideko_stripe/resources/treasury/outbound_transfer/README.md#get) - Retrieve an OutboundTransfer
* [list](sideko_stripe/resources/treasury/outbound_transfer/README.md#list) - List all OutboundTransfers

### [treasury.received_credit](sideko_stripe/resources/treasury/received_credit/README.md)

* [get](sideko_stripe/resources/treasury/received_credit/README.md#get) - Retrieve a ReceivedCredit
* [list](sideko_stripe/resources/treasury/received_credit/README.md#list) - List all ReceivedCredits

### [treasury.received_debit](sideko_stripe/resources/treasury/received_debit/README.md)

* [get](sideko_stripe/resources/treasury/received_debit/README.md#get) - Retrieve a ReceivedDebit
* [list](sideko_stripe/resources/treasury/received_debit/README.md#list) - List all ReceivedDebits

### [treasury.transaction](sideko_stripe/resources/treasury/transaction/README.md)

* [get](sideko_stripe/resources/treasury/transaction/README.md#get) - Retrieve a Transaction
* [list](sideko_stripe/resources/treasury/transaction/README.md#list) - List all Transactions

### [treasury.transaction_entry](sideko_stripe/resources/treasury/transaction_entry/README.md)

* [get](sideko_stripe/resources/treasury/transaction_entry/README.md#get) - Retrieve a TransactionEntry
* [list](sideko_stripe/resources/treasury/transaction_entry/README.md#list) - List all TransactionEntries

### [v1.climate.suppliers](sideko_stripe/resources/v1/climate/suppliers/README.md)

* [list](sideko_stripe/resources/v1/climate/suppliers/README.md#list) - List suppliers

### [webhook_endpoints](sideko_stripe/resources/webhook_endpoints/README.md)

* [create](sideko_stripe/resources/webhook_endpoints/README.md#create) - Create a webhook endpoint
* [delete](sideko_stripe/resources/webhook_endpoints/README.md#delete) - Delete a webhook endpoint
* [get](sideko_stripe/resources/webhook_endpoints/README.md#get) - Retrieve a webhook endpoint
* [list](sideko_stripe/resources/webhook_endpoints/README.md#list) - List all webhook endpoints
* [update](sideko_stripe/resources/webhook_endpoints/README.md#update) - Update a webhook endpoint

<!-- MODULE DOCS END -->
