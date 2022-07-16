import unittest
from unittest.mock import Mock, patch

from webster.net.request import Request

class TestRequest(unittest.TestCase):
    #Alias for Request class
    request_class = Request
    
    def testRequestBADInit(self):
        #Requests must have URL.
        #Except to raise exception when initializing.
        self.assertRaises(Exception, self.request_class)
    
    def testRequestInit(self):
        #Create test request.
        test_url = "https://www.example.com"
        request = self.request_class(test_url)
        
        #Test URL is of string type
        assert isinstance(request.url, str)

        #Test URL is correct
        self.assertEqual(request.url, test_url)
        
        #Test method is correct
        self.assertEqual(request.method, "GET")
        
        #Test encoding is correct
        self.assertEqual(request._encoding, "utf-8")
        
        #Test request body is there
        assert request.body is not None
        
    def testRequestURL(self):
        test_url = "https://www.example.com"
        request = self.request_class(test_url)
        
        self.assertEqual(request.url, test_url)
    
    def testRequestEncoding(self):
        test_url = "https://www.example.com"
        request = self.request_class(test_url)
        
        self.assertEqual(request._encoding, "utf-8")
    
    def testRequestBody(self):
        request = self.request_class(url="https://www.example.com", body=b"")
        
        assert request.body == b''
        
        test_url = "https://www.example.com"
        request = self.request_class(test_url)
        
        assert isinstance(request.body, bytes)
        
        request = self.request_class(url="http://www.example.com/", body=b"Foo: \c4", encoding='utf-8')
        assert isinstance(request.body, bytes)
        self.assertEqual(request.body, b"Foo: \c4")

        request = self.request_class(url="http://www.example.com/", body=b"\xa31", encoding='latin1')
        assert isinstance(request.body, bytes)
        self.assertEqual(request.body, b"\xa31")
        
    def testRequestStatusCode(self):
        raise NotImplementedError

if __name__ == "__main__":
    unittest.main()