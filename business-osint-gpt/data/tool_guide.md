# Tool Guide

This guide outlines the free data sources used by the Business OSINT Assistant and how each tool can help your business research.

## OpenCorporates
- **What it is**: A large open database of company information.
- **Use case**: Find company registration details when verifying competitors or partners.
- **GPT usage**: The assistant queries `/search_companies` to return matching company records.

## Google Trends (PyTrends)
- **What it is**: A Python library that proxies Google Trends.
- **Use case**: Identify interest over time for keywords or topics.
- **GPT usage**: Calls `/get_market_trends` with a keyword and optional region.

## Yelp Fusion API
- **What it is**: Provides business listings and reviews.
- **Use case**: Discover local competitors and customer ratings.
- **GPT usage**: Uses `/get_local_competitors` to list nearby businesses.

## NAICS / Census API
- **What it is**: U.S. Census Bureau data organized by NAICS industry codes.
- **Use case**: Gather statistics on industry size and employment.
- **GPT usage**: Fetches data from `/get_industry_data`.

## DataUSA
- **What it is**: Aggregated demographic and economic information.
- **Use case**: Understand customer demographics by location.
- **GPT usage**: Retrieves stats via `/get_customer_data`.

## Grants.gov
- **What it is**: Federal government grant listings.
- **Use case**: Find potential funding opportunities.
- **GPT usage**: Searches using `/get_grants`.

## BuiltWith
- **What it is**: Tool for analyzing website technology stacks.
- **Use case**: See what technologies competitors use.
- **GPT usage**: Provides a direct link to `https://builtwith.com/<domain>` via `/get_website_stack` output.

## Meta Ad Library
- **What it is**: Transparency database of ads on Meta platforms.
- **Use case**: Research advertiser activity in your market.
- **GPT usage**: Returns a search link formatted as `https://www.facebook.com/ads/library/?active_status=all&search_type=keyword&q=<query>` from `/get_ad_transparency`.
