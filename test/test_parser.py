
import unittest
import requests
import os

from webster.core.parser import Parser
from webster.core.downloader import Downloader

ROOT_DIR = os.path.abspath(os.curdir)

class TestParser(unittest.TestCase):
    
    #Test giving accepted response to parser.
    def testParserOKResponseInit(self):
        response = requests.get("https://www.google.com/")
        p = Parser(response)
        
        self.assertEqual(response, p.response)
    

if __name__ == "__main__":
    unittest.main()