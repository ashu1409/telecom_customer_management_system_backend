# backend/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for customers and plans (replace with actual database logic)
customers = []
plans = [
    {'planName': 'Platinum365', 'planCost': 499, 'validity': 365, 'planStatus': 'Active'},
    {'planName': 'Gold180', 'planCost': 299, 'validity': 180, 'planStatus': 'Active'},
    {'planName': 'Silver90', 'planCost': 199, 'validity': 90, 'planStatus': 'Active'}
]

# API endpoints for managing customers and plans
@app.route('/api/customers', methods=['POST'])
def register_customer():
    data = request.json
    customers.append(data)  # Add customer to the list (replace with database logic)
    return jsonify({'message': 'Customer registered successfully'})

@app.route('/api/plans', methods=['POST'])
def choose_plan():
    data = request.json
    # Logic to choose a plan (replace with actual implementation)
    return jsonify({'message': 'Plan selected successfully'})

@app.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True)
