import unittest

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
        #Assert that Request body as parameter is bytes.
        request = self.request_class(url="https://www.example.com", body=b"")
        assert request.body == b''
        
        #Assert TypeError gets raised if given body is not bytes.
        self.assertRaises(TypeError, self.request_class, url="https://www.example.com", body=12)
        
        #Assert that Request body is bytes.
        test_url = "https://www.example.com"
        request = self.request_class(test_url)
        assert isinstance(request.body, bytes)
        
        #Assert that Request body is bytes when using standard encoding.
        request = self.request_class(url="http://www.example.com/", body=b"Foo: \c4", encoding='utf-8')
        assert isinstance(request.body, bytes)
        self.assertEqual(request.body, b"Foo: \c4")

        #Assert that Request body is bytes when using latin encoding.
        request = self.request_class(url="http://www.example.com/", body=b"\xa31", encoding='latin1')
        assert isinstance(request.body, bytes)
        self.assertEqual(request.body, b"\xa31")
    
    @unittest.skip("not implemented test") 
    def testRequestStatusCode(self):
        raise NotImplementedError
    
    def testRequestEqual(self):
        #Test Requests are not equal despite same url.
        r1 = self.request_class(url="https://www.example.com")
        r2 = self.request_class(url="https://www.example.com")
        self.assertNotEqual(r1, r2)
        
        #Test Requests are not equal and can be part of set
        #without any problems
        test_set = set()
        test_set.add(r1)
        test_set.add(r2)
        self.assertEqual(len(test_set), 2)
        
if __name__ == "__main__":
    unittest.main()