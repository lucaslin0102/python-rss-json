import unittest
from unittest.mock import patch, Mock
import requests
import feedparser

# Import the functions from your script
from rss_json import post_rss_json, parse_rss_json  # replace 'rss_json' with the actual module name

class TestRSSFunctions(unittest.TestCase):

    @patch('requests.get')
    @patch('builtins.print')
    def test_post_rss_json_success(self, mock_print, mock_get):
        # Create a mock response object with the desired properties
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "feed": {"title": "Test Feed", "url": "http://test.feed"},
            "items": [
                {"title": "Test Blog 1", "link": "http://blog1.test", "author": "Author 1", "pubDate": "2023-01-01"},
                {"title": "Test Blog 2", "link": "http://blog2.test", "author": "Author 2", "pubDate": "2023-01-02"},
            ]
        }
        mock_get.return_value = mock_response

        post_rss_json("http://test.rss")
        mock_print.assert_any_call('Title:', 'Test Feed')
        mock_print.assert_any_call('Feed Url:', 'http://test.feed')
        mock_print.assert_any_call('Number of Blogs:', 2)

    @patch('feedparser.parse')
    @patch('builtins.print')
    def test_parse_rss_json_success(self, mock_print, mock_parse):
        mock_parse.return_value = {
            "feed": {"title": "Test Feed", "title_detail": {"base": "http://test.feed"}},
            "entries": [
                {"title": "Test Blog 1", "link": "http://blog1.test", "author": "Author 1", "published": "2023-01-01"},
                {"title": "Test Blog 2", "link": "http://blog2.test", "author": "Author 2", "published": "2023-01-02"},
            ]
        }

        parse_rss_json("http://test.rss")
        mock_print.assert_any_call('Title:', 'Test Feed')
        mock_print.assert_any_call('Feed Url:', 'http://test.feed')
        mock_print.assert_any_call('Number of Blogs:', 2)

if __name__ == '__main__':
    unittest.main()
