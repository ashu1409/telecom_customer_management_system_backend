from flask import Flask, request, jsonify

app = Flask(__name__)

# Define routes for managing customers and plans


@app.route('/api/customers', methods=['POST'])
def register_customer():
    data = request.json
    # Logic to register a new customer
    return jsonify({'message': 'Customer registered successfully'})


@app.route('/api/plans', methods=['POST'])
def choose_plan():
    data = request.json
    # Logic to choose a plan
    return jsonify({'message': 'Plan selected successfully'})


@app.route('/api/customers', methods=['GET'])
def get_customers():
    # Logic to retrieve customers from database
    customers = [{'id': 1, 'name': 'John', 'email': 'john@example.com', 'mobileNumber': '1234567890'}]
    return jsonify(customers)


if __name__ == '__main__':
    app.run(debug=True)
