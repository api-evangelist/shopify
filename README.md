# Shopify

Shopify is a complete commerce platform that lets merchants start, grow, and manage a business. The Shopify APIs let developers build apps and integrations that extend Shopify functionality — from managing products and orders to building custom storefronts and embedded admin experiences.

**URL:** [https://shopify.dev/docs/api](https://shopify.dev/docs/api)

## Scope

- **Type:** Contract
- **Position:** Consuming
- **Access:** 3rd-Party

## Tags

- Commerce, Ecommerce, Payments, Retail, Shopping Cart

## Timestamps

- **Created:** 2024-04-14
- **Modified:** 2026-05-02

## APIs

### Shopify Admin REST API

The Shopify Admin REST API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillments, and webhooks for managing all aspects of a Shopify store.

**Human URL:** [https://shopify.dev/docs/api/admin-rest](https://shopify.dev/docs/api/admin-rest)

**Base URL:** `https://{store}.myshopify.com/admin/api/2025-01`

**Authentication:** API Key — `X-Shopify-Access-Token` header

**Tags:** Admin, Commerce, Ecommerce, REST, Retail

#### Properties

| Type | URL |
|------|-----|
| OpenAPI | [openapi/shopify-api-openapi.yml](openapi/shopify-api-openapi.yml) |
| OpenAPI | [openapi/shopify-admin-rest-api-openapi.yml](openapi/shopify-admin-rest-api-openapi.yml) |
| JSONSchema | [json-schema/shopify-product-schema.json](json-schema/shopify-product-schema.json) |
| JSONSchema | [json-schema/shopify-customer-schema.json](json-schema/shopify-customer-schema.json) |
| JSONSchema | [json-schema/shopify-order-schema.json](json-schema/shopify-order-schema.json) |
| JSONSchema | [json-schema/shopify-collection-schema.json](json-schema/shopify-collection-schema.json) |
| JSONSchema | [json-schema/shopify-inventory-item-schema.json](json-schema/shopify-inventory-item-schema.json) |
| JSONSchema | [json-schema/shopify-fulfillment-schema.json](json-schema/shopify-fulfillment-schema.json) |
| JSONStructure | [json-structure/shopify-product-structure.json](json-structure/shopify-product-structure.json) |
| JSONStructure | [json-structure/shopify-order-structure.json](json-structure/shopify-order-structure.json) |
| JSONLD | [json-ld/shopify-context.jsonld](json-ld/shopify-context.jsonld) |
| Example | [examples/shopify-create-product-example.json](examples/shopify-create-product-example.json) |
| Example | [examples/shopify-list-orders-example.json](examples/shopify-list-orders-example.json) |
| Vocabulary | [vocabulary/shopify-vocabulary.yml](vocabulary/shopify-vocabulary.yml) |
| SpectralRules | [rules/shopify-rules.yml](rules/shopify-rules.yml) |
| NaftikoCapability | [capabilities/shared/admin-rest.yaml](capabilities/shared/admin-rest.yaml) |
| NaftikoCapability | [capabilities/commerce-management.yaml](capabilities/commerce-management.yaml) |
| Documentation | [https://shopify.dev/docs/api/admin-rest](https://shopify.dev/docs/api/admin-rest) |

### Shopify GraphQL Admin API

The GraphQL Admin API lets you build apps and integrations that extend and enhance the Shopify admin. GraphQL is the recommended API for all new Shopify app development.

**Human URL:** [https://shopify.dev/docs/api/admin-graphql](https://shopify.dev/docs/api/admin-graphql)

**Tags:** Admin, Commerce, GraphQL

### Shopify Storefront API

A GraphQL API that provides commerce primitives to build custom, scalable shopping experiences on any platform including web, apps, and games.

**Human URL:** [https://shopify.dev/docs/api/storefront](https://shopify.dev/docs/api/storefront)

**Tags:** Commerce, GraphQL, Headless, Storefronts

### Shopify Customer Account API

Offers a secure way to access private customer-scoped data for building personalized, authenticated experiences in custom storefronts.

**Human URL:** [https://shopify.dev/docs/api/customer](https://shopify.dev/docs/api/customer)

**Tags:** Accounts, Commerce, Customers, GraphQL

### Shopify Webhooks API

Webhook subscriptions that enable apps to receive real-time notifications when events occur in a store — a performant alternative to polling.

**Human URL:** [https://shopify.dev/docs/api/webhooks](https://shopify.dev/docs/api/webhooks)

**Tags:** Commerce, Events, Webhooks

#### Properties

| Type | URL |
|------|-----|
| OpenAPI | [openapi/shopify-webhooks-api-openapi.yml](openapi/shopify-webhooks-api-openapi.yml) |
| Documentation | [https://shopify.dev/docs/api/webhooks](https://shopify.dev/docs/api/webhooks) |

### Shopify Ajax API

A suite of lightweight REST API endpoints for Shopify theme development — unauthenticated, used to add products to cart, show recommendations, and suggest products during search.

**Human URL:** [https://shopify.dev/docs/api/ajax](https://shopify.dev/docs/api/ajax)

**Tags:** Commerce, REST, Themes

#### Properties

| Type | URL |
|------|-----|
| OpenAPI | [openapi/shopify-ajax-api-openapi.yml](openapi/shopify-ajax-api-openapi.yml) |
| Documentation | [https://shopify.dev/docs/api/ajax](https://shopify.dev/docs/api/ajax) |

### Shopify Multipass API

Enables single sign-on by redirecting users from an external site and automatically logging them into the Shopify storefront. Requires a Shopify Plus plan.

**Human URL:** [https://shopify.dev/docs/api/multipass](https://shopify.dev/docs/api/multipass)

**Tags:** Authentication, Commerce, SSO

#### Properties

| Type | URL |
|------|-----|
| OpenAPI | [openapi/shopify-multipass-api-openapi.yml](openapi/shopify-multipass-api-openapi.yml) |
| Documentation | [https://shopify.dev/docs/api/multipass](https://shopify.dev/docs/api/multipass) |

### Shopify Functions API

Allows developers to customize backend logic with WebAssembly-compiled functions for custom discounts, payment customizations, delivery customizations, cart transforms, and order validation.

**Human URL:** [https://shopify.dev/docs/api/functions](https://shopify.dev/docs/api/functions)

**Tags:** Commerce, Serverless, WebAssembly

### Shopify Partner API

Provides access to Partners Dashboard data including transactions, app events, and Experts Marketplace opportunities via a GraphQL API.

**Human URL:** [https://shopify.dev/docs/api/partner](https://shopify.dev/docs/api/partner)

**Tags:** Commerce, GraphQL, Partners

### Shopify App Bridge

Enables apps to render UI in the Shopify app home surface and integrate with the Shopify admin — menus, save bars, toast notifications, resource pickers, and more.

**Human URL:** [https://shopify.dev/docs/api/app-bridge](https://shopify.dev/docs/api/app-bridge)

**Tags:** Commerce, Embedded Apps, UI

### Shopify Liquid API

Shopify's template language for building themes and customizing the storefront experience. Documents tags, filters, and objects available in Liquid templates.

**Human URL:** [https://shopify.dev/docs/api/liquid](https://shopify.dev/docs/api/liquid)

**Tags:** Commerce, Templates, Themes

### Shopify Hydrogen

Shopify's React-based framework for building custom storefronts powered by the Storefront API. Provides commerce-optimized components, hooks, and utilities.

**Human URL:** [https://shopify.dev/docs/storefronts/headless/hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen)

**Tags:** Commerce, Framework, Headless, React

### Shopify Polaris

Shopify's unified UI framework built on web components. Provides a library of UI components, tokens, and icons for building admin-consistent app interfaces.

**Human URL:** [https://shopify.dev/docs/api/polaris](https://shopify.dev/docs/api/polaris)

**Tags:** Commerce, Components, Design System, UI

## Capabilities

### Workflow Capabilities

| Capability | Description | REST Port | MCP Port |
|-----------|-------------|-----------|----------|
| [commerce-management](capabilities/commerce-management.yaml) | Unified Shopify commerce management covering products, orders, customers, inventory, fulfillments, and webhooks | 8080 | 9090 |

### Shared API Capabilities

| Capability | Description | REST Port | MCP Port |
|-----------|-------------|-----------|----------|
| [shared/admin-rest](capabilities/shared/admin-rest.yaml) | Shopify Admin REST API adapter with 8 resource endpoints | 8100 | 9100 |

### MCP Tools (commerce-management)

| Tool | Read-Only | Description |
|------|-----------|-------------|
| list-products | Yes | List store products with filters for status, vendor, product type |
| create-product | No | Create a new product listing |
| list-orders | Yes | List orders with status, financial status, fulfillment filters |
| create-order | No | Create a new order |
| list-customers | Yes | List customers with optional email filter |
| create-customer | No | Create a new customer record |
| list-collections | Yes | List custom product collections |
| list-inventory-levels | Yes | List inventory levels across locations |
| adjust-inventory | No | Adjust inventory quantity at a location |
| list-fulfillments | Yes | List fulfillments for an order |
| create-fulfillment | No | Fulfill an order with tracking information |
| list-webhooks | Yes | List configured webhook subscriptions |
| create-webhook | No | Create a webhook subscription for store events |

## Artifacts

| Type | File |
|------|------|
| OpenAPI | [openapi/shopify-api-openapi.yml](openapi/shopify-api-openapi.yml) |
| OpenAPI | [openapi/shopify-admin-rest-api-openapi.yml](openapi/shopify-admin-rest-api-openapi.yml) |
| OpenAPI | [openapi/shopify-ajax-api-openapi.yml](openapi/shopify-ajax-api-openapi.yml) |
| OpenAPI | [openapi/shopify-webhooks-api-openapi.yml](openapi/shopify-webhooks-api-openapi.yml) |
| OpenAPI | [openapi/shopify-multipass-api-openapi.yml](openapi/shopify-multipass-api-openapi.yml) |
| JSONSchema | [json-schema/shopify-product-schema.json](json-schema/shopify-product-schema.json) |
| JSONSchema | [json-schema/shopify-customer-schema.json](json-schema/shopify-customer-schema.json) |
| JSONSchema | [json-schema/shopify-order-schema.json](json-schema/shopify-order-schema.json) |
| JSONSchema | [json-schema/shopify-collection-schema.json](json-schema/shopify-collection-schema.json) |
| JSONSchema | [json-schema/shopify-inventory-item-schema.json](json-schema/shopify-inventory-item-schema.json) |
| JSONSchema | [json-schema/shopify-fulfillment-schema.json](json-schema/shopify-fulfillment-schema.json) |
| JSONStructure | [json-structure/shopify-product-structure.json](json-structure/shopify-product-structure.json) |
| JSONStructure | [json-structure/shopify-order-structure.json](json-structure/shopify-order-structure.json) |
| JSONLD | [json-ld/shopify-context.jsonld](json-ld/shopify-context.jsonld) |
| Example | [examples/shopify-create-product-example.json](examples/shopify-create-product-example.json) |
| Example | [examples/shopify-list-orders-example.json](examples/shopify-list-orders-example.json) |
| Vocabulary | [vocabulary/shopify-vocabulary.yml](vocabulary/shopify-vocabulary.yml) |
| SpectralRules | [rules/shopify-rules.yml](rules/shopify-rules.yml) |
| NaftikoCapability | [capabilities/shared/admin-rest.yaml](capabilities/shared/admin-rest.yaml) |
| NaftikoCapability | [capabilities/commerce-management.yaml](capabilities/commerce-management.yaml) |

## Common Properties

- [Documentation](https://shopify.dev/docs)
- [API Documentation](https://shopify.dev/docs/api)
- [Portal](https://shopify.dev)
- [Authentication](https://shopify.dev/docs/api/usage/authentication)
- [Versioning](https://shopify.dev/docs/api/usage/versioning)
- [Rate Limits](https://shopify.dev/docs/api/usage/rate-limits)
- [Changelog](https://shopify.dev/changelog)
- [Status](https://www.shopifystatus.com)
- [Support](https://shopify.dev/docs/api/usage/support)
- [Terms of Service](https://www.shopify.com/legal/api-terms)
- [Privacy Policy](https://www.shopify.com/legal/privacy)
- [Sign Up](https://partners.shopify.com/signup)
- [Community](https://community.shopify.dev/)
- [GitHub Organization](https://github.com/Shopify)
- [Partner Program](https://www.shopify.com/partners)
- [App Marketplace](https://apps.shopify.com)
- [YouTube](https://www.youtube.com/@shopifydevs)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/shopify)
- [CLI](https://shopify.dev/docs/api/shopify-cli)
- [SDKs](https://shopify.dev/docs/api/admin-rest/resources/sdk)
- [Webhooks](https://shopify.dev/docs/apps/build/webhooks)
- [Access Scopes](https://shopify.dev/docs/api/usage/access-scopes)
- [Getting Started](https://shopify.dev/docs/apps/build)
- [Headless Commerce](https://shopify.dev/docs/storefronts/headless)
- [Theme Development](https://shopify.dev/docs/themes)

## Maintainers

**Name:** Kin Lane
**Email:** kin@apievangelist.com
**URL:** http://apievangelist.com

**Name:** Shopify
**Email:** api@shopify.com
**URL:** https://www.shopify.com
