import unittest

from webster.utils import validators

class TestModeValidator(unittest.TestCase):
    
    def testModeValidatorAUTO(self):
        mode = "auto"
        validate = validators.ModeValidator(mode)
        self.assertTrue(validate)
     
    def testModeValidatorMANUAL(self):    
        mode = "manual"
        validate = validators.ModeValidator(mode)
        self.assertTrue(validate)
    
    def testModeValidatorTypeError(self):
        mode = "BadMode"
        with self.assertRaises(TypeError):
            validators.ModeValidator(mode)
            
class TestURLValidator(unittest.TestCase):
    
    def testURLValidatorSingleURLOK(self):
        url = "https://www.example.com/"
        validate = validators.URLValidator(url)
        self.assertTrue(validate)
        
    def testURLValidatorListOK(self):
        url = ["https://www.example.com/"]
        validate = validators.URLValidator(url)
        self.assertTrue(validate)
        
    def testURLValidatorBADInput(self):
        url = 1
        with self.assertRaises(TypeError):
            validators.URLValidator(url)
            
        url = b""
        with self.assertRaises(TypeError):
            validators.URLValidator(url)
    
    def testURLValidatorBADListInput(self):
        url = [1, 2, 3]
        with self.assertRaises(TypeError):
            validators.URLValidator(url)
            
        urls = [1, 
                "https://example.com",
                "https://www.example.com/"
                ]
        with self.assertRaises(TypeError):
            validators.URLValidator(urls)
    
    def testURLValidatorScheme(self):
        self.assertTrue(validators.URLValidator("https://example.com"))
        self.assertTrue(validators.URLValidator("http://example.com"))
        self.assertTrue(validators.URLValidator("ftp://example.com"))
     
    def testURLValidatorNotSupportedScheme(self):
        with self.assertRaises(ValueError):
            validators.URLValidator("mailto:info@remonen.fi")
            
        with self.assertRaises(ValueError):
            validators.URLValidator("data:remonen")
            
        with self.assertRaises(ValueError):    
            validators.URLValidator("about:remonen")
    
    def testURLValidatorNoScheme(self): 
        with self.assertRaises(ValueError):
            validators.URLValidator("asd")
            
        with self.assertRaises(ValueError):
            validators.URLValidator("/asd")
            
        with self.assertRaises(ValueError):
            validators.URLValidator("/asd/")
            
        with self.assertRaises(ValueError):
            validators.URLValidator("/asd:foo")

if __name__ == "__main__":
    unittest.main()