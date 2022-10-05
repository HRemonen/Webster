import unittest
import queue

from types import NoneType
from webster.crawler import Crawler

class TestCrawler(unittest.TestCase):
    #TEST DATA URLS
    TEST_URL = "https://www.example.com/index"
    
    def testCrawlerInitBAD(self):
        with self.assertRaises((ValueError, TypeError)):
            Crawler([123])
        with self.assertRaises((ValueError, TypeError)):
            Crawler("abadsf") 
        with self.assertRaises((ValueError, TypeError)):
            Crawler([self.TEST_URL], allowed_urls=[123])
        with self.assertRaises((ValueError, TypeError)):
            Crawler([self.TEST_URL], allowed_urls="adf") 
    
    def testCrawlerInitNoAllowed(self):
        ws = Crawler([self.TEST_URL])
        assert isinstance(ws.start_urls, list)
        assert isinstance(ws.allowed_urls, NoneType)
        self.assertEqual(ws.allowed_urls, None)
        self.assertEqual(ws.mode, "auto")
        self.assertFalse(ws.crawling)
        
        assert isinstance(ws.queue, queue.Queue)
        assert isinstance(ws.responses, dict)
        assert isinstance(ws.robots_allowed, dict)
        assert isinstance(ws.robots_excluded, dict)
        
    def testCrawlerInitWithAllowed(self):
        ws = Crawler([self.TEST_URL], allowed_urls=["https://www.example.com/"])
        assert isinstance(ws.start_urls, list)
        assert isinstance(ws.allowed_urls, list)
        self.assertEqual(ws.allowed_urls, ["https://www.example.com/"])
        self.assertEqual(ws.mode, "auto")
        self.assertFalse(ws.crawling)
        
        assert isinstance(ws.queue, queue.Queue)
        assert isinstance(ws.responses, dict)
        assert isinstance(ws.robots_allowed, dict)
        assert isinstance(ws.robots_excluded, dict)
    
    def testCrawlerBADAllowedUrls(self):
        ws = Crawler([self.TEST_URL], allowed_urls=["https://ex.com/"])                             
        xs = ws.crawl()
        assert isinstance(ws.start_urls, list)
        assert isinstance(ws.allowed_urls, list)
        
        assert isinstance(xs, dict)
        self.assertEqual(xs, {})
        
        ws = Crawler([self.TEST_URL], allowed_urls=["https://remonen.fi/"])                         
        xs = ws.crawl()
        assert isinstance(ws.start_urls, list)
        assert isinstance(ws.allowed_urls, list)
        
        assert isinstance(xs, dict)
        self.assertEqual(xs, {})
    
    def testCrawlerBADAllowedTypes(self):
        with self.assertRaises(TypeError):
            Crawler([self.TEST_URL], allowed_urls=[123])
            
        with self.assertRaises(TypeError):
            Crawler([self.TEST_URL], allowed_urls=123)
            
        with self.assertRaises(TypeError):
            Crawler([self.TEST_URL], allowed_urls=b"")    
               
        with self.assertRaises(TypeError):                              
            Crawler([self.TEST_URL], allowed_urls=b"c4")
            
        with self.assertRaises(ValueError):    
            Crawler([self.TEST_URL], allowed_urls="badbadbad")  
    
    def testCrawlerBADStartingURL(self):
        url = "https://example.com/"

        with self.assertRaises(ValueError):                                            
            Crawler(list(url), allowed_urls=[])   
        with self.assertRaises(ValueError): 
            Crawler("abcd.efg", allowed_urls=[])                                       
    
    def testCrawlerSomeBADStartingURLS(self):
        urls = ["https://example.com/",
                "https://remonen.fi/",
                "abdhs",
                1234,
                "https://is.fi/"]
        
        with self.assertRaises((TypeError, ValueError)):                                            
            Crawler(urls, allowed_urls=["https://example.com/"])


    def testCrawlerSomeIncorrectStartingURLS(self):
        urls = ["https://example.com/",
                "https://remonen.fi/",
                "abdhs",
                ]      
        with self.assertRaises(ValueError):                                            
            Crawler(urls, allowed_urls=["https://example.com/"])                      

    
    def testCrawlerValid(self):
        ws = Crawler([self.TEST_URL], allowed_urls=["https://example.com/"])                         
        xs = ws.crawl()
        assert isinstance(ws.start_urls, list)
        assert isinstance(ws.allowed_urls, list)
        
        assert isinstance(xs, dict)


if __name__ == "__main__":
    unittest.main()