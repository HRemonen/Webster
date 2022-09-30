import unittest

from webster.net.request import Request
from webster.core.parser import Parser
from test.test_data import get_testdata

class TestParser(unittest.TestCase):
    
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
    
    #Aliases
    request_class = Request
    parser_class = Parser
    
    #Create mock "response" object from the test html files to test parsing
    mock_body = get_testdata("test_site", "index.html")
    mock_request = Request(url="https://www.example.com/index", body=mock_body)
    
    def testParserBADInit(self):
        #Parser must have a Request object as parameter.
        #Except to raise TypeError when initializing.
        
        #Test without parameters
        self.assertRaises(TypeError, self.parser_class)
        
        #Test with bad parameter type
        self.assertRaises(TypeError, self.parser_class, "Request")
    
    def testParserInit(self):
        r = self.request_class(url="https://www.example.com")
        parser = self.parser_class(request=r)
        
        #Test Parser request is Request
        assert isinstance(parser.request, Request)
        
        #Test Parser "response" is bytes
        assert isinstance(parser.response, bytes)
        
    def testParseAnchorsBAD(self):
        #Test TypeError if Request could not be requested.
        #Failed Requests have body of None type.
        
        r = self.request_class(url="https://www")
        parser = self.parser_class(request=r)
        self.assertRaises(Exception, parser.parse_anchors)
        
    def testParseAnchorsMock(self):
        #Test succesful parsing returning list of elements.
        r = self.mock_request
        anchors = self.parser_class(request=r).parse_anchors()
        assert isinstance(anchors, list)
        
        self.assertEqual(len(anchors), len(self.INDEX_PAGE_LINKS))
    
    def testParseAnchorsResults(self):
        body = get_testdata("test_parse", "linkparse.html")
        request = Request(url="https://www.example.com/linkparse", body=body)
        anchors = self.parser_class(request=request).parse_anchors()
        
        assert isinstance(anchors, list)
        
        self.assertEqual(len(anchors), len(self.LINK_PARSE_PAGE_LINKS))
        
    def testParserIndexBAD(self):
        #Test bad url raises error
        r = self.request_class(url="https://www")
        parser = self.parser_class(request=r)
        self.assertRaises(Exception, parser.parse_index)
    
    def testParserIndexMock(self):  
        #Test succesful parsing returning list of indices or dataset.
        r = self.mock_request
        mock_url = r._get_url()
        indices = self.parser_class(request=r).parse_index()
        assert isinstance(indices, dict)
        
    def testParserIndexMockResults(self):
        r = self.mock_request
        mock_url = r._get_url()
        mock_adjacent = self.parser_class(request=r).parse_anchors()
        indices = self.parser_class(request=r).parse_index()
        
        #Test that indice url is the same as requests
        #and that it is type str
        assert isinstance(indices["url"], str)
        self.assertEqual(indices["url"], mock_url)
        
        #Test adjacent urls are type list
        assert isinstance(indices["adjacents"], list)
        self.assertEqual(indices["adjacents"], mock_adjacent)
        
        print(indices)
        
if __name__ == "__main__":
    unittest.main()   