import pycurl
import lxml

from io import BytesIO 

from typing import List, Optional, Union

import crawler
from utils import validators


class Request(object):
    """
    A class that represents a HTTP request object.
    
    Attributes
    ----------
    url : list
       
    method : str, default = "GET".
        Request method.
         
    headers : (Optional) dict, default = None.
        HTTP request headers to be send with the request to the server.

    body : (Optional) bytes, default = None.
        Request body. Will be stored as bytes.
    
    cookies : (Optional) dict or list of dicts, default = None.
        HTTP request cookies to be send with the request to the server.
        
    encoding : str, default = "utf-8".
        Encoding of request. Encoding is used to encode request body to bytes.
    
    Methods
    -------
    get()
        Returns bytes object of HTTP request.
    
    """

    def __init__(
        self,
        url: str,
        method: str = "GET",
        headers: Optional[dict] = None,
        body: Optional[bytes] = None,
        cookies: Optional[Union[dict, List[dict]]] = None,
        encoding: str = "utf-8",
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
        
        self.get = self.get()
        
    def _get_url(self) -> str:
        return self._url

    def _set_url(self, url: str) -> str:
        if validators.URLValidator(url):
            return url

    def _get_body(self) -> bytes:
        return self._body

    def get(self) -> bytes:
        """
        GET request.
        Returns bytes of the request
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

        return body

    def __str__(self):
        return f"{self.method} : {self.url}"

    __repr__ = __str__

if __name__ == "__main__":
    url = "https://webscraper.io/test-sites"
    request = Request(url)
    
