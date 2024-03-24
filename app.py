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
    if not all(field in data for field in ['name', 'dob', 'email', 'adharNumber', 'assignedMobileNumber']):
        return jsonify({'error': 'Missing fields'}), 400
    # Generate customer ID (assuming IDs are unique)
    data['id'] = len(customers) + 1
    customers.append(data)
    with open('customers.json', 'w') as f:
        json.dump(customers, f, indent=4)
    return jsonify({'message': 'Customer registered successfully'}), 201

# Endpoint to choose new plan
@app.route('/api/plans', methods=['POST'])
def choose_plan():
    data = request.json
    if not all(field in data for field in ['planName', 'planCost', 'validity']):
        return jsonify({'error': 'Missing fields'}), 400
    plans.append(data)
    with open('plans.json', 'w') as f:
        json.dump(plans, f, indent=4)
    return jsonify({'message': 'Plan chosen successfully'}), 201

# Endpoint to display customer table
@app.route('/api/customers', methods=['GET'])
def display_customers():
    return jsonify(customers)

if __name__ == "__main__":
    app.run(debug=True)
