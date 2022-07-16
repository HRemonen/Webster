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
    
    def testURLValidatorBADListInput(self):
        url = [1, 2, 3]
        
        with self.assertRaises(TypeError):
            validators.URLValidator(url)
            
    def testURLValidatorMAIL(self):
        url = "mailto:info@remonen.fi"
        
        validate = validators.URLValidator(url)
        
        self.assertFalse(validate)
    
    def testURLValidatorNoScheme(self):
        url = "github.com/"
        
        validate = validators.URLValidator(url)
        
        self.assertFalse(validate)
    
if __name__ == "__main__":
    unittest.main()