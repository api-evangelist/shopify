---
title: "Teaching Sidekick to say no: automated data curation with LLM judge consensus"
url: "https://shopify.engineering/sidekick-curation"
date: "2026-06-15"
author: "Shuang Xie"
feed_url: "https://shopify.engineering/"
---
Shopify's Sidekick AI assistant lacked training examples for refusing impossible requests because production logs only captured successful queries. The team built an automated curation pipeline using four frontier LLMs as judges, calibrated on 602 refusal annotations and requiring unanimous consensus, reaching 86.3% refusal accuracy with a 4.6% false positive rate. The approach lifted the customer segmentation skill's evaluation score from 0.619 to 0.798, a 28.9% relative gain.
