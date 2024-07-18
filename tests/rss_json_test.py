import unittest
from unittest.mock import patch, Mock
import argparse
from sources import rss_json
from xmlrunner import XMLTestRunner  # Import the XMLTestRunner

class rss_json_test(unittest.TestCase):

    @patch('requests.get')
    @patch('builtins.print')
    def test_post_rss_json_success(self, mock_print, mock_get):
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

        rss_json.post_rss_json("http://test.rss")
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

        rss_json.parse_rss_json("http://test.rss")
        mock_print.assert_any_call('Title:', 'Test Feed')
        mock_print.assert_any_call('Feed Url:', 'http://test.feed')
        mock_print.assert_any_call('Number of Blogs:', 2)
    

    @patch('builtins.print')
    @patch('argparse.ArgumentParser.parse_args')
    def test_main_api_option(self, mock_parse_args, mock_print):
        # Simulate command-line arguments
        mock_parse_args.return_value = argparse.Namespace(options='api', feedurl="http://test.rss")
        
        # Call the main function
        rss_json.main()
        
        # Assertions to ensure correct functions were called
        mock_print.assert_any_call("Selected RSS to JSON option: ", 'api')


    @patch('builtins.print')
    @patch('argparse.ArgumentParser.parse_args')
    def test_main_feedparser_option(self, mock_parse_args, mock_print):
        # Simulate command-line arguments
        mock_parse_args.return_value = argparse.Namespace(options='feedparser', feedurl="http://test.rss")
        
        # Call the main function
        rss_json.main()
        
        # Assertions to ensure correct functions were called
        mock_print.assert_any_call("Selected RSS to JSON option: ", 'feedparser')

    @patch('sources.rss_json.post_rss_json')
    @patch('builtins.print')
    @patch('argparse.ArgumentParser.parse_args')
    def test_main_default_feedurl(self, mock_parse_args, mock_print, mock_post_rss_json):
        # Simulate command-line arguments
        mock_parse_args.return_value = argparse.Namespace(options='api', feedurl="https://medium.com/feed/@lucaslin0102")
        
        # Call the main function
        rss_json.main()
        
        # Assertions to ensure correct functions were called
        mock_print.assert_any_call("Selected RSS to JSON option: ", 'api')
        mock_post_rss_json.assert_called_once_with("https://medium.com/feed/@lucaslin0102")

if __name__ == '__main__':
    with open('xunit-result.xml', 'wb') as output:
        unittest.main(testRunner=XMLTestRunner(output=output))