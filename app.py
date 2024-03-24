# backend/app.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load customer and plan data from JSON files
with open('customers.json') as f:
    customers = json.load(f)

with open('plans.json') as f:
    plans = json.load(f)

# Endpoint to register new customers
@app.route('/api/customers', methods=['POST'])
def register_customer():
    data = request.json
   
