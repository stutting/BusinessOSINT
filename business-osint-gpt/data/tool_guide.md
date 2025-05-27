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
=======
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

