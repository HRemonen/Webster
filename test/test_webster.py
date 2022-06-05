import queue
import unittest

from webster.core import webster as ws

PARAM2 = "https://google.com/"
PARAM21 = ["https://google.com/", 
            "https://github.com/", 
            "https://youtube.com/"]
PARAM21BAD = ["google.com/", 
            "https://.com/", 
            "https://youtube./"]


class TestWebster(unittest.TestCase):
    def testInitOK(self):
        ws1 = ws.Webster(PARAM2)
        
        self.assertEqual(ws1.start_urls, PARAM2), "Starting website not correct"
        self.assertEqual(ws1.queue.qsize(), 0), "queue size not matching should be 0 when only one URL is provided"
        self.assertEqual(ws1.mode, "auto"), "mode not correct, should be auto by default"           
        
        ws2 = ws.Webster(PARAM2, mode="manual")
        self.assertEqual(ws2.mode, "manual"), "mode not correct, should be manual but now it is auto"
        
    def testInitBadMode(self):
        #Test class init with bad mode
        with self.assertRaises(TypeError):
            ws1 = ws.Webster(PARAM2, mode="bad", autoQueue=True)
        
    def testInitURLValidity(self):
        ws1 = ws.Webster(PARAM21)
        ws2 = ws.Webster(PARAM2, allowed_urls=PARAM21)
        
        self.assertEqual(ws1.start_urls, PARAM21[0])
        self.assertEqual(ws1.queue.qsize(), len(PARAM21)-1)
        
        self.assertEqual(ws2.start_urls, PARAM2)
        
    def testInitBadURLValidity1(self):
        badSites = ["google.com/", 
                    "https://.com/", 
                    "https://youtube./"]
        badSite = "https://.com/"
        
        with self.assertRaises(TypeError):
            ws1 = ws.Webster(PARAM21BAD)
        with self.assertRaises(TypeError):
            ws2 = ws.Webster(PARAM21BAD[0])
            
    def testInitBadURLValidity2(self):
        with self.assertRaises(RuntimeError):
            ws3 = ws.Webster(PARAM21, allowed_urls=PARAM21BAD)

if __name__ == "__main__":
    unittest.main()
