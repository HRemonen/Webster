import pycurl

from io import BytesIO 
from typing import Optional

from webster.utils import url_tools
from webster.utils import validators


class Request:
    
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
    get
        Returns Webster.net.Request object of HTTP request.
    
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
        return url_tools.base_url(self.url)
    
    def __get(self):
        """
        Helper function for request.get()
        
        This actually is where the magic happens.
        """

        data = None
        b = BytesIO()

        try:
            crl = pycurl.Curl()
            crl.setopt(pycurl.URL, self.url)
            crl.setopt(pycurl.FOLLOWLOCATION, 1)
            crl.setopt(pycurl.CONNECTTIMEOUT, 5)
            crl.setopt(pycurl.TIMEOUT, 8)
            crl.setopt(pycurl.WRITEDATA, b)
            crl.perform()
            
        except (pycurl.error, TypeError):
            #Something went wrong requesting.
            #Could be connection timeout, bad url, no network
            #connection or other stuff
            
            #Return none data. 
            return data
        
        data = b.getvalue()
        
        self.status_code = crl.getinfo(pycurl.HTTP_CODE)
        crl.close()
        
        return data 

    def __str__(self):
        return f"({self.status_code}) <{self.method} : {self.url}>"

    __repr__ = __str__