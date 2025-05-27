from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), 'mock_data')

def load_json(filename):
    """Utility to load a JSON file from the mock_data directory."""
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'r') as f:
        return json.load(f)

@app.route('/search_companies')
def search_companies():
    return jsonify(load_json('search_companies.json'))

@app.route('/market_trends')
def market_trends():
    return jsonify(load_json('get_market_trends.json'))

@app.route('/local_competitors')
def local_competitors():
    return jsonify(load_json('get_local_competitors.json'))

@app.route('/industry_data')
def industry_data():
    return jsonify(load_json('get_industry_data.json'))

@app.route('/customer_data')
def customer_data():
    return jsonify(load_json('get_customer_data.json'))

@app.route('/grants')
def grants():
    return jsonify(load_json('get_grants.json'))

@app.route('/website_stack')
def website_stack():
    return jsonify(load_json('get_website_stack.json'))

@app.route('/ad_transparency')
def ad_transparency():
    return jsonify(load_json('get_ad_transparency.json'))

if __name__ == '__main__':
    app.run(debug=True)
