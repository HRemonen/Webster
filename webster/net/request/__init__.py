import pycurl

from io import BytesIO 
from typing import List, Optional, Union
from urllib.parse import urlparse

from utils import validators


class Request(object):
    """
    A class that represents a HTTP request object.
    
    Attributes
    ----------
    url : str
        URL to request data from.
        URL must be in correct form: ex. https://example.com/ or https://www.example.com/
       
    method : str, default = "GET".
        Request method.
         
    headers : (Optional) dict, default = None.
        HTTP request headers to be send with the request to the server.

    body : (Optional) bytes, default = None.
        Request body. Will be stored as bytes, encoded using utf-8.
    
    cookies : (Optional) dict or list of dicts, default = None.
        HTTP request cookies to be send with the request to the server.
        
    encoding : str, default = "utf-8".
        Encoding of request. Encoding is used to encode request body to bytes.
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
        headers: Optional[dict] = None,
        cookies: Optional[Union[dict, List[dict]]] = None,
    ) -> None:
        
        self._encoding = encoding
        self.method = str(method).upper()
        self.url = self._set_url(url)
        
        if body is not None:
            if isinstance(body, bytes):
                self.body = body
            else: 
                raise TypeError(
                    "Expected body type of bytes, instead got: "
                    , type(body))
        else: self.body = None
        
    def _get_url(self) -> str:
        return self.url

    def _set_url(self, url: str) -> str:
        if validators.URLValidator(url):
            return url

    def _get_body(self) -> bytes:
        return self.body
    
    def _get_body_string(self) -> str:
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
    
    def get(self) -> bytes:
        """
        Send GET request to server of the request class object.

        Returns
        -------
        bytes
            Website content.
        
        """
        
        b = BytesIO() 
        crl = pycurl.Curl() 

        # Set URL value
        crl.setopt(crl.URL, self.url)

        # Write bytes that are utf-8 encoded
        crl.setopt(crl.WRITEDATA, b)

        crl.perform() 
        crl.close()

        # Get the content stored in the BytesIO object (in byte characters) 
        body = b.getvalue()
        
        self.body = body

        return self.body

    def __str__(self):
        return f"{self.method} : {self.url}"

    __repr__ = __str__

if __name__ == "__main__":
    url = "https://webscraper.io/test-sites"
    request = Request(url)
    print(request.base_url())
    
    
    
    test = "https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en"
    request = Request(test)
    response = request.get()
    print(response)
    
    
    
