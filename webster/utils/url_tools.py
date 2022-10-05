"""
Helper file for URL related stuff

"""
from urllib.parse import urlparse


def netloc_url(url: str) -> str:
    """
    Get websites URL netloc from the URL string.

    Returns
    -------
    string
        netloc URL (<netloc>)
    
    """
    if not isinstance(url, str):
        raise TypeError(
                "Expected URL type of string, instead got: "
                , type(input))
    
    url = urlparse(url)
        
    netloc = '{uri.netloc}'.format(uri=url)
        
    return netloc

def base_url(url: str) -> str:
    """
    Get websites base URL from the URL string.

    Returns
    -------
    string
        Base URL (<scheme>://<netloc>)
    
    """
    if not isinstance(url, str):
        raise TypeError(
                "Expected URL type of string, instead got: "
                , type(input))
    
    url = urlparse(url)
        
    #Get the "base URL" for the relative URLs to work correctly
    #Base URL consist of URL scheme and netloc basically, ignore anything else.
    #Skip the bogus urls where there is scheme or netloc missing.
    if not url[0] or not url[1]:
        return ""
    base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
            
    return base_url