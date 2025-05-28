import unittest
from unittest.mock import patch, MagicMock
import function_app

class MockRequest:
    def __init__(self):
        self.method = 'GET'

class TestVisitorCounter(unittest.TestCase):

    @patch('function_app.TableServiceClient')
    @patch('function_app.os.environ', {'COSMOS_DB_CONNECTION_STRING': 'fake_connection_string'})
    def test_visit_counter_success(self, mock_table_service_client):
        # Setup mock table client and entity
        mock_table_client = MagicMock()
        mock_table_client.get_entity.return_value = {"PartitionKey": "visitor", "RowKey": "count", "count": 7}

        # Mock the TableServiceClient return
        mock_table_service_client.from_connection_string.return_value.get_table_client.return_value = mock_table_client

        # Call the function
        response = function_app.visit_counter(MockRequest())

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn('"count": 8', response.get_body().decode())

if __name__ == '__main__':
    unittest.main()
