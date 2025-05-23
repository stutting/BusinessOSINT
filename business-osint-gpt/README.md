# Business OSINT Assistant

Business OSINT Assistant helps small U.S. business owners gather open-source intelligence about markets, competitors, customers, and government programs using only free data sources.

![Screenshot](.gpt/thumbnail.png)

## Running the Flask Server

1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Start the server:
   ```bash
   python server/app.py
   ```
3. The API will be available at `http://localhost:5000`.

## Testing Endpoints

Use `curl` or a browser to hit each endpoint. Example:
```bash
curl "http://localhost:5000/search_companies?query=bakery"
```

## Deployment on GitHub

Push this repository to GitHub. Enable GitHub Actions or your own CI/CD pipeline if desired.

## Uploading to GPT Builder

1. Go to [https://platform.openai.com/](https://platform.openai.com/) and create a new GPT.
2. Upload `actions.json` and `openapi.yaml` when prompted.
3. Use the provided example prompts to test the assistant.


