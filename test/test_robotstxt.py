import unittest

from webster.net.request import Request
from webster import robotstxt
from test.test_data import get_testdata, get_testrobots

class TestRobotsTxt(unittest.TestCase):
    #CONSTANTS
    MOCK_PAGES = ["https://www.example.com/", 
                  "https://www.example.com/index", 
                  "https://www.example.com/page1",
                  "https://www.example.com/page2"]
    
    #ALIASES
    request_class = Request
    
    #MOCKS
    mock_robots = get_testrobots("test_site", "robots.txt")
    mock_body = get_testdata("test_site", "index.html")
    mock_root = "https://www.example.com"
    mock_parser = robotstxt.RobotParser(mock_root)
    
    def testRobotParserBADInit(self):
        mock_root = "https://www."
        with self.assertRaises(ValueError):
            robotstxt.RobotParser(mock_root)
        
    def testRobotParserInit(self):
        mock_root = "https://www.example.com"
        mock_parser = robotstxt.RobotParser(mock_root)
        
        #Test url validity after RobotParser
        assert isinstance(mock_parser.root_url, str)
        self.assertEqual(mock_parser.root_url, mock_root)
    
    #Because urllib RobotParser does not allow for mocking
    #can not test with mock website...
    #Anyhow RobotParser has tests of its own, so we could trust
    #that this is fine.
    #Same goes for delay testing I am afraid.
    
    """
    def testAllowedAllUseragents(self):
        mock_root = "https://www.example.com"
        mock_parser = robotstxt.RobotParser(mock_root)
        
        #User agent * should allow crawling on all pages
        self.assertEqual(mock_parser.allowed(self.MOCK_PAGES[0], user_agent="*"), True)
        self.assertEqual(mock_parser.allowed(self.MOCK_PAGES[1], user_agent="*"), False)
        self.assertEqual(mock_parser.allowed(self.MOCK_PAGES[2], user_agent="*"), True)
        

    def testDisallowedHenebot(self):
        mock_root = "https://www.example.com"
        mock_parser = robotstxt.RobotParser(mock_root)
        
        #User agent Henebot should not be allowed to crawl any pages
        self.assertEqual(mock_parser.allowed(self.MOCK_PAGES[0], user_agent="Henebot"), False)
        self.assertEqual(mock_parser.allowed(self.MOCK_PAGES[1], user_agent="Henebot"), False)
        self.assertEqual(mock_parser.allowed(self.MOCK_PAGES[2], user_agent="Henebot"), False)
    """
    
    
if __name__ == "__main__":
    unittest.main()   