# Business OSINT Assistant

**Business OSINT Assistant** is a CustomGPT project that helps small U.S. businesses gather open-source intelligence from free public data sources. It exposes a simple Flask API with mock endpoints and includes references for integrating with real services.

![Screenshot Placeholder](.gpt/thumbnail.png)

## Running the Mock Server

1. Ensure you have Python 3 and Flask installed.
2. Navigate to the `server` directory and run:
   ```bash
   python app.py
   ```
3. The API will be available at `http://localhost:5000`.

## Testing Endpoints

Each endpoint returns example JSON. Try them in a browser or with `curl`:

- `/search_companies?query=bakery`
- `/market_trends?keyword=coffee&location=us`
- `/local_competitors?term=bakery&location=madison+wi`
- `/industry_data?naics_code=722310`
- `/customer_data?location=Miami,FL`
- `/grants?keyword=cleaning&state=TX`
- `/website_stack?url=https://example.com`
- `/ad_transparency?search_term=yoga`

## Deployment on GitHub

Commit the project to a public GitHub repository. GitHub Pages can host the static files, while the Flask server can be deployed separately (e.g., on Heroku or Fly.io) if needed.

## Uploading to GPT Builder

1. In GPT Builder, create a new Custom GPT.
2. Upload `actions.json` as the manifest file.
3. Upload `openapi.yaml` as the API specification.
4. Optionally include `.gpt/example_prompts.json` for testing prompts.

The GPT will then be able to call the defined actions or provide direct links to the referenced tools.
