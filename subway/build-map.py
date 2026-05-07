#!/usr/bin/env python3
"""Build the Shopify API tube-style map.

20 of Shopify's developer surfaces grouped onto 5 lines.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Customer Account API": "Customer Account",
    "Discount Function":    "Discount Functions",
    "Checkout UI":          "Checkout UI",
    "POS UI":               "POS UI",
    "Admin Extensions":     "Admin Ext.",
}

LINES = [
    {
        "name": "Admin & Storefront",
        "color": "#95BF47",  # Shopify green
        "stations": [
            ("Admin REST API",  (260, 200)),
            ("GraphQL Admin",   (440, 175)),
            ("Storefront",      (620, 165)),
            ("Customer Account API",(810, 175)),
            ("Partner",         (1000, 200)),
        ],
    },
    {
        "name": "Commerce & Payments",
        "color": "#E68B1F",
        "stations": [
            ("Webhooks",         (340, 320)),
            ("Multipass",        (570, 295)),
            ("Payments Apps",    (820, 320)),
        ],
    },
    {
        "name": "Theme & UI",
        "color": "#7B3FE4",
        "stations": [
            ("Liquid",       (260, 460)),
            ("AJAX",         (400, 440)),
            ("Polaris",      (540, 440)),
            ("App Bridge",   (680, 440)),
            ("Hydrogen",     (820, 460)),
        ],
    },
    {
        "name": "Functions",
        "color": "#C5318B",
        "stations": [
            ("Functions",         (270, 580)),
            ("Discount Function", (470, 555)),
            ("Shopify CLI",       (700, 580)),
        ],
    },
    {
        "name": "Extensions",
        "color": "#5A6275",
        # Closed quadrilateral at the bottom-right.
        "closed": True,
        "stations": [
            ("Checkout UI",      (820, 660)),
            ("POS UI",           (920, 730)),
            ("Admin Extensions", (820, 800)),
            ("App Home",         (720, 730)),
        ],
    },
]

URL_OVERRIDES = {
    "Admin REST API":      "https://apis.apis.io/apis/shopify/shopify-api/",
    "GraphQL Admin":       "https://apis.apis.io/apis/shopify/graphql-admin-api/",
    "Storefront":          "https://apis.apis.io/apis/shopify/storefront-api/",
    "Customer Account API":"https://apis.apis.io/apis/shopify/customer-account-api/",
    "Partner":             "https://apis.apis.io/apis/shopify/partner-api/",
    "Webhooks":            "https://apis.apis.io/apis/shopify/webhooks-api/",
    "Multipass":           "https://apis.apis.io/apis/shopify/multipass-api/",
    "Payments Apps":       "https://apis.apis.io/apis/shopify/payments-apps-api/",
    "Liquid":              "https://apis.apis.io/apis/shopify/liquid-api/",
    "AJAX":                "https://apis.apis.io/apis/shopify/ajax-api/",
    "Polaris":             "https://apis.apis.io/apis/shopify/polaris/",
    "App Bridge":          "https://apis.apis.io/apis/shopify/app-bridge/",
    "Hydrogen":            "https://apis.apis.io/apis/shopify/hydrogen/",
    "Functions":           "https://apis.apis.io/apis/shopify/functions-api/",
    "Discount Function":   "https://apis.apis.io/apis/shopify/discount-function-api/",
    "Shopify CLI":         "https://apis.apis.io/apis/shopify/shopify-cli/",
    "Checkout UI":         "https://apis.apis.io/apis/shopify/checkout-ui-extensions-api/",
    "POS UI":              "https://apis.apis.io/apis/shopify/pos-ui-extensions-api/",
    "Admin Extensions":    "https://apis.apis.io/apis/shopify/admin-extensions-api/",
    "App Home":            "https://apis.apis.io/apis/shopify/app-home-api/",
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)
    build_subway(
        title="The Shopify API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: shopify/openapi/*.yml · github.com/api-evangelist/shopify",
        out_dir=Path(__file__).resolve().parent,
        out_basename="shopify-subway-map",
        provider_id="shopify",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
