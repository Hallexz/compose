import unittest
from unittest.mock import patch, Mock
import alarm 

class TestMemoryUsage(unittest.TestCase):
    @patch('psutil.Process')
    def test_memory_usage(self, mock_process):
        mock_process.return_value.memory_info.return_value.rss = 1024
        self.assertEqual(alarm.memory_usage(), 1024)

class TestSendAlert(unittest.TestCase):
    @patch('requests.post')
    def test_send_alert(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        self.assertEqual(alarm.send_alert(1024), 200)

if __name__ == '__main__':
    unittest.main()

