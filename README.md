### Introduction

Welcome to Escrow, a secure transaction service designed to protect online transactions between buyers and sellers. This document provides an overview of the Escrow platform and technical guidelines for third-party integrations.

### What is Escrow?

Escrow is a trusted intermediary service that helps ensure both parties in a transaction fulfill their obligations securely. The service temporarily holds funds until the agreed terms of the transaction have been completed.

### How does Escrow work?
1. Secure Transaction: Escrow provides a secure environment for online transactions between parties.
2. Funds Holding: When the buyer submits payment, the funds are securely held by Escrow until the transaction requirements are fulfilled.
3. Goods or Service Confirmation: The buyer confirms receipt of the goods or successful delivery of the service.
4. Payment Release: Once confirmation is completed, Escrow releases the funds to the seller or service provider, finalizing the transaction.
### Workflows
We provide two primary workflows, each with multiple configurable settings.

### Purchase Workflow
A Purchase workflow represents a standard sale transaction in which a seller offers an item for sale and the buyer pays the agreed amount upfront. After the seller ships the item and the buyer confirms receipt, the buyer may release the funds to the seller.

This workflow is ideal for:

* Physical product sales
* Marketplace transactions
* E-commerce purchases

### Earnest Workflow
An Earnest workflow represents a deposit-based agreement where no physical item is exchanged. This workflow is commonly used for services, rentals, reservations, or advance deposits.

After the payer receives the agreed-upon service or fulfillment, the payer may release the funds to the payee.

This workflow is ideal for:

* Rental deposits
* Service agreements
* Booking reservations
* Advance payments

## Settings
Each application can configure multiple settings depending on its business requirements.

### Relationship Type
##### C2C (Consumer-to-Consumer)

In this model, both parties in the transaction are individual users. This setup is suitable for platforms that connect users directly to each other.

Example use cases:

* Marketplaces
* Peer-to-peer trading platforms
* Classified listing services
##### B2C (Business-to-Consumer)
In this model, the payee represents a business or merchant, while the payer is an individual user. This setup is suitable for platforms that integrate shops, merchants, or commercial providers.

Example use cases:

* Online stores
* Merchant platforms
* Service providers

#### Initiation Setting

This setting enables payer to modify the initial deal details, such as:

* Price
* Description

before proceeding with payment.

If disabled, the payer must follow the original deal terms defined by the payee, such as purchasing an item with a fixed price from a shop.

#### Verification Setting

This setting enables the payee or service provider to receive a callback after payment and perform additional verification before the transaction proceeds.

This is commonly used for:

* Warehouse management
* Inventory verification
* Order approval systems

#### Controlled by Provider Setting

This setting allows the service provider to manage transaction actions such as accepting and shipping the deal on behalf of the payee.

This is useful when the provider wants to manage the entire transaction flow internally without redirecting users to Escrow service interfaces.