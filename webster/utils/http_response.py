"""
Helper file for response related stuff

"""
import requests

from urllib.parse import urlparse

def base_url(response: object) -> str:
    """
    Get websites base URL (URL netloc) from the response object

    Returns
    -------
    string
        Base URL (<scheme>://<netloc>/)
    
    """
    
    if not isinstance(response, requests.Response):
            raise TypeError(
                    "Expected response type of requests.Response, instead got: "
                    , type(response))
    else: response_url = urlparse(response.url)
        
    #Get the "base URL" for the relative URLs to work correctly
    #Base URL consist of URL scheme and netloc basically, ignore anything else.
    base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=response_url)
        
    return base_url

def netloc(url: str) -> str:
    """
    Get websites URL netloc from the response object

    Returns
    -------
    string
        Base URL (<netloc>)
    
    """
    url = urlparse(url)
        
    netloc = '{uri.netloc}'.format(uri=url)
        
    return netloc

def response(url: str) -> object:
    """
    Return http response using requests package
    """
    try:
        response = requests.get(url, timeout=2)
        return response
    except requests.RequestException:
        pass
    

if __name__ == "__main__":
    s = "https://www.youtube.com/"

    rsp = response(s)
    print(rsp.url)
    
          