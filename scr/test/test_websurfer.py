import unittest
import surfer

from surfer import websurfer
from surfer.websurfer import WebSurfer as ws

class TestWebSurfer(unittest.TestCase):
    
    def testWebSurfesWithOneWebsiteNoOtherParameters(self):
        ws1 = ws.WebSurfer("https://google.com/")
        
        self.assertEqual(ws1.start, "https://google.com/")
        self.assertEqual(ws1.queue.qsize(), 0)
        self.assertEqual(ws1.mode, "auto")
        self.assertEqual(ws1.autoQueue, False)
        
    def testWebSurferWithModeAndAutoQueue(self):
        ws1 = ws.WebSurfer("https://github.com/", mode="manual", autoQueue=True)
        
        self.assertEqual(ws1.start, "https://google.com/")
        self.assertEqual(ws1.queue.qsize(), 0)
        self.assertEqual(ws1.mode, "manual")
        self.assertEqual(ws1.autoQueue, True)
        
    def testWebSurferWithMultipleWebsites(self):
        sites = ["https://google.com/", 
                "https://github.com/", 
                "https://youtube.com/"]
        
        ws1 = ws.WebSurfer(sites)
        
        self.assertEqual(ws1.start, sites[0])
        self.assertEqual(ws1.queue.qsize(), len(sites)-1)
        

        

if __name__ == "__main__":
    unittest.main()
