# Tool Guide

This guide lists the free public data tools used by **Business OSINT Assistant** and how the GPT utilizes them.

## OpenCorporates
- **Purpose:** Search official company registrations worldwide.
- **Usage:** `search_companies` action queries company names or keywords to identify legal entities.

## Google Trends
- **Purpose:** Understand interest in topics over time and by location.
- **Usage:** `get_market_trends` action provides trend scores for specific keywords.

## Yelp API
- **Purpose:** Discover local businesses and their ratings.
- **Usage:** `get_local_competitors` action lists nearby competitors based on a search term and location.

## NAICS / Census API
- **Purpose:** Provide industry classification and statistical data in the U.S.
- **Usage:** `get_industry_data` action retrieves counts of establishments and employment numbers for a NAICS code.

## DataUSA
- **Purpose:** Offer demographic and economic information for regions and industries.
- **Usage:** `get_customer_data` action supplies population and income data for a specified location.

## Grants.gov
- **Purpose:** List federal grant opportunities.
- **Usage:** `get_grants` action returns grants that match keywords and optional state filters.

## BuiltWith
- **Purpose:** Detect technologies used on websites.
- **Usage:** `get_website_stack` action summarizes frameworks and services running on a given URL.

## Meta Ad Library
- **Purpose:** Search ads that businesses run across Meta platforms.
- **Usage:** `get_ad_transparency` action delivers ad counts and related information for a search term.

The GPT selects these tools based on the user's request. If an API call fails, it can provide fallback links so users can continue researching manually.
