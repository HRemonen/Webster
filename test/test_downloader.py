import unittest
import requests

from webster.core.downloader import Downloader

class TestDownloader(unittest.TestCase):
    
    #Test giving accepted response to downloader
    def testOKResponse(self):
        response = requests.get("https://www.google.com/")
        downloader = Downloader()
        downloader.give_response(response)
        
        self.assertEqual(response, downloader._response)
    
    #Test giving a bad response type to downloader
    def testBADResponse(self):
        response = "I am a request"
        downloader = Downloader()
        
        with self.assertRaises(TypeError):
            downloader.give_response(response)

if __name__ == "__main__":
    unittest.main()