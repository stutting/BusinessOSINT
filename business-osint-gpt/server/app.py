from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

def load_json(filename):
    """Utility function to load a JSON file from mock_data directory."""
    filepath = os.path.join(os.path.dirname(__file__), 'mock_data', filename)
    with open(filepath, 'r') as f:
        return json.load(f)

@app.route('/search_companies')
def search_companies():
    data = load_json('search_companies.json')
    query = request.args.get('query')
    return jsonify(data)

@app.route('/get_market_trends')
def get_market_trends():
    data = load_json('market_trends.json')
    keyword = request.args.get('keyword')
    geo = request.args.get('geo')
    return jsonify(data)

@app.route('/get_local_competitors')
def get_local_competitors():
    data = load_json('local_competitors.json')
    term = request.args.get('term')
    location = request.args.get('location')
    return jsonify(data)

@app.route('/get_industry_data')
def get_industry_data():
    data = load_json('industry_data.json')
    naics = request.args.get('naics')
    return jsonify(data)

@app.route('/get_customer_data')
def get_customer_data():
    data = load_json('customer_data.json')
    location = request.args.get('location')
    return jsonify(data)

@app.route('/get_grants')
def get_grants():
    data = load_json('grants.json')
    keyword = request.args.get('keyword')
    return jsonify(data)

@app.route('/get_website_stack')
def get_website_stack():
    data = load_json('website_stack.json')
    url = request.args.get('url')
    return jsonify(data)

@app.route('/get_ad_transparency')
def get_ad_transparency():
    data = load_json('ad_transparency.json')
    query = request.args.get('query')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
