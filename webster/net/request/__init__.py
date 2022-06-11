import pycurl
from io import BytesIO 

from typing import Callable, List, Optional, Tuple, Type, TypeVar, Union

import crawler
from utils import validators


class Request(object):
    """
    Represents an HTTP request object.
    """

    def __init__(
        self,
        url: str,
        method: str = "GET",
        headers: Optional[dict] = None,
        body: Optional[bytes] = None,
        cookies: Optional[Union[dict, List[dict]]] = None,
        meta: Optional[dict] = None,
        encoding: str = "utf-8",
    ) -> None:
        
        self._encoding = encoding
        self.method = str(method).upper()
        self.url = self._set_url(url)
        self._meta = dict(meta) if meta else None
        
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
    print(request)
    
    print(Request(url, body=123))