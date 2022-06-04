import unittest

from src.webster import webster as ws


class TestWebster(unittest.TestCase):
    
    def testWebsterWithOneWebsiteNoOtherParameters(self):
        ws1 = ws.Webster("https://google.com/")
        
        self.assertEqual(ws1.start, "https://google.com/")
        self.assertEqual(ws1.queue.qsize(), 0)
        self.assertEqual(ws1.mode, "auto")
        self.assertEqual(ws1.autoQueue, False)
        
    def testWebsterWithModeAndAutoQueue(self):
        ws1 = ws.Webster("https://github.com/", mode="manual", autoQueue=True)
        
        self.assertEqual(ws1.start, "https://github.com/")
        self.assertEqual(ws1.queue.qsize(), 0)
        self.assertEqual(ws1.mode, "manual")
        self.assertEqual(ws1.autoQueue, True)
        
    def testWebsterWithMultipleWebsites(self):
        sites = ["https://google.com/", 
                "https://github.com/", 
                "https://youtube.com/"]
        
        ws1 = ws.Webster(sites)
        
        self.assertEqual(ws1.start, sites[0])
        self.assertEqual(ws1.queue.qsize(), len(sites)-1)
        


if __name__ == "__main__":
    unittest.main()
