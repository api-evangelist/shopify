# Programmatic API Onboarding — Shopify

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for Shopify: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`shopify-api-auth.mjs`](shopify-api-auth.mjs)
- Run `node shopify-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/21/shopify-app-registration-is-dashboard-only/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
