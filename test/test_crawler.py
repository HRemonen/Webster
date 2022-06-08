import queue
import unittest

from webster.crawler import Crawler

PARAM2 = "https://google.com/"
PARAM21 = ["https://google.com/", 
            "https://github.com/", 
            "https://youtube.com/"]
PARAM21BAD = ["google.com/", 
            "https://.com/", 
            "https://youtube./"]


class TestCrawler(unittest.TestCase):
    #Test class init with valid parameters
    def testInitOK(self):
        ws1 = Crawler(PARAM2)
        
        self.assertEqual(ws1.start_urls, PARAM2),
        self.assertEqual(ws1.queue.qsize(), 0)
        self.assertEqual(ws1.mode, "auto")     
        
        ws2 = Crawler(PARAM2, mode="manual")
        self.assertEqual(ws2.mode, "manual")
    
    #Test class init with bad mode
    def testInitBadMode(self):
        with self.assertRaises(TypeError):
            ws1 = Crawler(PARAM2, mode="bad", autoQueue=True)
    
    #Test class init start URLs working correctly
    def testInitURLValidity(self):
        ws1 = Crawler(PARAM2)
        ws2 = Crawler(PARAM2, allowed_urls=PARAM21)
        
        self.assertEqual(ws1.start_urls, PARAM2)
        
        self.assertEqual(ws2.start_urls, PARAM2)
    
    #Test class init start URLs bad input
    def testInitBadURLValidity1(self):    
        with self.assertRaises(TypeError):
            ws1 = Crawler(PARAM21BAD)
        with self.assertRaises(TypeError):
            ws2 = Crawler(PARAM21BAD[0])
    
    #Test class init start URLs bad input      
    def testInitBadURLValidity2(self):
        with self.assertRaises(RuntimeError):
            ws3 = Crawler(PARAM21, allowed_urls=PARAM21BAD)

if __name__ == "__main__":
    unittest.main()
