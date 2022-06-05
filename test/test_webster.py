import queue
import unittest

from src.webster import webster as ws


class TestWebster(unittest.TestCase):
    def testInitOK(self):
        ws1 = ws.Webster("https://google.com/")
        
        self.assertEqual(ws1.start, "https://google.com/"), "Starting website not correct"
        self.assertEqual(ws1.queue.qsize(), 0), "queue size not matching should be 0 when only one URL is provided"
        self.assertEqual(ws1.mode, "auto"), "mode not correct, should be auto by default"           
        self.assertEqual(ws1.autoQueue, False), "autoqueue not correct, should be False by default"
        
        ws2 = ws.Webster("https://google.com/", mode="manual")
        self.assertEqual(ws2.mode, "manual"), "mode not correct, should be manual but now it is auto"
        
    def testInitBadMode(self):
        #Test class init with bad mode
        with self.assertRaises(TypeError):
            ws1 = ws.Webster("https://github.com/", mode="bad", autoQueue=True)
            
    def testInitBadAutoQueue(self):      
        #Test class init with bad autoQueue input
        with self.assertRaises(TypeError):
            ws1 = ws.Webster("https://github.com/", autoQueue="True")
        
    def testInitURLValidity(self):
        sites = ["https://google.com/", 
                    "https://github.com/", 
                    "https://youtube.com/"]
        site = "https://www.github.com/" 
        ws1 = ws.Webster(sites)
        ws2 = ws.Webster(site)
        
        self.assertEqual(ws1.start, sites[0])
        self.assertEqual(ws1.queue.qsize(), len(sites)-1)
        
        self.assertEqual(ws2.start, site)
        
    def testInitBadURLValidity(self):
        badSites = ["google.com/", 
                    "https://.com/", 
                    "https://youtube./"]
        badSite = "https://.com/"
        
        with self.assertRaises(TypeError):
            ws1 = ws.Webster(badSites)
        with self.assertRaises(TypeError):
            ws2 = ws.Webster(badSite)

if __name__ == "__main__":
    unittest.main()
