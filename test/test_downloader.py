import unittest

from pathlib import Path

from webster.conf import settings
from webster.net.request import Request
from webster.core.downloader import Downloader
from test.test_data import get_testdata


class TestDownloader(unittest.TestCase):
    #ALIASES
    request_class = Request
    downloader_class = Downloader
    
    #MOCKS
    mock_body = get_testdata("test_site", "index.html")
    mock_request = Request(url="https://www.example.com/index", body=mock_body)
    
    def testDownloaderBADInit(self):
        #Downloader must have a Request object as parameter.
        #Except to raise TypeError when initializing.
        
        #Test without parameters
        self.assertRaises(TypeError, self.downloader_class)
        
        #Test with bad parameter type
        self.assertRaises(TypeError, self.downloader_class, "Request")
        
    def testParserInit(self):
        r = self.request_class(url="https://www.example.com")
        dlr = self.downloader_class(request=r)
        
        #Test Downloader request is Request
        assert isinstance(dlr.get_request(), Request)
        
        #After init filename and filepaths are None type.
        self.assertEqual(dlr.filename, None)
        self.assertEqual(dlr.filepath, None)
        
    def testDownloadTestData(self):
        body = get_testdata("test_site", "index.html")
        r = Request(url="https://www.example.com/", body=body)
        
        dlr = self.downloader_class(request=r)
        
        self.assertEqual(dlr.get_request(), r)
        self.assertEqual(dlr.filename, None)
        self.assertEqual(dlr.filepath, None)
        
        #After this filename and filepath should have changed
        dlr.download()
        self.assertEqual(dlr.request.url, r.url)
        assert isinstance(dlr.filename, str)
        assert isinstance(dlr.filepath, str)
        
    def testDownloadFolderAndFileCreated(self):
        body = get_testdata("test_site", "index.html")
        r = Request(url="https://www.example.com/", body=body)
        
        dlr = self.downloader_class(request=r)
        dlr.download()
        
        #Directory and filepaths for testing
        dl_dir = Path(settings.PATH.join(settings.DL_DIR))
        p = Path(dlr.filepath)

        #Assert that the file and folder is created
        self.assertTrue(p.exists())
        self.assertFalse(p.is_dir())
        self.assertTrue(dl_dir.is_dir())
        
if __name__ == "__main__":
    unittest.main()