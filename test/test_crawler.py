import queue
import unittest

from webster.crawler import Crawler


OKSites = ["https://google.com/", 
            "https://github.com/", 
            "https://youtube.com/"]
BADSites = ["google.com/", 
            "https://.com/", 
            "https://youtube./"]


class TestCrawler(unittest.TestCase):
    #Test class init with valid parameters
    def testInitOK(self):
        ws1 = Crawler(OKSites)
        
        self.assertEqual(ws1.queue.qsize(), len(OKSites)),
        self.assertEqual(ws1.mode, "auto")     
        
        ws2 = Crawler(OKSites, mode="manual")
        self.assertEqual(ws2.mode, "manual")
    
    #Test class init with bad mode
    def testInitBadMode(self):
        with self.assertRaises(TypeError):
            ws1 = Crawler(OKSites, mode="bad", autoQueue=True)
    
    #Test class init start URLs working correctly
    def testInitURLValidity(self):
        ws1 = Crawler(OKSites)
        ws2 = Crawler(OKSites, allowed_urls=OKSites)
        
        self.assertEqual(ws1.queue.qsize(), len(OKSites))
        
        self.assertEqual(ws1.queue.qsize(), len(OKSites))
    
    #Test class init start URLs bad input
    def testInitBadURLValidity1(self):    
        with self.assertRaises(TypeError):
            ws1 = Crawler(BADSites)
    
    #Test class init start URLs bad input      
    def testInitBadURLValidity2(self):
        with self.assertRaises(TypeError):
            ws3 = Crawler(OKSites, allowed_urls=BADSites)

if __name__ == "__main__":
    unittest.main()
