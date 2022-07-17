import unittest

import requests

from webster.net.request import Request
from webster.core.parser import Parser
from test.test_data import get_testdata

class TestParser(unittest.TestCase):
    
    #Aliases
    request_class = Request
    parser_class = Parser
    
    #Create mock "response" object from local html files to test parsing
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
        
    def testParseAnchors(self):
        #Test TypeError if Request could not be requested.
        #Failed Requests have body of None type.
        
        r = self.request_class(url="https://www")
        parser = self.parser_class(request=r)
        self.assertRaises(Exception, parser.parse_anchors)
        
        #Test succesful parsing returning list of elements.
        r = self.mock_request
        anchors = self.parser_class(request=r).parse_anchors()
        assert isinstance(anchors, list)
        self.assertEqual(anchors, [])
    
    def testParseAnchorsWithLinks(self):
        body = get_testdata("test_parse", "linkparse.html")
        request = Request(url="https://www.example.com/linkparse", body=body)
        anchors = self.parser_class(request=request).parse_anchors()
        
        print(anchors)
        
if __name__ == "__main__":
    unittest.main()   