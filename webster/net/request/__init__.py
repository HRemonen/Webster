import pycurl

from io import BytesIO 
from typing import Optional
from urllib.parse import urlparse

from utils import validators


class Request(object):
    """
    A class that represents a HTTP request object.
    
    Attributes
    ----------
    url : str
        URL to request data from.
        URL must be in correct form: 
        ex. https://example.com/ or https://www.example.com/
       
    method : str, default = "GET".
        Request method.

    body : (Optional) bytes, default = None.
        Request body. Will be stored as bytes, 
        encoded using utf-8.
        
    encoding : str, default = "utf-8".
        Encoding of request. Encoding is used to encode 
        request body to bytes.
        Also allows for decoding bytes to string.
    
    Methods
    -------
    get()
        Returns bytes object of HTTP request.
    
    """

    def __init__(
        self,
        url: str,
        method: str = "GET",
        encoding: str = "utf-8",
        body: Optional[bytes] = None,
    ) -> None:
        
        self._encoding = encoding
        self.method = str(method).upper()
        self.url = self._set_url(url)
        self.status_code = None
        
        if body is not None:
            if isinstance(body, bytes):
                self.body = body
            else: 
                raise TypeError(
                    "Expected body type of bytes, instead got: "
                    , type(body))
        else: self.body = self.__get()
        
    def _get_url(self) -> str:
        return self.url

    def _set_url(self, url: str) -> str:
        if validators.URLValidator(url):
            return url

    def get(self) -> bytes:
        """
        Send GET request to server of the request class object.

        Returns
        -------
        bytes
            Website content.
        """
        return self.body
    
    def text(self) -> str:
        return self.body.decode(self._encoding)
    

    def base_url(self) -> str:
        """
        Get websites base URL (URL netloc) from the response object

        Returns
        -------
        string
            Base URL (<scheme>://<netloc>/)
        
        """
        request_url = urlparse(self.url)
        
        #Get the "base URL" for the relative URLs to work correctly
        #Base URL consist of URL scheme and netloc basically, ignore anything else.
        base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=request_url)
            
        return base_url
    
    
    def __get(self):
        """
        Helper function for request.get()
        
        This actually is where the magic happens.
        """

        data = None
        b = BytesIO()

        crl = pycurl.Curl()
        crl.setopt(pycurl.URL, self.url)
        crl.setopt(pycurl.FOLLOWLOCATION, 1)
        crl.setopt(pycurl.CONNECTTIMEOUT, 5)
        crl.setopt(pycurl.TIMEOUT, 8)
        crl.setopt(pycurl.WRITEDATA, b)

        try:
            crl.perform()
        except pycurl.error:
            return data
        
        data = b.getvalue()
        
        self.status_code = crl.getinfo(pycurl.HTTP_CODE)
        crl.close()
        
        return data 

    def __str__(self):
        return f"({self.status_code}) <{self.method} : {self.url}>"

    __repr__ = __str__

if __name__ == "__main__":
    url = "https://webscraper.io/test-sites"
    request = Request(url)
    print(request)
    
    
    
    test = "http://www.networkadvertising.org/choices/"
    test_req = Request(test)
    print(test_req)


    
    
    
