import unittest

from webster.utils import url_tools

class TestTools(unittest.TestCase):
    def testNetlocUrlOK(self):
        url = "https://example.com/HRemonen/"
        
        self.assertEqual(url_tools.netloc_url(url),
                         "example.com")
    
    def testNetlocUrlBAD(self):
        bad_url = "mailto:info@example.com"
        
        self.assertEqual(url_tools.netloc_url(bad_url),
                         "")
        with self.assertRaises(TypeError):
            url_tools.netloc_url(12)
        
    def testBaseUrlOK(self):
        url = "https://example.com/HRemonen/Webster/"
        
        self.assertEqual(url_tools.base_url(url),
                         "https://example.com/")
        
    def testBaseUrlBAD(self):
        url = "https:/HRemonen/Webster/"
        
        self.assertEqual(url_tools.base_url(url),
                         "")
        self.assertEqual(url_tools.base_url("https:/"),
                         "")
        with self.assertRaises(TypeError):
            url_tools.base_url(12)
        
        
if __name__ == "__main__":
    unittest.main()