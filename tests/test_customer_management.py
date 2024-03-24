import unittest
from app import app

class TestCustomerManagement(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_customer(self):
        # Test customer registration endpoint
        data = {
            'name': 'Test Customer',
            'email': 'test@example.com',
            'mobileNumber': '1234567890'
        }
        response = self.app.post('/api/customers', json=data)
        self.assertEqual(response.status_code, 200)

    def test_choose_plan(self):
        # Test plan selection endpoint
        data = {'planName': 'Platinum365'}
        response = self.app.post('/api/plans', json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_customers(self):
        # Test customer retrieval endpoint
        response = self.app.get('/api/customers')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
