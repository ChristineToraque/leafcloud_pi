import unittest
from unittest.mock import patch, MagicMock
import sys

# Mock hardware libraries BEFORE importing leaf_node
mock_board = MagicMock()
mock_busio = MagicMock()
mock_ads = MagicMock()
sys.modules["board"] = mock_board
sys.modules["busio"] = mock_busio
sys.modules["adafruit_ads1x15"] = MagicMock()
sys.modules["adafruit_ads1x15.ads1115"] = mock_ads
sys.modules["adafruit_ads1x15.analog_in"] = MagicMock()

import leaf_node

class TestLeafNode(unittest.TestCase):
    @patch('leaf_node.requests.get')
    def test_get_active_command_success(self, mock_get):
        # Mock a successful response with an active_bucket_id
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"active_bucket_id": "test-bucket-123"}
        mock_get.return_value = mock_response

        result = leaf_node.get_active_command()
        self.assertEqual(result, {"active_bucket_id": "test-bucket-123"})

    @patch('leaf_node.requests.get')
    def test_get_active_command_none_on_404(self, mock_get):
        # Mock a 404 response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = leaf_node.get_active_command()
        self.assertIsNone(result)

    @patch('leaf_node.requests.get')
    def test_get_active_command_none_on_error(self, mock_get):
        # Mock a connection error
        mock_get.side_effect = Exception("Connection error")

        result = leaf_node.get_active_command()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
