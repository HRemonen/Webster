"""
Helper file for response related stuff

"""
import requests

from urllib.parse import urlparse

def base_url(response: object) -> str:
    """
    Get websites base URL (URL netloc) from the downloaded file.

    Returns
    -------
    string
        Base URL (<scheme>://<netloc>/)
    
    """
    
    if not isinstance(response, requests.Response):
            raise TypeError("Response object was not of accepted type")
    else: response_url = urlparse(response.url)
        
    #Get the "base URL" for the relative URLs to work correctly
    #Base URL consist of URL scheme and netloc basically, ignore anything else.
    base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=response_url)
        
    return base_url

def http_response(url: str) -> object:
    """
    Return http response using requests package
    """
    try:
        response = requests.get(url, timeout=2)
        return response
    except requests.RequestException:
        print("Something went wrong requesting page")
    

if __name__ == "__main__":
    s = "https://www.youtube.com/"
    response = http_response(s)
    
          