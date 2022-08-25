import unittest

from webster.utils import url_tools

class TestTools(unittest.TestCase):
    def testURLnetlocOK(self):
        url = "https://github.com/HRemonen/Webster/"
        
        self.assertEqual(url_tools.URLnetloc(url),
                         "github.com")
    
    def testURLnetlocBAD(self):
        bad_url = "mailto:info@example.com"
        
        self.assertEqual(url_tools.URLnetloc(bad_url),
                         "")
        
if __name__ == "__main__":
    unittest.main()