from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv('MONGO_URI')) # Connect to MongoDB Atlas, or use localhost "mongodb://localhost:27017/"
db = client.portfolio_db
portfolios = db.portfolios

@app.route('/portfolio', methods=['POST'])
def add_portfolio():
    data = request.json
    portfolios.insert_one(data)
    return jsonify({"msg": "Portfolio added successfully!"}), 201

@app.route('/portfolio/<name>', methods=['GET'])
def get_portfolio(name):
    portfolio = portfolios.find_one({"name": name})
    if portfolio:
        return jsonify(portfolio), 200
    return jsonify({"msg": "Portfolio not found!"}), 404


@app.route('/portfolio', methods=['GET'])
def get_all_portfolios():
    portfolio_list = list(portfolios.find({}))

    # Convert ObjectId to string for JSON serialization
    for portfolio in portfolio_list:
        portfolio['_id'] = str(portfolio['_id'])

    return jsonify(portfolio_list), 200

if __name__ == '__main__':
    app.run(debug=True)
