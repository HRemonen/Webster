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
        url = "https://github.com/HRemonen/Webster/"
        
        validate = validators.URLValidator(url)
        
        self.assertTrue(validate)
        
    def testURLValidatorListOK(self):
        url = ["https://github.com/HRemonen/Webster/"]
        
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
                "https://example.org",
                ]
        
        with self.assertRaises(TypeError):
            validators.URLValidator(urls)
    
    def testURLValidatorScheme(self):
        self.assertTrue(validators.URLValidator("https://example.org"))
        self.assertTrue(validators.URLValidator("http://example.org"))
        self.assertTrue(validators.URLValidator("ftp://example.org"))
     
    def testURLValidatorNotSupportedScheme(self):
        self.assertFalse(validators.URLValidator("mailto:info@remonen.fi"))
        self.assertFalse(validators.URLValidator("data:remonen"))
        self.assertFalse(validators.URLValidator("about:remonen"))
    
    
    def testURLValidatorNoScheme(self): 
        self.assertRaises(TypeError, validators.URLValidator("asd"))
        self.assertRaises(TypeError, validators.URLValidator("/asd"))
        self.assertRaises(TypeError, validators.URLValidator("/asd/"))
        self.assertRaises(TypeError, validators.URLValidator("/asd:foo"))

if __name__ == "__main__":
    unittest.main()