import unittest

from webster.net.request import Request
from webster.core.downloader import Downloader


class TestDownloader(unittest.TestCase):
    #CONSTANTS 
    INDEX_PAGE_LINKS = [
        "page1.html",
        "page2.html",
        "page-not-found.html"
        ]
    
    LINK_PARSE_PAGE_LINKS = [
        '/sample2.html',
        'http://example.com/sample3.html',
        '/sample3.html',
        '/sample3.html#foo',
        'http://www.google.com/something',
        'http://example.com/innertag.html',
        '/page 4.html'
    ]
    
    #ALIASES
    request_class = Request
    downloader_class = Downloader
    
    #MOCKS
    mock_body = get_testdata("test_site", "index.html")
    mock_request = Request(url="https://www.example.com/index", body=mock_body)